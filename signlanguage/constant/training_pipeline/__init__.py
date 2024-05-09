import os

ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion constant start with DATA_INGESTION var name
"""
DATA_INGESTION_DIR: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_URL: str = "https://github.com/entbappy/Branching-tutorial/raw/master/Sign_language_data.zip"



"""
Data Validation constant start with DATA_VALIDATION var name
"""
DATA_VALIDATION_DIR_NAME: str = 'data_validation'
DATA_VALIDATION_STATUS_FILE = 'status.txt'
DATA_VALIDATION_ALL_REQUIRED_FILES = ['train', 'test', 'data.yaml']



"""
Model Trainer constant start with MODEL TRAINER var name
"""
MODEL_TRAINER_DIR_NAME: str = 'model_trainer'
MODEL_TRAINER_PRETRAINED_WTS_NAME: str = 'yolov5s.pt'
MODEL_TRAINER_NO_EPOCHS: int = 1
MODEL_TRAINER_BATCH_SIZE: int = 16


