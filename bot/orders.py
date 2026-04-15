import logging
import random


class OrderService:
    def __init__(self, client):
        self.client = client.client

    def place_order(self, symbol, side, order_type, quantity, price=None):
        # 🔹 MOCK MODE (if API not available)
        if self.client is None:
            logging.warning("MOCK MODE: Order simulated")

            mock_response = {
                "orderId": random.randint(100000, 999999),
                "status": "FILLED",
                "executedQty": quantity,
                "avgPrice": price if price else "market"
            }

            logging.info(f"Mock Response -> {mock_response}")
            return mock_response

        # 🔹 REAL API MODE
        try:
            logging.info(
                f"Request -> {symbol} | {side} | {order_type} | qty={quantity} | price={price}"
            )

            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("LIMIT order requires price")

                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Invalid order type")

            logging.info(f"Response -> {order}")
            return order

        except Exception as e:
            logging.error(f"Order failed: {str(e)}")

            # fallback to mock if API fails mid-way
            print("⚠ API failed, switching to MOCK response")

            return {
                "orderId": random.randint(100000, 999999),
                "status": "FAILED (mock fallback)",
                "executedQty": 0,
                "avgPrice": None
            }