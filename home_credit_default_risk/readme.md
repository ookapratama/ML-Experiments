# 🏦 Credit Scoring Model — Home Credit Case Study

## 📌 Project Overview
This project aims to build an end-to-end **credit scoring system** using machine learning to predict the probability of loan default.  
The objective is to support better lending decisions by balancing **risk mitigation** and **customer approval growth**.

The workflow covers:
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Multiple machine learning models
- Threshold tuning
- Business-oriented model comparison

---

## 🎯 Business Objective
- Identify customers with high default risk
- Reduce false approvals of risky customers
- Maintain a reasonable approval rate aligned with business strategy
- Provide interpretable insights for stakeholders

---

## 📂 Project Structure

```text
.
├── data/
│   ├── dataset/                 # Original datasets
│   ├── downloads/               # Get Dataset from Url
│   ├── processed/               # Cleaned & feature-engineered datasets
│   └── fetch_dataset.py         # Script for Download the Dataset
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_01_logistic_regression.ipynb
│   ├── 03_03_random_forest.ipynb
│   ├── 03_04_lightgbm.ipynb
│   └── 03_05_model_comparison.ipynb
│
├── assets/
│   ├── roc
│   └── cm
│
└── README.md
