from pathlib import Path
import sys
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from fastapi import APIRouter, status

router = APIRouter(
    tags=['Home']
    )

@router.get('/', status_code=status.HTTP_200_OK)
def home():
    return {"message": '''Hi there, app is up and running...Prediction services are available at http://<HOST>/predict OR Try to visit http://<HOST>/docs for API documentation'''}
