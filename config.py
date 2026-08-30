import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# TRADING BOT CONFIGURATION (ULTRA-SAFE)
# ==========================================

# True = Demo Trading (No Real Money Used)
# False = Real Trading
PAPER_TRADING = True

# Trade Sizing (Wallet Protection)
MAX_TRADE_AMOUNT = 10  # Maximum $10 USDT per trade

# Strict Risk Management (1:2.3 Risk-to-Reward Ratio)
STOP_LOSS_PERCENT = 1.5      # Strictly 1.5% Stop Loss (Chota Loss)
TAKE_PROFIT_PERCENT = 3.5    # 3.5% Take Profit (Bada Profit)

# Strict Indicator Thresholds
RSI_BUY_THRESHOLD = 35       # Sirf jab market oversold ho tab buy karein
RSI_SELL_THRESHOLD = 68      # Sudden dump se pehle sell karein

# Exchange Setup (Default: KuCoin)
EXCHANGE_NAME = "kucoin"