# Binance Futures Testnet Trading Bot

## Overview
A simple Python CLI-based trading bot that places MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Supports BUY and SELL orders
- MARKET and LIMIT order types
- CLI-based input
- Logging of requests and responses
- Mock fallback mode (if API unavailable)

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 60000

## Assumptions
- Only USDT-M futures supported
- Testnet environment used

## Note
Due to Binance Testnet API access issues (verification restriction),
the project includes a fallback mock mode.

The implementation is fully compatible with Binance Futures API
and can be enabled by providing valid API credentials.
