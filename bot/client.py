import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        # If keys are missing → fallback to mock mode
        if not api_key or not api_secret:
            print("⚠ API keys not found. Running in MOCK mode.")
            self.client = None
            return

        try:
            self.client = Client(api_key, api_secret)

            # force Futures Testnet endpoint
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        except Exception as e:
            print("⚠ Failed to initialize Binance client. Switching to MOCK mode.")
            self.client = None