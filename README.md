# AI-Powered Customer Churn Analysis and Prediction

## Project Overview
Developed for the **IBM SkillsBuild Data Analytics with AI Academic Internship** by **Ashish**.

## Business Intelligence (BI) Dashboard Framework
1. **Level 1 (KPIs)**: Total Customers (7,043), Churn Rate (26.54%), Avg Monthly Spend (.76).
2. **Level 2 (Trends)**: Tenure vs Billing Trajectory Analysis.
3. **Level 3 (Drivers)**: Month-to-Month Contracts & Electronic Check root cause.
4. **Level 4 (Risk)**: Random Forest Risk Scoring (model/churn_model.pkl).
5. **Level 5 (Action)**: Retention Strategy & Discount Workflows.

## Feature Summary
| Category | Features Included |
| :--- | :--- |
| **Demographics** | Gender, Senior Citizen, Partner, Dependents |
| **Account Info** | Tenure, Contract Type, Paperless Billing, Payment Method |
| **Services** | Phone, Internet, Online Security, Tech Support |
| **Financials** | Monthly Charges, Total Charges |
| **Target Variable** | Churn (Yes / No) |

## Model Performance
| Metric | Score | Impact |
| :--- | :--- | :--- |
| Accuracy | 80.5% | Overall correct predictions |
| Precision | 79.2% | Low false positive churn alerts |
| Recall | 78.8% | High churn capture rate |
| ROC-AUC | 0.84 | Strong class separation |

## Tech Stack
| Layer | Technology |
| :--- | :--- |
| Language | Python 3.13 |
| Data & Viz | Pandas, NumPy, Matplotlib, Seaborn |
| ML Framework | Scikit-Learn (Random Forest) |
| IDE | IBM Bob IDE |

## Directory Structure
`	ext
IBM Customer Churn Project/
├── data/WA_Fn-UseC_-Telco-Customer-Churn.csv
├── model/churn_model.pkl
├── report_images/
├── Ashish_Telco_Churn.ipynb
├── Ashish_ProjectReport.docx
├── README.md
└── requirements.txt
`
