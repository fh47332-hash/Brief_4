import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/merged_data.csv")

# 创建一个画布（3个子图）
fig, axs = plt.subplots(3, 1, figsize=(8,10))

# --- 图1：时间序列 ---
axs[0].plot(df["timestamp"], df["brightness"], label="Sky Brightness")
axs[0].plot(df["timestamp"], df["activity"], label="Bird Activity")
axs[0].set_title("Light vs Bird Activity Over Time")
axs[0].legend()
axs[0].tick_params(axis='x', rotation=45)

# --- 图2：Scatter ---
axs[1].scatter(df["brightness"], df["activity"])
axs[1].set_title("Correlation between Light and Bird Activity")
axs[1].set_xlabel("Brightness")
axs[1].set_ylabel("Activity")

# --- 图3：Trend Line ---
z = np.polyfit(df["brightness"], df["activity"], 1)
p = np.poly1d(z)

axs[2].scatter(df["brightness"], df["activity"])
axs[2].plot(df["brightness"], p(df["brightness"]))
axs[2].set_title("Trend Line")
axs[2].set_xlabel("Brightness")
axs[2].set_ylabel("Activity")

plt.tight_layout()
plt.show()
