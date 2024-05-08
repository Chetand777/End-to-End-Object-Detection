import os
from dataclasses import dataclass
from datetime import datetime
from signlanguage.constant.training_pipeline import *

TIMESTAMP: str = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

@dataclass
class TrainingPipelineconfig:
  artifacts_dir: str = os.path.join(ARTIFACTS_DIR, TIMESTAMP)

traning_pipeline_config: TrainingPipelineconfig = TrainingPipelineconfig()


@dataclass
class DataIngestionconfig:
  data_ingestion_dir: str = os.path.join(traning_pipeline_config.artifacts_dir, DATA_INGESTION_DIR)

  feature_store_file_path: str = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

  data_download_url: str = DATA_INGESTION_URL
