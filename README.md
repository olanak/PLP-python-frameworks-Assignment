Got it ✅ Let’s craft a **professional and advanced `README.md`** for your GitHub repo.
This will look polished, highlight your skills, and guide users through your project like a real-world data science portfolio.

---

# 📊 CORD-19 Metadata Analysis & Interactive Explorer

[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-ff4b4b)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-pandas-yellow)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Library-matplotlib-orange)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Library-seaborn-green)](https://seaborn.pydata.org/)

This project explores the **CORD-19 metadata dataset** (COVID-19 research papers) and demonstrates a **complete data science workflow**:

1. Data loading & exploration
2. Data cleaning & preparation
3. Descriptive analysis & visualization
4. Interactive **Streamlit web app** for exploration
5. Documentation & reflection

---

## 📂 Project Structure

```
Frameworks_Assignment/
│
├── notebooks/                  # Jupyter notebooks for step-by-step analysis
│   ├── Part1_Data_Exploration.ipynb
│   ├── Part2_Data_Cleaning.ipynb
│   ├── Part3_Analysis_Visualization.ipynb
│   └── Part5_Reflection.ipynb
│
├── app.py                      # Streamlit application
├── metadata_clean.csv          # Cleaned dataset (sample from Kaggle CORD-19)
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/Frameworks_Assignment.git
cd Frameworks_Assignment
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Key Findings

* **Dataset Overview**

  * Final cleaned dataset: ~29,491 records × 10 columns
  * Major missing values in `publish_time` (~96%)
  * All records retain titles, abstracts, authors, and journals after cleaning

* **Temporal Trends**

  * Publications span **2006–2020**
  * Massive spike in **2020** with 1,100+ papers

* **Top Journals**

  * *PLoS One*, *Emerg Infect Dis*, *Sci Rep*, *PLoS Pathog* lead publication counts

* **Sources**

  * Data aggregated from multiple repositories (PubMed, PMC, WHO, etc.)

* **Text Insights**

  * Titles average 8–15 words
  * Abstracts vary from ~50–300 words
  * Frequent terms: *COVID-19*, *coronavirus*, *infection*, *respiratory*

---

## 📷 Sample Visualizations

### Publications by Year

![Publications by Year](docs/publications_by_year.png)

### Word Cloud of Titles

![Word Cloud](docs/wordcloud_titles.png)

### Top Journals

![Top Journals](docs/top_journals.png)

---

## 🌐 Streamlit App Features

✅ Interactive **year range slider**
✅ **Dropdown filter** by source
✅ 📊 Charts: publications trend, top journals, top sources
✅ ☁ Word cloud of research titles
✅ 🔎 Raw data preview

---

## 🔍 Reflection

### Challenges

* **High missingness** in `publish_time` limited full temporal analysis
* **Authors field** contained unnormalized strings, complicating per-author stats
* Dataset size required sampling for efficient analysis

### Learnings

* Practical experience with **data cleaning strategies** (dropping vs imputing)
* Text analysis basics with **word frequency & word clouds**
* Building interactive dashboards using **Streamlit**
* End-to-end workflow: *load → clean → analyze → visualize → deploy*

---

## 📜 License

This project is for educational purposes. Data source: [CORD-19 Dataset (Allen Institute for AI)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge).

---

## 🙌 Acknowledgements

* [Allen Institute for AI](https://allenai.org/) for dataset
* [Streamlit](https://streamlit.io/) for rapid app development
* [Kaggle](https://www.kaggle.com/) community for open datasets

---

✨ Developed as part of **Frameworks Assignment** — demonstrating data science fundamentals with a real-world dataset.

---
