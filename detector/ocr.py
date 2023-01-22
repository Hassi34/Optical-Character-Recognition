from pathlib import Path
import sys
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

import tesserocr
from PIL import Image
import appConfig as CONFIG
import os
from utils import decodeImage

class OCR:

    def get_prediction(base64_str):
        decodeImage(base64_str, CONFIG.IMG_IN)
        img = Image.open(CONFIG.IMG_IN)
        lines = tesserocr.image_to_text(img)  # print ocr text from image
        for line in lines.split("\r"):
           print(line)
        return {"result" : lines}

    def clean_up():
        try:
            imgs = os.listdir(CONFIG.IMAGES_DIR)
            [os.remove(os.path.join(CONFIG.IMAGES_DIR, img)) for img in imgs]
        except Exception as e:
            raise e
            pass