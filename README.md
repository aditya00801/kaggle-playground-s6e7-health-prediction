# 🏥 Student Health Risk Prediction using CatBoost

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![CatBoost](https://img.shields.io/badge/CatBoost-ML-yellow)
![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Optimization-red)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

</p>

---

# 📌 Project Overview

**Student Health Risk Prediction** is a Machine Learning project developed to classify students into different health risk categories based on lifestyle, physical activity, sleep patterns, diet, stress levels, and other health-related attributes.

The project uses **CatBoost Classifier** combined with **advanced feature engineering** and **Optuna hyperparameter optimization** to achieve high predictive performance.

The final model is named:

> **SHRP-CatBoost-Pro**

---

# 🎯 Objectives

- Predict student health conditions accurately.
- Handle imbalanced multi-class classification.
- Improve performance using feature engineering.
- Optimize CatBoost with Optuna.
- Deploy a production-ready prediction model.

---

# 🏆 Final Performance

| Metric | Score |
|---------|-------|
| Algorithm | CatBoost Classifier |
| Hyperparameter Tuning | Optuna |
| Validation | Stratified K-Fold Cross Validation |
| Evaluation Metric | Balanced Accuracy |
| **Best Balanced Accuracy** | **0.94985** |

---

# 🚀 Features

- Advanced Feature Engineering
- CatBoost Classifier
- Optuna Hyperparameter Optimization
- GPU Training Support
- Automatic Class Weight Balancing
- Feature Importance Analysis
- Streamlit Web Application
- Production Ready Model
- Kaggle Submission Ready

---

# 📂 Project Structure

```text
Student-Health-Risk-Prediction/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_CatBoost_Training.ipynb
│   └── 04_Optuna_Optimization.ipynb
│
├── models/
│   ├── shrp_catboost_pro_v1_0.94985.cbm
│   ├── shrp_catboost_pro_best_params.json
│   └── shrp_catboost_pro_feature_importance.csv
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluation.py
│   └── utils.py
│
├── submissions/
│   └── submission_shrp_catboost_pro_0.94985.csv
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The dataset contains student health and lifestyle information.

### Features

- Sleep Duration
- Heart Rate
- BMI
- Calorie Expenditure
- Step Count
- Exercise Duration
- Water Intake
- Diet Type
- Stress Level
- Sleep Quality
- Physical Activity Level
- Smoking & Alcohol
- Gender

---

# 🧠 Feature Engineering

Additional features created to improve prediction performance include:

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

Total Features Used:

**33 Features**

---

# 🤖 Model

## SHRP-CatBoost-Pro

The final model uses:

- CatBoost Classifier
- Multi-Class Classification
- Automatic Class Weight Balancing
- GPU Training
- Early Stopping
- Optuna Optimization

---

# ⚙️ Hyperparameter Optimization

The model was optimized using **Optuna**.

### Optimized Parameters

- Learning Rate
- Depth
- L2 Leaf Regularization
- Random Strength
- Border Count
- Grow Policy
- Leaf Estimation Iterations
- Minimum Data in Leaf
- Bootstrap Type
- Subsample

---

# 📈 Machine Learning Pipeline

```text
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Train/Test Split
      │
      ▼
CatBoost Classifier
      │
      ▼
Optuna Hyperparameter Optimization
      │
      ▼
Stratified K-Fold Validation
      │
      ▼
Final Model
      │
      ▼
Prediction
      │
      ▼
Kaggle Submission
```

---

# 💾 Saved Model

```
models/shrp_catboost_pro_v1_0.94985.cbm
```

---

# 📊 Feature Importance

Feature importance generated using CatBoost helps identify the most influential variables affecting prediction performance.

Output File:

```
models/shrp_catboost_pro_feature_importance.csv
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Student-Health-Risk-Prediction.git

cd Student-Health-Risk-Prediction
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

### Windows

```bash
.venv\Scripts\activate
```

### Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit App

```bash
streamlit run app.py
```

---

# 📈 Results

✅ Balanced Accuracy

**0.94985**

✅ Optimized using Optuna

✅ CatBoost GPU Training

✅ Advanced Feature Engineering

✅ Production Ready

---

# 🔮 Future Improvements

- Ensemble Learning
- Explainable AI (SHAP)
- Real-Time Prediction API
- Docker Deployment
- CI/CD Pipeline
- Cloud Deployment (AWS/Azure/GCP)

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- CatBoost
- Optuna
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

---

# 👨‍💻 Author

**Aditya Kushwaha**

B.Tech CSE (Artificial Intelligence)

Machine Learning | Data Science | Python Developer

GitHub: https://github.com/aditya00801

LinkedIn: *(Add your LinkedIn profile here)*

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!

---

# 📄 License

This project is licensed under the MIT License.