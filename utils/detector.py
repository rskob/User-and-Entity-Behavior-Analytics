from collectors import MainCollector
from config import PERIOD_IN_SECONDS, INTERVAL_IN_SECONDS
from model import Detector


def detect() -> None:
    detector = Detector()
    collector = MainCollector()

    for data in collector.collect(PERIOD_IN_SECONDS, INTERVAL_IN_SECONDS):
        result = detector.predict(data)
        detector.save_info(result, print_console=True)
