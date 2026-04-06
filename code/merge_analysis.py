import pandas as pd

brightness = pd.read_csv("../data/brightness.csv")
birds = pd.read_csv("../data/bird_calls.csv")

merged = pd.merge(brightness, birds, on="timestamp")

merged.to_csv("../data/merged_data.csv", index=False)

print(merged)
