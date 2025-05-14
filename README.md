# Compressive Strength Prediction for Ceramic Waste Concrete

This project focuses on predicting the compressive strength of ceramic waste concrete using machine learning techniques. The dataset used contains various features related to ceramic concrete properties, and the goal is to predict its compressive strength. Multiple regression models have been evaluated, and the best-performing model has been saved for future deployment.

## 🧠 Project Overview

In this project, various regression models are trained and evaluated to predict the compressive strength of ceramic waste concrete. The models considered include:

- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **AdaBoost Regressor**
- **Support Vector Regressor (SVR)**

The project includes comprehensive exploratory data analysis (EDA), feature importance analysis, model evaluation using RMSE, MAE, and R², and model selection based on performance.

## 📊 Key Features

- **Exploratory Data Analysis (EDA)**: Understanding data distributions, correlations, and missing values.
- **Model Evaluation**: Comparison of models based on performance metrics (RMSE, MAE, R²).
- **Visualization**: Includes plots for feature importance and actual vs predicted values.
- **Cross-Validation**: Used for better model assessment.
- **Best Model Selection**: Saved the best-performing model for future deployment.

## ⚙️ Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.x
- Pandas
- NumPy
- Scikit-Learn
- Matplotlib
- Seaborn

You can install the necessary dependencies using `pip`:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn