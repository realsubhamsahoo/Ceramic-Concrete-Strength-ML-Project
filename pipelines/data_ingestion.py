import pandas as pd
from src.logger.logger import get_logger
from src.exception.exception import CustomException
from src.config.configuration import ConfigurationManager
import sys

logger = get_logger(__name__)

def load_data():
    try:
        config = ConfigurationManager()
        data_path = config.get("data_source")["path"]
        logger.info(f"Loading data from: {data_path}")
        df = pd.read_csv(data_path)
        logger.info(f"Data loaded successfully with shape: {df.shape}")
        return df
    except Exception as e:
        logger.error("Failed to load data")
        raise CustomException(str(e), sys)
