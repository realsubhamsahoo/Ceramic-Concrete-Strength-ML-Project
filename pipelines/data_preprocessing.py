import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from src.logger.logger import get_logger
from src.exception.exception import CustomException
import sys
import joblib

logger = get_logger(__name__)

def preprocess_data(df: pd.DataFrame):
    try:
        logger.info("Starting data preprocessing.....")

        # Drop Serial No if present
        if "Serial No" in df.columns:
            df = df.drop("Serial No", axis=1)
            logger.info("Dropped column: Serial No")

        # Separate features and target
        X = df.drop("CS", axis=1)
        y = df["CS"]

        # Train-test split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        logger.info(f"Data split: {X_train.shape}, {X_test.shape}")

        # Feature scaling
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)

        # Save scaler
        joblib.dump(scaler, "artifacts/scaler.pkl")
        logger.info("Scaling complete and saved to artifacts/")

        return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled

    except Exception as e:
        logger.error("Preprocessing failed")
        raise CustomException(str(e), sys)
