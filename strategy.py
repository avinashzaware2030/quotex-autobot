import pandas as pd
import talib

def calculate_indicators(df):
    df['EMA20'] = talib.EMA(df['Close'], timeperiod=20)
    df['EMA50'] = talib.EMA(df['Close'], timeperiod=50)
    df['MACD'], df['MACD_signal'], _ = talib.MACD(df['Close'])
    df['RSI'] = talib.RSI(df['Close'], timeperiod=14)
    return df

def generate_signal(df):
    last = df.iloc[-1]

    if last['MACD'] > last['MACD_signal'] and last['RSI'] < 30 and last['EMA20'] > last['EMA50']:
        return "BUY"
    elif last['MACD'] < last['MACD_signal'] and last['RSI'] > 70 and last['EMA20'] < last['EMA50']:
        return "SELL"
    else:
        return "WAIT"
