import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import requests

exchange = ccxt.binance()


def alerta(ticker, timefr, limite, indicador):

    bars = exchange.fetch_ohlcv(ticker, timeframe=timefr, limit=limite)
    df = pd.DataFrame(bars, columns=["time", "open", "high", "low", "close", "volume"])

    adx = df.ta.adx()
    macd = df.ta.macd(fast=14, slow=28)
    rsi = df.ta.rsi()

    df = pd.concat([df, adx, macd, rsi], axis=1)

    print(df)

    last_row = df.iloc[-1]

    print(last_row)

    # 1=adx 2=macd 3=rsi
    WEBHOOK_URL = "https://discord.com/api/v9/channels/974635599896137728/messages"

    if indicador == 1:
        if last_row["ADX_14"] >= 25:
            if last_row["DMP_14"] > last_row["DMN_14"]:
                message = f"Fuerte tendencia alcista: El adx está en:  {last_row['ADX_14']:.2f}"
            if last_row["DMN_14"] > last_row["DMP_14"]:
                message = f"Fuerte tendencia bajista: El adx está en: {last_row['ADX_14']:.2f}"

            payload = {"content": message}
            header = {
                "authorization": "OTc0NjM0NzM0OTE3Mzg2Mjgw.GNZMu_.8Z2AbGo-dPmzvDcSerHL06ZI4m6Znd2cDceRI4"
            }

            r = requests.post(
                "https://discord.com/api/v9/channels/974635599896137728/messages",
                data=payload,
                headers=header,
            )

        if last_row["ADX_14"] < 25:
            message = f"NO hay tendencia: El adx está en: {last_row['ADX_14']:.2f}"

            payload = {"content": message}
            header = {
                "authorization": "OTc0NjM0NzM0OTE3Mzg2Mjgw.GNZMu_.8Z2AbGo-dPmzvDcSerHL06ZI4m6Znd2cDceRI4"
            }

            r = requests.post(
                "https://discord.com/api/v9/channels/974635599896137728/messages",
                data=payload,
                headers=header,
            )

    elif indicador == 2:
        if last_row["MACD_14_28_9"] > 0:

            message = f"Fuerte tendencia alcista: El MACD está en:  {last_row['MACD_14_28_9']:.2f}"
        if last_row["MACD_14_28_9"] <= 0:
            message = f"Fuerte tendencia bajista: El MACD está en: {last_row['MACD_14_28_9']:.2f}"

            payload = {"content": message}
            header = {
                "authorization": "OTc0NjM0NzM0OTE3Mzg2Mjgw.GNZMu_.8Z2AbGo-dPmzvDcSerHL06ZI4m6Znd2cDceRI4"
            }

            r = requests.post(
                "https://discord.com/api/v9/channels/974635599896137728/messages",
                data=payload,
                headers=header,
            )

    elif indicador == 3:

        if last_row["RSI_14"] > 60:
            message = (
                f"Fuerte tendencia alcista: El rsi está en:  {last_row['RSI_14']:.2f}"
            )
        elif last_row["DMN_14"] < 20:
            message = (
                f"Fuerte tendencia bajista: El rsi está en: {last_row['RSI_14']:.2f}"
            )

            payload = {"content": message}
            header = {
                "authorization": "OTc0NjM0NzM0OTE3Mzg2Mjgw.GNZMu_.8Z2AbGo-dPmzvDcSerHL06ZI4m6Znd2cDceRI4"
            }

            r = requests.post(
                "https://discord.com/api/v9/channels/974635599896137728/messages",
                data=payload,
                headers=header,
            )


alerta("ETH/USDT", "5m", 100, 2)
