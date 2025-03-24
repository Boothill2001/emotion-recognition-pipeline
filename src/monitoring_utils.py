"""monitoring_utils.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1F4xN7lmztKeTfQkPubNqfCBdpfufP1Ma
"""

import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, UnidentifiedImageError

# ----------------------------
# Monitoring #1: Check ảnh lỗi
# ----------------------------
def is_valid_image(image_path):
    try:
        img = Image.open(image_path).convert("RGB")
        if img.size[0] < 64 or img.size[1] < 64:
            return False, "Too small"
        if np.array(img).std() < 5:
            return False, "Almost blank"
        return True, "OK"
    except UnidentifiedImageError:
        return False, "Unreadable image"

# ----------------------------
# Monitoring #2: Phân phối cảm xúc
# ----------------------------
def plot_label_distribution(df, label_col='dominant_emotion', title='Emotion Distribution'):
    counts = df[label_col].value_counts()
    counts.plot(kind='bar', title=title)
    plt.ylabel("Count")
    plt.xlabel("Emotion")
    plt.show()

def log_label_distribution(df, label_col='dominant_emotion', log_path="label_monitor_log.csv", batch_id=None):
    counts = df[label_col].value_counts().to_dict()
    log_entry = {
        "batch_id": batch_id,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        **counts
    }
    log_df = pd.DataFrame([log_entry])

    if not os.path.exists(log_path):
        log_df.to_csv(log_path, index=False)
    else:
        log_df.to_csv(log_path, mode='a', index=False, header=False)

# ----------------------------
# Monitoring #3: Ghi log accuracy theo thời gian
# ----------------------------
def log_accuracy(model_name, accuracy, log_path="model_monitor_log.json"):
    log_entry = {
        "model": model_name,
        "accuracy": accuracy,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists(log_path):
        try:
            existing = pd.read_json(log_path)
            updated = pd.concat([existing, pd.DataFrame([log_entry])], ignore_index=True)
        except Exception:
            updated = pd.DataFrame([log_entry])
    else:
        updated = pd.DataFrame([log_entry])

    updated.to_json(log_path, indent=4, orient='records')
