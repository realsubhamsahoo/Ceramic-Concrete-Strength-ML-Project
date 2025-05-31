import numpy as np
import pandas as pd
import joblib
from src.logger.logger import get_logger
from src.exception.exception import CustomException
import sys
import os

logger = get_logger(__name__)

class Predictor:
    def __init__(self, model_path="artifacts/final_model_catboost.pkl", scaler_path="artifacts/scaler.pkl"):
        try:
            logger.info("Loading model and scaler....")
            self.model = joblib.load(model_path)
            self.scaler = joblib.load(scaler_path)
            logger.info("Model and scaler loaded successfully.")
        except Exception as e:
            logger.error("Failed to load model or scaler !!")
            raise CustomException(str(e), sys)

    def predict(self, input_data: dict) -> float:
        try:
            logger.info("Starting prediction.....")

            # Convert input to DataFrame
            input_df = pd.DataFrame([input_data])

            # Apply scaling (same features as training)
            scaled_input = self.scaler.transform(input_df)

            # Predict
            prediction = self.model.predict(scaled_input)[0]
            logger.info(f"Prediction complete: {prediction:.2f} MPa")

            return prediction
        except Exception as e:
            logger.error("Prediction failed !!!")
            raise CustomException(str(e), sys)
