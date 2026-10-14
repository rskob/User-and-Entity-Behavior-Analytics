import pandas as pd
import numpy as np
import torch
from sklearn.preprocessing import StandardScaler
import joblib
from config import FIELDS


def load(data_path: str, scaler_path: str):
    df = pd.read_csv(data_path)[FIELDS]
    df[["net_bytes_sent", "net_bytes_received"]] = np.log1p(df[["net_bytes_sent", "net_bytes_received"]]).clip(lower=0)
    scaler = StandardScaler()
    X = torch.FloatTensor(scaler.fit_transform(df))
    joblib.dump(scaler, scaler_path)
    return X
