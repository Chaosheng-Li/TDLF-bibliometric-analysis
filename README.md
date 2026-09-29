# TDLF-bibliometric-analysis

Supporting data, scripts and software-configuration records for the bibliometric
analysis of **Topological Deep Learning in Finance (TDLF)**.

[中文说明](#中文说明) | [English](#english)

---

## 中文说明

### 概述

本仓库提供论文 *Topological Deep Learning in Finance: A Bibliometric Analysis of
the Financial Machine-Learning Literature and a Research Agenda* 中文献计量分析的
全部支撑材料，包括原始下载数据、清洗后的分析数据、VOSviewer / CiteSpace 的配置
文件与分析输出记录。

分析对象为 Web of Science Core Collection 中 1997–2025 年的 **1,207 篇**文献。

### 数据

| 路径 | 说明 |
| --- | --- |
| `download_Rawdata_1.4/` | **原始下载数据。** WoS 分三批导出的原始记录（1–500、501–1000、1001–1415）。 |
| `final_analyzed_data/` | **数据清洗后本论文用于分析的最终数据。** 含逐年的 WoS 导出记录 `download<年份>u<序号>.txt`（1997–2025），以及最终 1,207 篇文献的 DOI 清单 `doi_1207.list`。 |
| `Number_of_publications_per_year.xlsx` | 该领域**每年发表文章的数量**。 |

### 脚本

| 文件 | 说明 |
| --- | --- |
| `3.1 Trends in publications.py` | 用于**统计和绘制**该领域每年发表文章的数量与趋势。 |

### VOSviewer thesaurus 文件

| 文件 | 对应的分析 |
| --- | --- |
| `3.3.1-3country_thesaurus.txt` | Country cooperation networks analysis |
| `3.3.2-3institution_thesaurus.txt` | Institution collaboration network analysis |
| `3.3.3-3author_thesaurus.txt` | Author collaboration network analysis |
| `3.4.1-3-5keyword__thesaurus.csv` | High-frequency keyword analysis |

### CiteSpace 配置文件

| 文件 | 说明 |
| --- | --- |
| `citespace.alias` | CiteSpace 的**合并（alias）文件**。 |
| `citespace.exclusion` | CiteSpace 的**排除文件**。 |

以上两个文件均用于下列三项分析：

- Analysis of timeline visualization mapping for keyword clustering
- Analysis of co-cited reference network
- Analysis keyword burst

### CiteSpace 分析输出记录

| 路径 | 说明 |
| --- | --- |
| `3.4.3 Analysis of timeline visualization mapping for keyword clustering/` | 关键词聚类时间线可视化分析产生的记录。 |
| `3.4.4 Analysis of co-cited reference network/` | 共被引网络分析产生的记录。 |
| `3.4.5 Analysis keyword burst/` | 关键词突现分析产生的记录。 |

各目录内包含 CiteSpace 导出的 `.graphml`、`.viz`、`CitationBurst.in` / `.out`、
参数文件与图像等。

### 鲁棒性分析

| 路径 | 说明 |
| --- | --- |
| `robustness/` | 确定 **g-index scale factor k 值**的鲁棒性分析记录。按 `k15/`、`k20/`、`k25/` 分为三组，每组各自重复上述三项 CiteSpace 分析（子目录 `3.4.3/`、`3.4.4/`、`3.4.5/`）。 |

### 分析工具

- **CiteSpace** 6.4.R1 (Advanced)
- **VOSviewer** 1.6.20

---

## English

### Overview

This repository provides the supporting material for the bibliometric analysis
in *Topological Deep Learning in Finance: A Bibliometric Analysis of the
Financial Machine-Learning Literature and a Research Agenda*. It contains the
raw downloaded records, the cleaned analysis data, and the VOSviewer / CiteSpace
configuration files and analysis outputs.

The corpus comprises **1,207 publications** from the Web of Science Core
Collection, spanning 1997–2025.

### Data

| Path | Description |
| --- | --- |
| `download_Rawdata_1.4/` | **Raw downloaded data.** The original Web of Science export, split into three batches (records 1–500, 501–1000, 1001–1415). |
| `final_analyzed_data/` | **The final, cleaned data used for the analysis in this paper.** Contains the per-year Web of Science exports `download<year>u<index>.txt` (1997–2025) and `doi_1207.list`, the DOI list of the final 1,207 publications. |
| `Number_of_publications_per_year.xlsx` | The **number of publications per year** in this field. |

### Script

| File | Description |
| --- | --- |
| `3.1 Trends in publications.py` | Script used to **count and plot** the annual number of publications and the publication trend. |

### VOSviewer thesaurus files

| File | Used for |
| --- | --- |
| `3.3.1-3country_thesaurus.txt` | Country cooperation networks analysis |
| `3.3.2-3institution_thesaurus.txt` | Institution collaboration network analysis |
| `3.3.3-3author_thesaurus.txt` | Author collaboration network analysis |
| `3.4.1-3-5keyword__thesaurus.csv` | High-frequency keyword analysis |

### CiteSpace configuration files

| File | Description |
| --- | --- |
| `citespace.alias` | CiteSpace **alias (merge) file**. |
| `citespace.exclusion` | CiteSpace **exclusion file**. |

Both files are used for the following three analyses:

- Analysis of timeline visualization mapping for keyword clustering
- Analysis of co-cited reference network
- Analysis keyword burst

### CiteSpace analysis records

| Path | Description |
| --- | --- |
| `3.4.3 Analysis of timeline visualization mapping for keyword clustering/` | Records produced by the keyword-clustering timeline visualization analysis. |
| `3.4.4 Analysis of co-cited reference network/` | Records produced by the co-cited reference network analysis. |
| `3.4.5 Analysis keyword burst/` | Records produced by the keyword burst analysis. |

Each directory contains CiteSpace exports such as `.graphml` and `.viz` files,
`CitationBurst.in` / `.out`, parameter files and figures.

### Robustness analysis

| Path | Description |
| --- | --- |
| `robustness/` | Records of the robustness analysis used to determine the **g-index scale factor `k`**. Organised as `k15/`, `k20/` and `k25/`, each repeating the three CiteSpace analyses above in its own `3.4.3/`, `3.4.4/` and `3.4.5/` subdirectories. |

### Software

- **CiteSpace** 6.4.R1 (Advanced)
- **VOSviewer** 1.6.20
