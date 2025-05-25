# 🧱 Predicting Compressive Strength of Ceramic Waste Concrete using Machine Learning

This project explores the application of machine learning to predict the compressive strength of concrete incorporating **ceramic waste powder** as a partial cement replacement. This initiative contributes to sustainable construction practices by reducing cement usage and reusing industrial ceramic waste.

---

## 📊 Problem Statement

Traditional concrete production has high environmental costs due to cement manufacturing. By replacing a portion of cement with ceramic waste powder, we aim to:

- **Improve sustainability**
- **Maintain structural integrity**
- **Predict compressive strength accurately using ML**

---

## 📁 Dataset Description

The dataset used contains the following features:

| Feature              | Description                             |
|----------------------|-----------------------------------------|
| Cement               | Cement content (kg/m³)                  |
| CeramicWastePowder   | Recycled ceramic waste (kg/m³)          |
| FineAggregate        | Sand content (kg/m³)                    |
| CoarseAggregate      | Gravel content (kg/m³)                  |
| Water                | Water content (kg/m³)                   |
| CompressiveStrength  | Target variable (MPa)                   |

Additional engineered features:

- `WaterCementRatio`, `TotalAggregate`, `CementContent`, `LogCompressiveStrength`

---

## 🧠 ML Pipeline

### 🔧 Preprocessing:
- Feature Engineering
- Log Transformation on Target
- Standardization + Power Transformation (Yeo-Johnson)

### 📈 Models Used:
- Linear Models: `Ridge`, `Lasso`, `ElasticNet`
- Ensemble Models: `Random Forest`, `Gradient Boosting Regressor`

### 📊 Evaluation Metrics:
- RMSE, MAE, R² Score
- Cross-validation scores
- SHAP for model explainability

---

## 📌 Key Results

| Model                     | R² Score | RMSE  | MAE   |
|--------------------------|----------|-------|-------|
| Gradient Boosting        | **0.96** | 1.75  | 1.12  |
| Random Forest            | 0.95     | 1.92  | 1.24  |
| Ridge Regression         | 0.93     | 2.15  | 1.36  |

> 🚀 Best performance achieved with **Gradient Boosting Regressor**

---

## 📉 SHAP Analysis

We used SHAP (SHapley Additive exPlanations) to interpret model predictions and understand feature contributions:

- `Cement`, `CeramicWastePowder`, and `WaterCementRatio` were key drivers of compressive strength.

![SHAP Summary Plot](output/plots/shap_summary.jpg)

---

## 🛠 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- SHAP
- Matplotlib, Seaborn

---

## 🌱 Future Improvements

- Add Deep Learning model (e.g., MLP Regressor)
- Hyperparameter tuning with Optuna
- Web-based prediction interface using Flask/Streamlit

---

## 🙋‍♂️ Author

**[Your Name]**  
B.Tech | Ceramic Engineering | NIT Rourkela  
[GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

