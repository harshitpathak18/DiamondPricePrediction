import sys
import os
import pandas as pd
import numpy as np
from src.exceptions import CustomException
from src.loggers import logging
from sklearn.impute import SimpleImputer  #Handling Missing Values
from sklearn.preprocessing import StandardScaler  #Handling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder  #Ordinal Encoding
from src.utils import save_obects
# pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass


@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()

    def get_data_transformation_object(self):
        try:
            logging.info("Data Transformation Initated")

            # Categorical & Numerical Columns
            categorical_cols=['cut', 'color', 'clarity']
            numerical_cols=['carat', 'depth', 'table', 'x', 'y', 'z']

            # Defining Custom ranking (refered from domain expert)
            cut_categories=['Fair','Good','Very Good','Premium','Ideal']
            color_categories=['D','E','F','G','H','I','J']
            clarity_categories=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            logging.info("Data Transformation Pipeline Initiated")
            # Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='median')),
                    ('scaler',StandardScaler())
                ]
            )

            # Categorial Pipeline
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy='most_frequent')),
                    ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                    ('scaler',StandardScaler())
                ]
            )

            preprocessor=ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_cols),
                ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            logging.info('Data Transformation Completed')
            return preprocessor

        except Exception as e:
            logging.info("Exception Occurred Data Transformation")
            raise CustomException(e,sys)


    def initiate_dat_transformation(self,train_data_path,test_data_path):
        try:
            train_df=pd.read_csv(train_data_path)
            test_df=pd.read_csv(test_data_path)

            logging.info('Reading train and test data completed')
            logging.info(f"Training Dataframe Head: \n{train_df.head().to_string()}")
            logging.info(f"Testing Dataframe Head: \n{test_df.head().to_string()}")


            logging.info("Obtaining Preprocessing Object")
            preprocesing_obj=self.get_data_transformation_object()

            target_column='price'
            drop_columns=[target_column,'id']
            
            # dividing data into dependent and independent features
            # Training Data
            input_feature_train_df=train_df.drop(columns=drop_columns,axis=1)
            target_feature_train_df=train_df[target_column]

            # Testing Data
            input_feature_test_df=test_df.drop(columns=drop_columns,axis=1)
            target_feature_test_df=test_df[target_column]

            # Data Transformation
            input_feature_train_arr=preprocesing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocesing_obj.transform(input_feature_test_df)

            # combining input and target feature together
            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]


            save_obects(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocesing_obj)
            

            logging.info("Training and testing data got preprocessed")
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )





        except Exception as e:
            logging.info("Excpetion has occures in Data Transformation")
            raise CustomException(e,sys)

