from fastapi import FastAPI
from pydantic import BaseModel

# create fastAPI application
app = FastAPI()

# Define a request body schema using Pydantic
class Message(BaseModel):
    text: str # expect json object with a single string field called text


#  create end point
@app.get("/")
def read_root():
    return {"message":"Hello from realtime-sentiment-model!"}

# handle POST requests to "/echo"
# This endpoint receives a JSON body matching the Message schema
@app.post("/echo")
def echo_message(msg:Message):
    # return text that was sent in the request body
    return{"received": msg.text}