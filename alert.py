import ccxt, yfinance
import pandas_ta as ta
import pandas as pd

exchange = ccxt.binance()


def alerta(ticker, timefr, limite, indicador):

    bars = exchange.fetch_ohlcv(ticker, timeframe=timefr, limit=limite)
    df = pd.DataFrame(bars, columns=["time", "open", "high", "low", "close", "volume"])

    adx = df.ta.adx()
    macd = df.ta.macd(fast=14, slow=28)
    rsi = df.ta.rsi()

    df = pd.concat([df, adx, macd, rsi], axis=1)

    last_row = df.iloc[-1]


    if indicador == 1:
        if last_row["ADX_14"] >= 25:
            if last_row["DMP_14"] > last_row["DMN_14"]:
                message = f"Fuerte tendencia alcista: El adx está en:  {last_row['ADX_14']:.2f}"
                return message
            if last_row["DMN_14"] > last_row["DMP_14"]:
                message = f"Fuerte tendencia bajista: El adx está en: {last_row['ADX_14']:.2f}"
                return message

        if last_row["ADX_14"] < 25:
            message = f"NO hay tendencia: El adx está en: {last_row['ADX_14']:.2f}"
            return message

    elif indicador == 2:
        if last_row["MACD_14_28_9"] > 0:

            message = f"Fuerte tendencia alcista: El MACD está en:  {last_row['MACD_14_28_9']:.2f}"
            return message
        if last_row["MACD_14_28_9"] <= 0:
            message = f"Fuerte tendencia bajista: El MACD está en: {last_row['MACD_14_28_9']:.2f}"
            return message

    elif indicador == 3:

        if last_row["RSI_14"] > 60:
            message = (
                f"Fuerte tendencia alcista: El rsi está en:  {last_row['RSI_14']:.2f}"
            )
            return message
        elif last_row["RSI_14"] < 20:
            message = (
                f"Fuerte tendencia bajista: El rsi está en: {last_row['RSI_14']:.2f}"
            )
            return message
        else:
            message = f"NO hay tendencia: El rsi está en: {last_row['RSI_14']:.2f}"
            return message


# alerta("ETH/USDT", "5m", 100, 2)
