from transformers import pipeline

# Load the sentiment analysis pipeline from the Hugging Face Transformers library
# This pipeline uses a pre-trained DistilBERT model fine-tuned on SST-2 for sentiment analysis
sentiment_pipeline = pipeline(
    "sentiment-analysis",  # Task type: sentiment analysis
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",  # Pre-trained model
    revision="714eb0f"  # Specific model revision (can be updated to the latest if needed)
)

# Function to predict the sentiment of a given text
def predict(text: str):
    # Use the sentiment pipeline to analyze the input text
    result = sentiment_pipeline(text)[0]
    # Return the sentiment label (e.g., "POSITIVE" or "NEGATIVE") and the confidence score rounded to 4 decimal places
    return {"label": result["label"], "score": round(result["score"], 4)}