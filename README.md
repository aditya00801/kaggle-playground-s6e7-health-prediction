# 🩺 Student Health Risk Prediction
### Kaggle Playground Series – Season 6 Episode 7

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CatBoost](https://img.shields.io/badge/CatBoost-GPU-yellow.svg)
![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Optimization-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📌 Overview

This repository contains my complete solution for the **Kaggle Playground Series – Season 6 Episode 7: Student Health Risk Prediction** competition.

The objective is to predict a student's **health condition** using lifestyle, physical activity, sleep patterns, dietary habits, stress levels, and demographic information.

This project follows a complete end-to-end machine learning workflow, including data preprocessing, feature engineering, hyperparameter optimization, model evaluation, and final Kaggle submission.

---

# 🎯 Problem Statement

Develop a multiclass classification model capable of predicting a student's health status.

### Target Classes

- 🟢 Fit
- 🟡 At-Risk
- 🔴 Unhealthy

---

# 🚀 Project Highlights

- Complete End-to-End ML Pipeline
- Extensive Exploratory Data Analysis
- Advanced Feature Engineering
- GPU Accelerated CatBoost Training
- Hyperparameter Optimization using Optuna
- Stratified Cross Validation
- Class Imbalance Handling
- Modular Python Project Structure
- Multiple Saved Models
- Kaggle Submission Pipeline

---

# 📂 Project Structure

```
student-health-risk/
│
├── data/
│   ├── train.csv
│   ├── test.csv
│   ├── X_processed.csv
│   └── y.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_Baseline_Model.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Cross_Validation.ipynb
│   ├── 06_Hyperparameter_Tuning.ipynb
│   ├── 07_Final_Model.ipynb
│   └── best_catboost_params.csv
│
├── output/
│   ├── models/
│   └── submissions/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── evaluation.py
│   └── utils.py
│
├── .gitignore
└── README.md
```

---

# 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- CatBoost
- Optuna
- Jupyter Notebook

---

# 📊 Dataset Information

The dataset contains information related to student health and lifestyle.

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

# ⚙️ Machine Learning Pipeline

```
Raw Dataset
      │
      ▼
Exploratory Data Analysis
      │
      ▼
Data Cleaning
      │
      ▼
Missing Value Handling
      │
      ▼
Feature Engineering
      │
      ▼
Encoding
      │
      ▼
Cross Validation
      │
      ▼
Optuna Hyperparameter Optimization
      │
      ▼
GPU CatBoost Training
      │
      ▼
Model Evaluation
      │
      ▼
Kaggle Submission
```

---

# 🤖 Final Model

## Algorithm

**CatBoostClassifier**

CatBoost was selected because it provides excellent performance on structured/tabular datasets and efficiently handles categorical features.

The final model was trained using GPU acceleration and optimized with Optuna.

---

# ⚡ Final Model Configuration

| Parameter | Value |
|------------|------:|
| Algorithm | CatBoostClassifier |
| Device | GPU |
| Objective | Multi-Class Classification |
| Hyperparameter Optimization | Optuna |
| Cross Validation | Stratified K-Fold |
| Evaluation Metric | Balanced Accuracy |
| Random Seed | 42 |

---

# 🔧 Best Hyperparameters

| Parameter | Value |
|------------|------:|
| Iterations | **3501** |
| Learning Rate | **0.07298** |
| Depth | **8** |
| Evaluation Metric | **TotalF1** |
| Class Weights | Balanced |

---

# 📈 Model Performance

| Metric | Score |
|---------|------:|
| Validation Accuracy | **89%** |
| Balanced Accuracy | **0.9093** |
| Cross Validation | Stratified K-Fold |
| Optimization | Optuna |

---

# 🧠 Feature Engineering

Several additional features were engineered to improve model performance.

### Engineered Features

- Activity Score
- Hydration Score
- Exercise-to-Sleep Ratio
- Calories per Step
- Water per Exercise
- BMI Category

---

# ⭐ Top Feature Importance

| Rank | Feature |
|------|---------|
| 1 | Sleep Duration |
| 2 | Stress Level |
| 3 | BMI |
| 4 | Physical Activity Level |
| 5 | Smoking & Alcohol |
| 6 | Heart Rate |
| 7 | Activity Score |
| 8 | Water Intake |
| 9 | Calorie Expenditure |
| 10 | Sleep Quality |

---

# 💾 Saved Models

The repository includes multiple trained models.

```
output/models/

catboost_final.pkl
catboost_tuned.pkl
catboost_optuna_best.cbm
catboost_optuna_3501iter_v1.cbm
catboost_fold_5.cbm
```

---

# 📄 Generated Outputs

The project generates:

- Trained CatBoost Models
- Best Hyperparameters
- Cross Validation Results
- Submission Files
- Evaluation Reports

---

# 📦 Installation

Clone the repository.

```bash
git clone https://github.com/aditya00801/kaggle-playground-s6e7-health-prediction.git
```

Move into the project directory.

```bash
cd kaggle-playground-s6e7-health-prediction
```

Install the required packages.

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Launch Jupyter Notebook.

```bash
jupyter notebook
```

Run the notebooks in the following order:

1. 01_eda.ipynb
2. 02_preprocessing.ipynb
3. 03_Baseline_Model.ipynb
4. 04_Feature_Engineering.ipynb
5. 05_Cross_Validation.ipynb
6. 06_Hyperparameter_Tuning.ipynb
7. 07_Final_Model.ipynb

---

# 📚 Competition

**Kaggle Playground Series – Season 6 Episode 7**

Student Health Risk Prediction

---

# 📌 Future Improvements

- Ensemble Learning
- Explainable AI using SHAP
- Automated Feature Selection
- Model Deployment with Streamlit/FastAPI
- CI/CD Pipeline
- Docker Support

---

# 👨‍💻 Author

**Aditya Kushwaha**

B.Tech CSE (Artificial Intelligence)

GitHub:
https://github.com/aditya00801

Email:
adityakushwaha0007@gmail.com

---

# ⭐ Support

If you found this project helpful:

⭐ Star the repository

🍴 Fork the repository

📢 Share your feedback

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- Kaggle
- CatBoost
- Optuna
- Scikit-Learn
- Open Source Community

---

**Thank you for visiting this repository!**
```