import pandas as pd

df = pd.read_csv("../data/mw_state_annual.csv")

df = df[df["Year"] == 2019]

df = df.sort_values("Name")

df = df[["Name", "Annual State Minimum"]]

df.rename(columns={"Name": "state", "Annual State Minimum":"minimum_wage"}, inplace=True)

df.to_csv("../data/minimum_wage.csv", index=False)
