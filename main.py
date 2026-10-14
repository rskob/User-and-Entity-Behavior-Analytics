from model import train
from dataset import collect
from config import *
import sys
from utils import print_logs, show_help, detect
import os


if __name__ == "__main__":
    if len(sys.argv) < 2:
        collect(DATA_PATH, PERIOD_IN_SECONDS, INTERVAL_IN_SECONDS)
        train(DATA_PATH, SCALER_PATH, MODEL_PATH)
        detect()
    else:
        arg = sys.argv[1]
        if arg == "--collect":
            collect(DATA_PATH, PERIOD_IN_SECONDS, INTERVAL_IN_SECONDS)
        elif arg == "--train":
            if not os.path.exists(DATA_PATH) or os.path.getsize(DATA_PATH) == 0:
                print("Сначала нужно собрать обучающие данные")
            else:
                train(DATA_PATH, SCALER_PATH, MODEL_PATH)
        elif arg == "--detect":
            if not os.path.exists(MODEL_PATH):
                print("Сначала нужно обучить модель")
            else:
                detect()
        elif arg == "--show-logs":
            print_logs()
        else:
            show_help()
