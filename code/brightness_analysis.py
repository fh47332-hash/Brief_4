import cv2
import numpy as np
import glob
import pandas as pd
from datetime import datetime, timedelta

image_files = sorted(glob.glob("../timelapse/*.jpg"))

brightness_data = []

start_time = datetime.strptime("22:00", "%H:%M")

for i, img_path in enumerate(image_files):

    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    current_time = start_time + timedelta(minutes=10*i)
    timestamp = current_time.strftime("%H:%M")

    brightness_data.append([timestamp, brightness])

df = pd.DataFrame(brightness_data, columns=["timestamp", "brightness"])

df.to_csv("../data/brightness.csv", index=False)

print("Brightness data saved")
