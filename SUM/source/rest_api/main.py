from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel


app = FastAPI()


class NumbersRequest(BaseModel):
    number1: float
    number2: float

# Test root


@app.get("/")
def read_root():
    return {"Hello": "World!"}

# Root to calculate the sum between 2 numbers


@app.post("/sum")
def sum(numbers: NumbersRequest):
    result = numbers.number1 + numbers.number2
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
