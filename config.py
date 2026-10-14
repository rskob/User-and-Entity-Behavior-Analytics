FIELDS = [
    "mouse_clicks",
    "mouse_distance",
    "keyboard_presses",
    "scroll_events",
    "scroll_delta",
    "new_processes",
    "net_bytes_sent",
    "net_bytes_received",
    "cpu_percent",
    "memory_percent",
    "idle_time",
]

FIELDS_NAMES = {
    "mouse_clicks": "Количество кликов мышью",
    "mouse_distance": "Пройденное расстояние курсора",
    "keyboard_presses": "Количество нажатий клавиш",
    "scroll_events": "Количество прокруток колёсика мышью",
    "scroll_delta": "Общий объем прокрутки колёсика мышью",
    "new_processes": "Количество новых процессов",
    "net_bytes_sent": "Объем исходящего сетевого трафика",
    "net_bytes_received": "Объем входящего сетевого трафика",
    "cpu_percent": "Загрузка процессора",
    "memory_percent": "Использование оперативной памяти",
    "idle_time": "Время бездействия пользователя",
}

EXCLUDED_FIELDS = ["idle_time"]

PERIOD_IN_SECONDS = 10
INTERVAL_IN_SECONDS = 5
ITERATIONS = 3000
LEARNING_RATE = 0.003
TOP_N_FEATURES = 1
TEST_SIZE = 0.2
THRESHOLD_PERCENTILE = 0.95

SCALER_PATH = "model/scaler.pkl"
MODEL_PATH = "model/model.pth"
DATA_PATH = "dataset/data.csv"
LOGS_PATH = "logs/anomalies.log"
