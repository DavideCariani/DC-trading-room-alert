import requests
import yfinance
import pandas_ta as ta
import pandas as pd



security = "FSR"
ticker = yfinance.Ticker(security)
WEBHOOK_URL = "https://discord.com/api/webhooks/928316070509547521/6WLiADJk0hKmLPizHsh-HX2QoRD7wv9rmkZlJkA77UV02f98mG231fGZ70iJXltd4r56"
def send_discord_message(mess):
  payload = {
    "username": "tradingBot",
    "content": mess 
  }
  requests.post(WEBHOOK_URL, json=payload)

th = ticker.history(period="max", interval="5m")

adx = th.ta.adx()
rsi = th.ta.rsi()

df = pd.concat([th, adx, rsi], axis=1)

last_row = df.iloc[-1]

if last_row["ADX_14"] >= 25:
  mess = f"STRONG TREND {security}: ADX IS {last_row['ADX_14']:.2f}" 
  print(mess)
  send_discord_message(mess)
  if last_row["DMP_14"] > last_row['DMN_14']:
    mess = f"STRONG UPTREND {security}: ADX IS {last_row['ADX_14']:.2f}" 
    print(mess)
    send_discord_message(mess)
  if last_row["DMN_14"] > last_row['DMP_14']:
    mess = f"STRONG DOWNTREND for {security}: ADX IS {last_row['ADX_14']:.2f}" 
    print(mess)
    send_discord_message(mess)
     
if last_row["ADX_14"] < 25:
  mess = f"NO TREND for {security}: ADX IS {last_row['ADX_14']:.2f}" 
  print(mess)
  send_discord_message(mess)