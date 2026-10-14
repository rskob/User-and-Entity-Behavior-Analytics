from pynput import keyboard
from .base_collector import BaseCollector
from .activity_tracker import ActivityTracker


class KeyboardCollector(BaseCollector):
    def __init__(self, activity_tracker: ActivityTracker):
        super().__init__(activity_tracker)
        self.presses = 0
        self.listener = keyboard.Listener(on_press=self._on_press)

    def get_data(self) -> dict:
        data = {"keyboard_presses": self.presses}
        self.__clear()
        return data

    def start(self):
        self.listener.start()

    def _on_press(self, key):
        self._activity_tracker.update()
        self.presses += 1

    def __clear(self):
        self.presses = 0
