import os, sys
from signlanguage.logger import logging
from signlanguage.exception import SignException

from signlanguage.components.data_ingestion import DataIngestion

from signlanguage.components.data_validation import DataValidation

from signlanguage.components.model_trainer import ModelTrainer

from signlanguage.entity.config_entity import (DataIngestionconfig, DataValidationConfig, ModelTrainerConfig)

from signlanguage.entity.artifacts_entity import (DataIngestionArtifact, DataValidationArtifact, ModelTrainerArtifact)


class TrainingPipeline:
  def __init__(self):
    self.data_ingestion_config = DataIngestionconfig()
    self.data_validation_config = DataValidationConfig()
    self.model_trainer_config = ModelTrainerConfig()
    

  def start_data_ingestion(self) -> DataIngestionArtifact:
    try:
      logging.info('Entered the start data ingestion method of training pipeline class')
      logging.info('Getting the data from url')

      data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)

      data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
      logging.info('Got the data from url')
      logging.info('Exited the start data ingestion method of training pipeline class')
      return data_ingestion_artifact
    except Exception as e:
      raise SignException(e, sys)
    


  def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
    logging.info('Entered start_data_validation method of TrainingPipeline class')
    try:
      data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=self.data_validation_config)

      data_validation_artifact = data_validation.initiate_data_validation()
      logging.info('Performed data validation operation')
      logging.info('Exited start_data_validation method of TrainingPipeline class')
      return data_validation_artifact
    
    except Exception as e:
      raise SignException(e, sys)
    


  def start_model_trainer(self) -> ModelTrainerArtifact:
    try:
      model_trainer = ModelTrainer(model_trainer_config=self.model_trainer_config,)

      model_trainer_artifact = model_trainer.initiate_model_trainer()
      
      return model_trainer_artifact
    
    except Exception as e:
      raise SignException(e, sys)
    
  

    
  def run_pipeline(self):
    try:
      data_ingestion_artifact = self.start_data_ingestion()
      data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)

      if data_validation_artifact.validation_status == True:
        model_trainer_artifact = self.start_model_trainer()
        
      else:
        raise Exception('Data is not in correct format')

    except Exception as e:
      raise SignException(e, sys)
      

