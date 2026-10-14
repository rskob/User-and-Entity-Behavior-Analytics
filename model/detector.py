import pandas as pd
from config import *
import joblib
from .model import AutoEncoder
import torch
from logs import logger
from datetime import datetime


class Detector:
    def __init__(self) -> None:
        self.scaler = joblib.load(SCALER_PATH)
        self.model = AutoEncoder(len(FIELDS))

        load_data = torch.load(MODEL_PATH)

        self.threshold = load_data["threshold"]
        self.mean_feature_errors = load_data["mean_feature_errors"]
        self.model.load_state_dict(load_data["model"])
        self.model.eval()

    def predict(self, sample: dict) -> dict:
        x = pd.DataFrame([[sample[field] for field in FIELDS]], columns=FIELDS)
        x = self.scaler.transform(x)
        x = torch.FloatTensor(x)

        with torch.no_grad():
            prediction = self.model(x)

        difference = (x - prediction).squeeze()
        difference = dict(zip(FIELDS, difference.tolist()))

        errors = ((x - prediction) ** 2).squeeze()
        score = errors.mean().item()
        errors_dict = dict(zip(FIELDS, errors.tolist()))

        relative_errors = {field: errors_dict[field] / self.mean_feature_errors[field] for field in FIELDS}
        top_feature = [i[0] for i in sorted(relative_errors.items(), key=lambda x: x[1], reverse=True) if i[0] not in EXCLUDED_FIELDS][0]

        return {"is_anomaly": score > self.threshold, "score": score,
                "top_feature": top_feature, "difference": difference}

    @staticmethod
    def save_info(result: dict, print_console: bool = False) -> None:
        top_feature = result["top_feature"]
        if result["is_anomaly"]:
            direction = "выше ожидаемого" if result["difference"][top_feature] > 0 else "ниже ожидаемого"

            msg = f"Наиболее вероятная причина аномалии: {FIELDS_NAMES[top_feature]} ({direction})"
            logger.warning("MSE=%.3f | %s", result["score"], msg)

            if print_console:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | MSE={result['score']:3f} | {msg}")
