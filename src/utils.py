import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.loggers import logging
from src.exceptions import CustomException
from sklearn.metrics import r2_score,mean_squared_error,mean_absolute_error

def save_obects(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)


def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report={}

        for name,model in models.items():
            regressor=model

            regressor.fit(X_train,y_train)

            # Predict testing data
            y_test_pred=regressor.predict(X_test)

            test_model_score=r2_score(y_test,y_test_pred)
            report[name]=test_model_score

        return report
    
    except Exception as e:
        CustomException(e,sys)


def load_objects(file_path):
    try:
        with open(file_path,'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info("Exception Occured in load_object function utils")
        raise CustomException(e,sys)
    
