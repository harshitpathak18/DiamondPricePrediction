import pandas as pd
import numpy as np
import os
import sys
from src.components.data_ingestion import DataIngestion
from src.loggers import logging
from src.exceptions import CustomException
from src.components.data_transformation import DataTransformation

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_, test_data_ = obj.initiate_data_ingestion()
    print(train_data_)
    print(test_data_)

    data_transformation=DataTransformation()
    train_arr,test_arr,obj_path=data_transformation.initiate_dat_transformation(train_data_,test_data_)






