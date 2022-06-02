import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()


def rqst_graph_ind(ticker, timefr, limite, indicador):
    bars = exchange.fetch_ohlcv(ticker, timeframe=timefr, limit=limite)
    df = pd.DataFrame(bars, columns=["time", "open", "high", "low", "close", "volume"])
    # 1=adx 2=macd 3=rsi

    if indicador == 1:
        indicador1 = df.ta.adx()
        plt.plot(indicador1.values)
        plt.savefig("grafico.png")

    elif indicador == 2:
        indicador2 = df.ta.macd(fast=14, slow=28)
        plt.plot(indicador2.values)
        plt.savefig("grafico.png")

    elif indicador == 3:
        indicador3 = df.ta.rsi()
        plt.plot(indicador3.values)
        plt.savefig("grafico.png")


def rqst_graph(moneda):
    # ahora para que se haga el gráfico desde un archivo externo

    dt = pd.read_csv(moneda)[["unix", "open", "high", "low", "close"]]
    dt.sort_values(by="unix", inplace=True)
    dt["date"] = pd.to_datetime(dt["unix"], unit="s")

    dt.ta.sma(length=100, append=True)

    plt.plot(dt.date, dt.close)
    plt.plot(dt.date, dt.SMA_100)
    plt.savefig("grafico.png")
    plt.close()
