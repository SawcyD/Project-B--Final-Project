import pandas as pd

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/" \
      "csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv"
us = pd.read_csv(url)
md = us[us["Province_State"] == "Maryland"]
date_cols = md.columns[md.columns.str.match(r"\d{1,2}/\d{1,2}/\d{2}$")]
cum = md[date_cols].sum(axis=0)
cum.index = pd.to_datetime(cum.index, format="%m/%d/%y")

daily = cum.diff().clip(lower=0)
weekly = daily.resample("W").sum()

df = pd.DataFrame({"cases": weekly})
df.to_csv("data/maryland_weekly_cases.csv")

