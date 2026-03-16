from fastapi import FastAPI
from app.sentiment import predict  # Import the predict function from the sentiment module
from app.schemas import TextInput, SentimentOutput  # Import input and output schemas

# Create an instance of the FastAPI application
app = FastAPI()

# Define a root endpoint to check if the API is live
@app.get("/")
def root():
    return {"message": "Sentiment API is live"}

# Define a POST endpoint for sentiment prediction
# Accepts input in the form of TextInput schema and returns SentimentOutput schema
@app.post("/predict", response_model=SentimentOutput)
def get_sentiment(input: TextInput):
    return predict(input.text)  # Call the predict function with the input text