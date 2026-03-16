import os
import json
import asyncio
import aiohttp
from dotenv import load_dotenv
from alpaca_trade_api.stream import Stream

# Load environment variables from a .env file
load_dotenv()

# Retrieve Alpaca API credentials from environment variables
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

# Alpaca news stream WebSocket URL
NEWS_STREAM = "wss://stream.data.alpaca.markets/v1beta1/news"

# Initialize Alpaca news stream with API credentials
stream = Stream(ALPACA_API_KEY, ALPACA_SECRET_KEY, raw_data=True)

# Callback function to handle incoming news data
async def news_handler(news):
    # Extract headline and creation timestamp from the news data
    headline = news.get('headline')
    created_at = news.get('created_at')    

    # Print the news headline and its sentiment analysis result
    print(f"[{created_at}] {headline}")

# Subscribe to all news events and set the handler function
stream.subscribe_news(news_handler, "*")

# Start the Alpaca news stream and run it indefinitely
asyncio.run(stream._run_forever())