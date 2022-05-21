import ccxt, yfinance
import pandas_ta as ta
import pandas as pd
import matplotlib.pyplot as plt

exchange = ccxt.binance()
bars = exchange.fetch_ohlcv('ETH/USDT', timeframe='1h', limit=100)
df = pd.DataFrame(bars, columns=['time', 'open', 'high', 'low', 'close', 'volume'])


adx = df.ta.adx()
macd = df.ta.macd(fast=14, slow=28)


rsi = df.ta.rsi()
df = pd.concat([df, adx, macd, rsi], axis=1)
df = df[df['RSI_14'] < 30]
df.ta.sma(length = 100, append = True)


suma = 0
#ahora cada vez que llamen hay que subirle un numerito

plt.plot(rsi.values)
plt.savefig('grafico.png')
plt.show()
print(df)

#ahora para que se haga el gráfico desde un archivo externo

dt = pd.read_csv("btc.csv")[["unix","open", "high","low", "close"]]
dt.sort_values(by="unix", inplace=True)
dt["date"] = pd.to_datetime(dt["unix"], unit = 's')

dt.ta.sma(length = 100, append = True)

plt.plot(dt.date, dt.close)
plt.plot(dt.date, dt.SMA_100)
plt.show()