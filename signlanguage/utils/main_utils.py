import os.path
import sys, yaml, base64

from signlanguage.exception import SignException
from signlanguage.logger import logging

def read_yaml_file(filepath: str) -> dict:
  try:
    with open(filepath, 'rb') as yaml_file:
      logging.info('Read yaml file successfully')
      return yaml.safe_load(yaml_file)
    
  except Exception as e:
    raise SignException(e, sys)
  

def write_yaml_file(filepath: str, content: object, replace: bool = False) -> None:
  try:
    if replace:
      if os.path.exists(filepath):
        os.remove(filepath)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    with open(filepath, 'w') as file:
      yaml.dump(content, file)
      logging.info('Write yaml file successfully')

  except Exception as e:
    raise SignException(e, sys)
  

def decodeImage(imgstring, filename):
  imgdata = base64.b64decode(imgstring)
  with open('./data/' + filename, 'wb') as f:
    f.write(imgdata)
    f.close()


def encodeImageintoBase64(croppedImagepath):
  with open(croppedImagepath, "rb") as f:
    return base64.b64encode(f.read())
