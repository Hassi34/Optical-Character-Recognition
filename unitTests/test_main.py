import sys , os
from pathlib import Path
FILE = Path(__file__).resolve()
ROOT = FILE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))


IMG_PATH = Path(os.path.join(ROOT, "unitTests", "test_img.jpg")).resolve()

from main import app
from fastapi.testclient import TestClient
from utils import encodeImageIntoBase64


client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert type(response.content) == bytes
    assert type(response.json()) == dict
    assert list(response.json().keys()) == ["message"]
    assert [type(i) for i in response.json().values()] == [str]
    assert response.json() == {"message": '''Hi there, app is up and running...Prediction services are available at http://<HOST>/predict OR Try to visit http://<HOST>/docs for API documentation'''}

def test_predict():
    response = client.post("/predict", json={"base64_str": encodeImageIntoBase64(IMG_PATH)})
    assert response.status_code == 200
    assert type(response.content) == bytes
    assert type(response.json()) == dict
    assert list(response.json().keys()) == ["result"]
    assert [type(i) for i in response.json().values()] == [str]