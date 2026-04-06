import pandas as pd

# 读取数据
brightness = pd.read_csv("data/brightness.csv")
birds = pd.read_csv("data/bird_calls.csv")

# 对齐长度
min_len = min(len(brightness), len(birds))
brightness = brightness.iloc[:min_len]
birds = birds.iloc[:min_len]

# 合并
merged = pd.concat([brightness, birds["activity"]], axis=1)

# 保存
merged.to_csv("data/merged_data.csv", index=False)

print("Merged data saved")
