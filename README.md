# 🩺 Student Health Risk Prediction
### Kaggle Playground Series – Season 6 Episode 7

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![CatBoost](https://img.shields.io/badge/CatBoost-GPU-yellow.svg)
![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Optimization-red.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

# 📖 Overview

This repository contains my complete solution for the **Kaggle Playground Series – Season 6 Episode 7: Student Health Risk Prediction** competition.

The goal is to predict a student's **health condition** based on their lifestyle, sleep habits, physical activity, stress level, dietary information, and other health-related attributes.

The project demonstrates a complete machine learning workflow from data preprocessing to model optimization and final Kaggle submission.

---

# 🎯 Problem Statement

Develop a multiclass classification model capable of predicting a student's health status into one of the following categories:

- 🟢 Fit
- 🟡 At-Risk
- 🔴 Unhealthy

---

# 🚀 Project Highlights

- End-to-End Machine Learning Pipeline
- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Feature Engineering
- Stratified Cross Validation
- Optuna Hyperparameter Optimization
- GPU Accelerated CatBoost Training
- Automatic Class Weight Balancing
- Model Evaluation
- Kaggle Submission Generation

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
- Scikit-Learn
- CatBoost
- Optuna
- Matplotlib
- Jupyter Notebook

---

# 📊 Dataset Features

The model is trained using health and lifestyle-related features including:

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

Additional engineered features:

- Activity Score
- Hydration Score
- Exercise-to-Sleep Ratio
- Calories per Step
- Water per Exercise
- BMI Category

---

# 🤖 Final Model

The final solution uses a **GPU-accelerated CatBoostClassifier** optimized with **Optuna** for multiclass classification.

### Model Configuration

| Parameter | Value |
|-----------|-------|
| Algorithm | CatBoostClassifier |
| Objective | MultiClass |
| Task Type | GPU |
| Evaluation Metric | TotalF1 |
| Hyperparameter Optimization | Optuna |
| Cross Validation | Stratified K-Fold |
| Random Seed | 42 |
| Iterations | **3501** |
| Learning Rate | **0.0729819760** |
| Depth | **8** |
| L2 Leaf Regularization | **2.6131** |
| Random Strength | **1.9111** |
| Border Count | **244** |
| Bagging Temperature | **0.5504** |

---

# ⚖️ Class Weights

To address class imbalance, balanced class weights were automatically computed.

| Class | Weight |
|-------|-------:|
| At-Risk | **0.3882** |
| Fit | **5.7792** |
| Unhealthy | **3.9850** |

---

# 📈 Training Summary

| Metric | Value |
|---------|------:|
| Initial TotalF1 | 0.8041 |
| Final Training TotalF1 | **0.9786** |
| Training Iterations | **3501** |
| Training Device | GPU |
| Optimization | Optuna |

---

# ⭐ Feature Importance

Top contributing features:

1. Sleep Duration
2. Stress Level
3. BMI
4. Physical Activity Level
5. Smoking & Alcohol
6. Heart Rate
7. Activity Score
8. Water Intake
9. Calorie Expenditure
10. Sleep Quality

---

# 🏆 Machine Learning Pipeline

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

# 💾 Saved Models

```
output/models/

catboost_optuna_3501iter_v1.cbm
catboost_optuna_best.cbm
catboost_final.pkl
catboost_tuned.pkl
catboost_fold_5.cbm
```

---

# 📄 Outputs

The project generates:

- Trained CatBoost Models
- Optimized Hyperparameters
- Evaluation Results
- Kaggle Submission Files

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/aditya00801/kaggle-playground-s6e7-health-prediction.git
```

Navigate to the project directory:

```bash
cd kaggle-playground-s6e7-health-prediction
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Run the notebooks in this order:

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

# 🔮 Future Improvements

- SHAP Explainability
- Ensemble Models
- Automated Feature Selection
- Streamlit Deployment
- Docker Containerization
- CI/CD Integration

---

# 👨‍💻 Author

**Aditya Kushwaha**

**B.Tech – Computer Science & Engineering (Artificial Intelligence)**

📧 Email: adityakushwaha0007@gmail.com

🐙 GitHub: https://github.com/aditya00801

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork this repository

📝 Share your feedback

---

# 📜 License

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