# Real-Time Financial News Sentiment Pipeline

A real-time sentiment analysis pipeline for financial news using DistilBERT and FastAPI. Processes live news streams from Alpaca Markets and provides REST API endpoints for sentiment predictions.

## Features

- **Real-Time News Streaming**: WebSocket connection to Alpaca Markets news feed
- **Sentiment Analysis**: DistilBERT-based sentiment classification (POSITIVE/NEGATIVE)
- **REST API**: FastAPI endpoints for on-demand predictions
- **Production-Ready**: Uvicorn ASGI server with async support

## Project Structure

```
Real-Time-Financial-News-Sentiment-Pipeline/
├── app/                          # FastAPI REST API Server
│   ├── main.py                   # FastAPI app with /predict endpoint
│   ├── sentiment.py              # DistilBERT inference engine
│   └── schemas.py                # Pydantic I/O schemas
├── stream/                       # Real-time data ingestion
│   └── news.py                   # Alpaca WebSocket news listener
├── basics/                       # Utilities & examples
├── main.py                       # CLI entry point
└── pyproject.toml               # Project configuration
```

## Model Deployment Architecture

```
┌─────────────────────────────────────────┐
│      Alpaca Markets News Feed           │
│      (WebSocket Real-Time Stream)       │
└────────────────────┬────────────────────┘
                     │
         ┌───────────▼──────────┐
         │  stream/news.py      │
         │  (News Ingestion)    │
         └───────────┬──────────┘
                     │
      ┌──────────────┴──────────────┐
      │                             │
      ▼                             ▼
┌─────────────────┐        ┌───────────────────┐
│  Real-time      │        │  REST API         │
│  Processing     │        │  (FastAPI)        │
└─────────────────┘        │  /predict         │
                           │  (app/main.py)    │
                           └─────────┬─────────┘
                                     │
                        ┌────────────▼────────────┐
                        │  DistilBERT Model      │
                        │  (app/sentiment.py)    │
                        │  Sentiment Analysis    │
                        └────────────────────────┘
```

## Installation

```bash
# Install dependencies
pip install -r requirements.txt
# or using uv:
uv sync
```

## Quick Start

### Start the API Server

```bash
uvicorn app.main:app --reload
```

API will be available at `http://localhost:8000`

### Test Prediction

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "Apple stock surged 5% on strong earnings"}'
```

Response:
```json
{
  "label": "POSITIVE",
  "score": 0.9987
}
```

### Stream Real-Time News

```bash
# Requires ALPACA_API_KEY and ALPACA_SECRET_KEY environment variables
python stream/news.py
```

## Requirements

- Python 3.11+
- PyTorch 2.6.0
- Transformers 4.51.2
- FastAPI 0.115+
- Alpaca Trade API (for live news streaming)

## Environment Variables

```
ALPACA_API_KEY=your_api_key
ALPACA_SECRET_KEY=your_secret_key
```

## References

- [DistilBERT Model](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english)
- [Alpaca Markets API](https://alpaca.markets/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
