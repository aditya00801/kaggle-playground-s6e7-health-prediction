# 🏥 Student Health Risk Prediction

An end-to-end Machine Learning project that predicts a student's health condition based on lifestyle, physiological, and behavioral factors using an optimized **CatBoost Classifier**.

The project includes data preprocessing, feature engineering, hyperparameter optimization, model explainability, and deployment through a Streamlit web application.

---

## 🚀 Live Demo

**Streamlit App:** *(Add your deployed Streamlit URL here)*

---

## 📊 Project Overview

This project predicts one of the following health conditions:

- 🟢 Fit
- 🟡 At-Risk
- 🔴 Unhealthy

using student health and lifestyle information.

---

## 📈 Dataset

| Property | Value |
|----------|------:|
| Total Records | **690,088** |
| Target Classes | **3** |
| Original Features | **13** |
| Engineered Features | **20** |
| Total Features | **33** |

---

## 🧠 Final Model

| Property | Value |
|----------|------:|
| Algorithm | CatBoost Classifier |
| Hyperparameter Optimization | Optuna |
| Explainability | SHAP |
| Cross Validation | Stratified 5-Fold |
| Evaluation Metric | Balanced Accuracy |
| **Balanced Accuracy** | **94.985%** |

---

## ✨ Feature Engineering

The project creates several domain-specific features including:

- Activity Score
- Calories Per Step
- Water Per Exercise
- Exercise Sleep Ratio
- Steps Per Minute
- Calories Per Minute
- Activity Density
- Heart Activity
- Heart Steps
- BMI Sleep
- BMI Water
- Hydration Score
- Health Index
- BMI Category
- BMI Risk
- Stress Sleep
- Activity Diet
- Gender Activity
- Smoking Stress
- Diet Smoking

---

## 📂 Project Structure

```text
student-health-risk/
│
├── app.py
├── data/
├── notebooks/
├── output/
│   ├── models/
│   │   └── shrp_catboost_pro_v1_0.94985.cbm
│   └── submissions/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── utils.py
│
├── requirements.txt
└── README.md
```

---

## 🛠️ Technology Stack

- Python
- CatBoost
- Optuna
- SHAP
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Matplotlib
- Git & GitHub

---

## 📊 Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Data Preprocessing
      │
      ▼
Feature Engineering
      │
      ▼
Optuna Hyperparameter Optimization
      │
      ▼
CatBoost Training
      │
      ▼
SHAP Explainability
      │
      ▼
Final Production Model
      │
      ▼
Streamlit Deployment
```

---

## 📋 Input Features

### Numerical

- Sleep Duration
- Heart Rate
- BMI
- Calorie Expenditure
- Step Count
- Exercise Duration
- Water Intake

### Categorical

- Diet Type
- Stress Level
- Sleep Quality
- Physical Activity Level
- Smoking & Alcohol
- Gender

---

## 🎯 Results

- ✅ Balanced Accuracy: **94.985%**
- ✅ Optimized using **Optuna**
- ✅ Explainable using **SHAP**
- ✅ Interactive Streamlit Web Application
- ✅ Production-ready CatBoost Model

---

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/aditya00801/Student_Lifestyle_and_Stress_Prediction.git
cd Student_Lifestyle_and_Stress_Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📌 Future Improvements

- XGBoost comparison
- Model monitoring
- Docker deployment
- REST API with FastAPI
- Cloud deployment
- CI/CD pipeline

---

## 👨‍💻 Author

**Aditya Kushwaha**

B.Tech Computer Science & Engineering (Artificial Intelligence)

- GitHub: https://github.com/aditya00801
- LinkedIn: *(Add your LinkedIn profile)*

---

## ⭐ Repository

If you found this project useful, consider giving it a **⭐ Star**.