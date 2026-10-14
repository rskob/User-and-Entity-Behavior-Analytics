from .base_collector import BaseCollector
from .activity_tracker import ActivityTracker
from pynput import mouse


class MouseCollector(BaseCollector):
    def __init__(self, activity_tracker: ActivityTracker) -> None:
        super().__init__(activity_tracker)
        self.clicks = 0
        self.distance = 0.0
        self.last_position = None
        self.scroll_events = 0
        self.scroll_delta = 0
        self.listener = mouse.Listener(on_move=self._on_move, on_click=self._on_click, on_scroll=self._on_scroll)


    def start(self) -> None:
        self.listener.start()

    def _on_move(self, x, y) -> None:
        self._activity_tracker.update()

        if self.last_position:
            dx = x - self.last_position[0]
            dy = y - self.last_position[1]

            self.distance += (dx ** 2 + dy ** 2) ** 0.5

        self.last_position = (x, y)

    def _on_scroll(self, x: int, y: int, dx: int, dy: int) -> None:
        self._activity_tracker.update()
        self.scroll_events += 1
        self.scroll_delta += dy


    def _on_click(self, x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        if pressed:
            self.clicks += 1

    def get_data(self) -> dict:
        data = {"mouse_clicks": self.clicks, "mouse_distance": round(self.distance, 3),
                "scroll_events": self.scroll_events, "scroll_delta": self.scroll_delta}

        self.clicks = 0
        self.distance = 0.0
        self.scroll_events = 0
        self.scroll_delta = 0
        return data
