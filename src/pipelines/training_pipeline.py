import pandas as pd
import numpy as np
import os
import sys
from src.components.data_ingestion import DataIngestion
from src.loggers import logging
from src.exceptions import CustomException


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_, test_data_ = obj.initiate_data_ingestion()
    print(train_data_)
    print(test_data_)





