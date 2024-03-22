import requests
import json
import pandas as pd
import os

with open("fred_apikey.txt", "r") as f:
    apikey = f.readline().strip()

for path in ["data", "results"]:
    if not os.path.exists(path):
        os.makedirs(path)

series = "SP500"
start = "2019-01-01"
end = "2024-01-01"
url = (f"https://api.stlouisfed.org/fred/series/observations?"
      f"series_id={series}&api_key={apikey}"
      f"&observation_start={start}&observation_end={end}&file_type=json")

r = requests.get(url)

r.raise_for_status()

json_data = r.json()

with open("data/sp500.json", "w") as f:
    f.write(json.dumps(json_data, indent=4))

df = pd.json_normalize(json_data, 'observations')
df.dtypes

df = df.drop(["realtime_start", "realtime_end"], axis=1)
df = df[df.value != "."]

df["date"] = pd.to_datetime(df["date"])
df["value"] = pd.to_numeric(df["value"])

df.to_csv("data/sp500.csv")

df = df.set_index(["date"])
plt = df.plot(title="S&P 500 (2019-2024)", legend=False)
plt.set_xlabel("Date")
plt.set_ylabel("Index Value")
plt.get_figure().savefig("results/sp500.png")