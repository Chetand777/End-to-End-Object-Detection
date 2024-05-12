import sys
from signlanguage.configuration.s3_operations import S3operation

from signlanguage.entity.artifacts_entity import ModelPusherArtifact, ModelTrainerArtifact

from signlanguage.entity.config_entity import ModelPusherConfig
from signlanguage.exception import SignException
from signlanguage.logger import logging

class ModelPusher:
  def __init__(self, 
               model_pusher_config: ModelPusherConfig,
               model_trainer_artifact: ModelTrainerArtifact,
               s3: S3operation):
    
    self.model_pusher_config = model_pusher_config
    self.model_trainer_artifact = model_trainer_artifact
    self.s3 = s3


  def initiate_model_pusher(self) -> ModelPusherArtifact:

    logging.info('Entered initiate_model_pusher method of ModelPusher class')

    try:
      self.s3.upload_file(
        self.model_trainer_artifact.trained_model_file_path,
        self.model_pusher_config.S3_MODEL_KEY_PATH,
        bucket_name=self.model_pusher_config.BUCKET_NAME,
        remove=False,
      )

      logging.info(f'Uploaded best model to S3 bucket')
      logging.info('Exited initiate_model_pusher method of ModelPusher class')

      model_pusher_artifact = ModelPusherArtifact(
        bucket_name=self.model_pusher_config.BUCKET_NAME,
        s3_model_path=self.model_pusher_config.S3_MODEL_KEY_PATH
      )

      return model_pusher_artifact
    
    except Exception as e:
      raise SignException(e, sys) from e




