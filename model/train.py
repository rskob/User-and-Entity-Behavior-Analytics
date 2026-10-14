import torch
import torch.nn as nn
from .model import AutoEncoder
from dataset import load
from config import *
from sklearn.model_selection import train_test_split


def train(data_path: str, scaler_path: str, model_path: str) -> None:
    X = load(data_path, scaler_path)
    X_train, X_test = train_test_split(X, test_size=TEST_SIZE, random_state=30)
    model = AutoEncoder(X_train.shape[1])
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

    for i in range(ITERATIONS):
        output = model(X_train)
        loss = criterion(output, X_train)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        print(f"Epoch {i + 1}/{ITERATIONS} | Loss = {loss.item():.6f}")

    model.eval()
    with torch.no_grad():
        rec = model(X_test)

    errors = (X_test - rec).pow(2)
    mean_feature_errors = {field: errors[:, i].mean().item() for i, field in enumerate(FIELDS)}

    scores = errors.mean(dim=1)
    threshold = torch.quantile(scores, THRESHOLD_PERCENTILE).item()
    torch.save({"model": model.state_dict(), "threshold": threshold, "mean_feature_errors": mean_feature_errors}, model_path)
    print("Training completed.")
