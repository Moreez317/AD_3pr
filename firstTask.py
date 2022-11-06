import pandas as pd

def data_by_year():
    data = pd.read_csv("gold_prices_monthly.csv", sep=',')

    data.rename({"Date": "year"}, axis="columns", inplace=True)

    data["year"] = pd.to_datetime(data.year)
    data = data.groupby(data.year.dt.year).mean()

    return data

def data_by_decade():
    data = pd.read_csv("gold_prices_monthly.csv", sep=',')

    data.rename({"Date": "decade"}, axis="columns", inplace=True)

    data["decade"] = pd.to_datetime(data.decade)
    data = data.groupby((data.decade.dt.year // 10) * 10).mean()

    return data

print(data_by_year())
print(data_by_decade())