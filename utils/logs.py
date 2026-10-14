from config import LOGS_PATH


def print_logs() -> None:
    with open(LOGS_PATH, "r", encoding="utf-8") as file:
        for line in file.readlines():
            print(line)
