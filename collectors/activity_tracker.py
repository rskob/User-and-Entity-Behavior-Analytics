import time


class ActivityTracker:
    def __init__(self) -> None:
        self.__last_activity_time = time.time()

    def update(self) -> None:
        self.__last_activity_time = time.time()

    def get(self) -> float:
        return self.__last_activity_time
