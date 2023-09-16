import os
import sys
import pandas as pd
from src.loggers import logging
from src.exceptions import CustomException
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# initializing the Data Ingestion Configuration
@dataclass  #instead using this we can simply create class constructor and do this
class DataIngestionconfig:
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            # df = pd.read_csv(os.path.join('notebooks/data', 'gemstone.csv'))
            df=pd.read_csv(r"notebooks\data\gemstone.csv")
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Train test split")
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error(f'Error occurred in Data Ingestion config: {e}')
            # raise CustomException(e, sys)
