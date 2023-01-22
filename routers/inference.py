from pathlib import Path
import sys
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1] 
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from fastapi import APIRouter, status, HTTPException
import schemas as SCHEMA
from detector import OCR

router = APIRouter(
    prefix="/predict",
    tags=['Predict']
    )

@router.post('/', response_model=SCHEMA.ShowResults, status_code=status.HTTP_200_OK)
async def prediction(inputParam : SCHEMA.Prediction):
    try:
        result =  OCR.get_prediction(inputParam.base64_str)
        OCR.clean_up()
        return result
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                             detail='Make sure to provide a base64 encoded image in a valide string format')