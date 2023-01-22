from pathlib import Path
import sys
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from fastapi import FastAPI
from routers import inference, home

app = FastAPI()

app.include_router(home.router)
app.include_router(inference.router)