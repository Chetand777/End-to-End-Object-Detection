import os, sys
from signlanguage.logger import logging
from signlanguage.exception import SignException
from signlanguage.components.data_ingestion import DataIngestion
from signlanguage.entity.config_entity import (DataIngestionconfig)
from signlanguage.entity.artifacts_entity import (DataIngestionArtifact)


class TrainingPipeline:
  def __init__(self):
    self.data_ingestion_config = DataIngestionconfig()

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
    

  def run_pipeline(self):
    try:
      data_ingestion_artifact = self.start_data_ingestion()

    except Exception as e:
      raise SignException(e, sys)
      

