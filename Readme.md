# Trading Bot (Binance Futures Testnet)

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Features
- Market & Limit orders
- CLI input validation
- Logging to file
- Error handling

## Assumptions
- Only USDT-M futures supported
- Testnet environment used

## Note
Due to Binance Testnet API access issues (verification restriction),
the project includes a fallback mock mode.

The implementation is fully compatible with Binance Futures API
and can be enabled by providing valid API credentials.