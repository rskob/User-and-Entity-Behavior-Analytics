from .mouse import MouseCollector
from .keyboard import KeyboardCollector
from .system_collector import SystemCollector
import time
from .activity_tracker import ActivityTracker


class MainCollector:
    def __init__(self) -> None:
        activity_tracker = ActivityTracker()
        self.collectors = [MouseCollector(activity_tracker), KeyboardCollector(activity_tracker),
                           SystemCollector(activity_tracker)]

    def collect(self, period_in_seconds: int, interval_in_seconds: int) -> dict:
        for collector in self.collectors:
            collector.start()

        end_time = time.time() + period_in_seconds
        while time.time() < end_time:
            time.sleep(interval_in_seconds)
            data = {}
            for collector in self.collectors:
                data.update(collector.get_data())

            yield data
