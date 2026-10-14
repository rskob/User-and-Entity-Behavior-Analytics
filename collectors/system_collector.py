import time
from .base_collector import BaseCollector
from .activity_tracker import ActivityTracker
import psutil


class SystemCollector(BaseCollector):
    def __init__(self, activity_tracker: ActivityTracker) -> None:
        super().__init__(activity_tracker)
        self._previous_pids = None
        self._previous_net = None
        self.last_activity = None

    def start(self) -> None:
        self._previous_pids = set(psutil.pids())
        self._previous_net = psutil.net_io_counters()
        psutil.cpu_percent(None)

    def get_data(self) -> dict[str, int | float]:
        idle_time = round(time.time() - self._activity_tracker.get(), 5)
        current_pids = set(psutil.pids())
        current_net = psutil.net_io_counters()

        data = {"new_processes": len(current_pids - self._previous_pids),
                "net_bytes_sent": current_net.bytes_sent - self._previous_net.bytes_sent,
                "net_bytes_received": current_net.bytes_recv - self._previous_net.bytes_recv,
                "cpu_percent": psutil.cpu_percent(None),
                "memory_percent": psutil.virtual_memory().percent,
                "idle_time": idle_time,
                }

        self._previous_pids = current_pids
        self._previous_net = current_net
        return data
