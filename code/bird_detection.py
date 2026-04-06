import librosa
import pandas as pd
import numpy as np

# 正确路径（从项目根目录运行）
audio_path = "audio/night.wav"

# 加载音频
y, sr = librosa.load(audio_path)

# 每10秒一个片段
frame_length = sr * 10
hop_length = sr * 10

activity = []

# 遍历音频
for i in range(0, len(y), hop_length):
    frame = y[i:i + frame_length]

    if len(frame) == 0:
        continue

    # 计算音量（RMS）
    rms = np.sqrt(np.mean(frame**2))

    # 时间（秒）
    time = i / sr

    activity.append([time, rms])

# 转成DataFrame
df = pd.DataFrame(activity, columns=["time", "activity"])

# 保存CSV
df.to_csv("data/bird_calls.csv", index=False)

print("Audio activity saved")
