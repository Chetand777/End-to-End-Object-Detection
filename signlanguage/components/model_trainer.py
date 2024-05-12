import os, sys, shutil, zipfile
import yaml
from signlanguage.utils.main_utils import read_yaml_file
from signlanguage.exception import SignException
from signlanguage.logger import logging
from signlanguage.entity.config_entity import ModelTrainerConfig
from signlanguage.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
  def __init__(self, model_trainer_config: ModelTrainerConfig,):
    self.model_trainer_config = model_trainer_config


  def initiate_model_trainer(self,) -> ModelTrainerArtifact:
    logging.info('Entered initiate_model_trainer method of ModelTrainer class')
    try:
      logging.info('Unzipping data')

      with zipfile.ZipFile('Sign_language_data.zip', 'r') as zip_ref:
        zip_ref.extractall()

      os.remove('Sign_language_data.zip')

      with open("data.yaml", 'r') as stream:
        num_classes = str(yaml.safe_load(stream)['nc'])

      model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
      print(model_config_file_name)

      config = read_yaml_file(f'yolov5/models/{model_config_file_name}.yaml')

      config['nc'] = int(num_classes)

      with open(f'yolov5/models/custom_{model_config_file_name}.yaml', 'w') as f:
        yaml.dump(config, f)

      train_command = f'python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ..\\data.yaml --cfg .\\models\\custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results --cache'

      os.chdir('yolov5')
      os.system(train_command)

      os.system('copy yolov5\\runs\\train\\yolov5s_results\\weights\\best.pt yolov5\\')


      os.chdir('..')

      os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

      shutil.copy(src='F:/Projects/End-to-End-Object-Detection/yolov5/runs/train/yolov5s_results/weights/best.pt', dst=f'{self.model_trainer_config.model_trainer_dir}/')

      
      shutil.rmtree('F:/Projects/End-to-End-Object-Detection/yolov5/runs')

      model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path='F:\\Projects\\End-to-End-Object-Detection\\artifacts\\05_10_2024_18_00_00\\model_trainer\\best.pt')

      logging.info('Exited initiate_model_trainer method of ModelTrainer class')
      logging.info(f'Model Trainer Artifact: {model_trainer_artifact}')

      return model_trainer_artifact
    
    except Exception as e:
      raise SignException(e, sys)












