from catboost import CatBoostRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from pipelines.data_ingestion import load_data
from pipelines.data_preprocessing import preprocess_data
from src.logger.logger import get_logger
from src.exception.exception import CustomException
import joblib
import numpy as np
import os
import sys

logger = get_logger(__name__)

def train_model():
    try:
        logger.info("Starting model training.....")

        # Load and preprocess data
        df = load_data()
        X_train, X_test, y_train, y_test, _, _ = preprocess_data(df)

        # Initialize and train CatBoost
        model = CatBoostRegressor(verbose=0, random_state=42)
        model.fit(X_train, y_train)

        # Predict and evaluate
        y_pred = model.predict(X_test)
        r2 = r2_score(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        logger.info(f"Model Evaluation:")
        logger.info(f"- R² Score: {r2:.4f}")
        logger.info(f"- MAE: {mae:.2f}")
        logger.info(f"- RMSE: {rmse:.2f}")

        # Save model
        os.makedirs("artifacts", exist_ok=True)
        joblib.dump(model, "artifacts/final_model_catboost.pkl")
        logger.info("Model saved to artifacts/final_model_catboost.pkl")

        return model

    except Exception as e:
        logger.error("Model training failed!!!")
        raise CustomException(str(e), sys)
