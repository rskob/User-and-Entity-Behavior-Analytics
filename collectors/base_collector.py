from .activity_tracker import ActivityTracker


class BaseCollector:
    def __init__(self, activity_tracker: ActivityTracker) -> None:
        self._activity_tracker = activity_tracker

    def get_data(self) -> dict:
        raise NotImplementedError("Данный метод должен быть переопределён в дочернем классе")
