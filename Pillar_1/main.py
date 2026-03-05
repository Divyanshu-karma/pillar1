from fastapi import FastAPI
from pydantic import BaseModel
from services.classifier import classify
from services.interpreter import interpret_classification

app = FastAPI()

class ClassifyRequest(BaseModel):
    class_number: int
    identification: str

@app.post("/classify")
def classify_endpoint(req: ClassifyRequest):
    raw = classify(req.class_number, req.identification)
    return interpret_classification(raw)

@app.get("/health")
def health():
    return {"status": "ok"}
