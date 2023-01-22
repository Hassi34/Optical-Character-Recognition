import os 
from pathlib import Path

STATIC_DIR = Path("static")

IMAGES_DIR = os.path.join(STATIC_DIR,"images")
os.makedirs(IMAGES_DIR, exist_ok=True)

IMG_IN = os.path.join(IMAGES_DIR, f"in.jpg")


