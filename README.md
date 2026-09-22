# AI-Powered Customer Churn Analysis and Prediction

## Project Overview
Developed for the **IBM SkillsBuild Data Analytics with AI Academic Internship** by **Ashish**.

This project delivers an end-to-end Machine Learning and Business Intelligence solution designed to analyze customer retention drivers, identify churn risk factors, and accurately predict churn probability for telecommunications subscribers using the Telco dataset.

---

## Dataset
* **Dataset Source:** [Telco Customer Churn Dataset (Kaggle)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
* **Local Data Path:** `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`

---

## Business Intelligence (BI) Dashboard Framework
1. **Level 1 (KPIs)**: Total Customers (7,043), Churn Rate (26.54%), Avg Monthly Spend ($64.76).
2. **Level 2 (Trends)**: Tenure vs. Billing Trajectory Analysis.
3. **Level 3 (Drivers)**: Month-to-Month Contracts & Electronic Check payment method as key churn drivers.
4. **Level 4 (Risk)**: Machine Learning Risk Scoring (`model/churn_model.pkl`).
5. **Level 5 (Action)**: Proactive Retention Strategies & Targeted Discount Workflows.

---

## Feature Summary
| Category | Features Included |
| :--- | :--- |
| **Demographics** | Gender, Senior Citizen, Partner, Dependents |
| **Account Info** | Tenure, Contract Type, Paperless Billing, Payment Method |
| **Services** | Phone Service, Multiple Lines, Internet Service, Online Security, Online Backup, Device Protection, Tech Support, Streaming TV, Streaming Movies |
| **Financials** | Monthly Charges, Total Charges |
| **Target Variable** | Churn (Yes / No) |

---

## Model Performance
| Metric | Score | Impact |
| :--- | :--- | :--- |
| **Accuracy** | 80.5% | High overall correct prediction rate |
| **Precision** | 79.2% | Low false-positive churn alerts |
| **Recall** | 78.8% | High churn capture rate |
| **ROC-AUC** | 0.84 | Strong class separation capability |

---

## Tech Stack
| Layer | Technology |
| :--- | :--- |
| **Language** | Python 3.13 |
| **Data & Viz** | Pandas, NumPy, Matplotlib, Seaborn |
| **ML Framework** | Scikit-Learn (Random Forest) |
| **IDE / Environment** | IBM Bob IDE / Jupyter Notebook |

---

## Project Structure
```text
IBM Customer Churn Project/
├── data/
│   └── WA_Fn-UseC_-Telco-Customer-Churn.csv
├── model/
│   └── churn_model.pkl
├── report_images/
│   ├── churn_by_contract.png
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── feature_importance.png
├── generate_images.py
├── Ashish_Telco_Churn.ipynb
├── Ashish_ProjectReport.docx
├── README.md
└── requirements.txt