import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats
from sklearn.metrics import r2_score


DATA_FILE = "Number_of_publications_per_year.xlsx"
EXPECTED_TOTAL = 1207          

df = pd.read_excel(DATA_FILE)
df = df[df["Year"] < 2026].copy()   
df = df.sort_values("Year").reset_index(drop=True)
df["Cumulative"] = df["Number"].cumsum()

total = int(df["Number"].sum())
print(f"语料年份范围: {df['Year'].min()}-{df['Year'].max()}, 年度数据点 n = {len(df)}")
print(f"1997-2025 累计发文总数 = {total}")
if total != EXPECTED_TOTAL:
    print(f"*** 警告: 累计总数 {total} != 论文声称的 {EXPECTED_TOTAL}，请核实年度数据来源！ ***")
else:
    print("*** OK: 累计总数与论文一致 ***")

# ------------------------------------------------------------------
# 指数增长模型: y = a * exp((x - x0) / t) + c   （拟合【累计】发文量）
# ------------------------------------------------------------------
def exp_growth(x, a, x0, t, c):
    return a * np.exp((x - x0) / t) + c

x = df["Year"].values
y = df["Cumulative"].values
popt, pcov = curve_fit(exp_growth, x, y, p0=[1, x.min(), 5, 0], maxfev=10000)
a_opt, x0_opt, t_opt, c_opt = popt
y_pred = exp_growth(x, *popt)
r2 = r2_score(y, y_pred)

n, k = len(x), 4                      # n 个观测, k 个参数
df_f = n - k - 1                      # 残差自由度
f_stat = (r2 / k) / ((1 - r2) / df_f) if r2 < 1 else np.inf

print("\n拟合对象: 1997-2025 累计发文量 | 方法: 非线性最小二乘 (Levenberg-Marquardt)")
print(f"y = {a_opt:.5f} * exp((x - {x0_opt:.4f}) / {t_opt:.4f}) + {c_opt:.5f}")
print(f"R2 = {r2:.4f} | F({k},{df_f}) = {f_stat:.1f}")

# 端点拟合值 vs 实际累计值（残差核对）
print("\n关键年份核对（预测累计 vs 实际累计）:")
for yy in (1997, 2013, 2019, 2020, 2024, 2025):
    m = df.loc[df["Year"] == yy]
    if not m.empty:
        pred = exp_growth(yy, *popt)
        act = float(m["Cumulative"].iloc[0])
        print(f"  x={yy}: 预测={pred:8.1f}  实际={act:5.0f}  残差={pred - act:+.1f}")
print(f"最大绝对残差 = {np.abs(y - y_pred).max():.1f} (年份 {x[np.argmax(np.abs(y - y_pred))]})")
print(f"RMSE = {np.sqrt(np.mean((y - y_pred)**2)):.1f}")

# ------------------------------------------------------------------
# 绘图
# ------------------------------------------------------------------
plt.rcParams["svg.fonttype"] = "none"
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(df["Year"], df["Number"], color="#FFD700", label="Number of publications annually",
        alpha=0.9, width=0.8, edgecolor="#CCAC00", linewidth=0.8)
ax1.set_xlabel("Publication years", fontsize=12, fontweight="bold")
ax1.set_ylabel("Number of publications annually", fontsize=12, fontweight="bold")

ax2 = ax1.twinx()
ax2.plot(df["Year"], df["Cumulative"], "D", color="#2F5597",
         label="Cumulative number of publications", markersize=5)
x_curve = np.linspace(x.min(), x.max(), 200)
y_curve = exp_growth(x_curve, *popt)
ax2.plot(x_curve, y_curve, "--", color="#C00000", label="Exponential Growth Fit", linewidth=2.5)
ax2.set_ylabel("Cumulative number of publications", fontsize=12, fontweight="bold")

ax1.set_xlim(df["Year"].min() - 1, df["Year"].max() + 1)
ax1.set_ylim(0, df["Number"].max() * 1.2)

plt.axvline(x=2013.5, color="black", linestyle="-.", alpha=0.6, linewidth=1)
plt.axvline(x=2019.5, color="black", linestyle="-.", alpha=0.6, linewidth=1)

y_max = df["Cumulative"].max()
plt.text(2001, y_max * 0.3, "Initial exploration", ha="center", fontsize=11, color="brown", fontweight="bold")
plt.text(2016.5, y_max * 0.5, "Steady growth", ha="center", fontsize=11, color="brown", fontweight="bold")
plt.text(2022.8, y_max * 0.8, "Rapid development", ha="center", fontsize=11, color="brown", fontweight="bold")

latex_eq = f"$\\mathbf{{y = {a_opt:.5f} \\cdot e^{{(x - {x0_opt:.4f}) / {t_opt:.4f}}} + {c_opt:.5f}}}$"
latex_r2 = f"$\\mathbf{{R^2 = {r2:.4f}}}$ (descriptive fit to cumulative counts)"
formula_text = f"{latex_eq}\n{latex_r2}"

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left",
           bbox_to_anchor=(0, 0.96), frameon=True, framealpha=0.9,
           fontsize=10, handlelength=1.5)

ax1.text(0.01, 0.76, formula_text, transform=ax1.transAxes,
         fontsize=11, color="black", va="top", family="monospace",
         bbox=dict(facecolor="white", edgecolor="gray", alpha=0.85, boxstyle="round,pad=0.4"))

plt.title("Trends in the annual and cumulative number of publications",
          fontsize=14, fontweight="bold", pad=15)
plt.tight_layout()

plt.savefig("Fig2_Publication_Trend.svg", format="svg", bbox_inches="tight")
plt.savefig("Fig2_Publication_Trend.pdf", format="pdf", bbox_inches="tight")
plt.savefig("Fig2_Publication_Trend.png", format="png", dpi=300, bbox_inches="tight")
print("\nSuccess! Charts saved as SVG, PDF, and PNG.")
plt.show()
