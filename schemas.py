from pydantic import BaseModel

class Prediction(BaseModel):
    base64_str: str


class ShowResults(BaseModel):
    result: str



