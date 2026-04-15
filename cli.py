import argparse

from bot.client import BinanceClient
from bot.orders import OrderService
from bot.validators import validate_order
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Simple Binance Futures Testnet Bot")

    parser.add_argument("--symbol", help="Trading pair e.g. BTCUSDT", required=True)
    parser.add_argument("--side", help="BUY or SELL", required=True)
    parser.add_argument("--type", help="MARKET or LIMIT", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # normalize input
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    qty = args.quantity
    price = args.price

    try:
        validate_order(symbol, side, order_type, qty, price)

        print("\n--- Order Summary ---")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {qty}")
        if price:
            print(f"Price    : {price}")

        client = BinanceClient()
        service = OrderService(client)

        order = service.place_order(symbol, side, order_type, qty, price)

        print("\n✔ Order placed successfully")
        print(f"Order ID     : {order.get('orderId')}")
        print(f"Status       : {order.get('status')}")
        print(f"Executed Qty : {order.get('executedQty')}")
        print(f"Avg Price    : {order.get('avgPrice')}")

    except Exception as e:
        print("\n✖ Something went wrong")
        print(f"Reason: {str(e)}")


if __name__ == "__main__":
    main()