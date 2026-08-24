import os
import json
from datetime import datetime

ensure_ascii=False 

LOG_PATH = "LLM-Security-stand-/results/log.json"

def log(prompt, response, mode, blocked):
    data = []
    entry = {
        "prompt" : prompt, 
        "response" : response, 
        "mode" : mode, 
        "blocked" : blocked,
        "timestamp": datetime.now().isoformat()
    }

    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, "r", encoding="utf-8") as f:
           data = json.load(f)

    data.append(entry)

    original_size = os.path.getsize(LOG_PATH) if os.path.exists(LOG_PATH) else 0

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent =4, ensure_ascii = False)

# проверка изменения размера файла
    new_size = os.path.getsize(LOG_PATH)
    if original_size == new_size:
        print("Размер файла не изменился, не успешное добавление логов")
    else:
        print("Файл profile.json успешно изменен")




# надо попробоавть эту штуку 
# Если данные сложные (JSON, бинарные), можно добавить «подпись» — вычислить хеш-сумму или другую метку от записываемых данных и проверить её в файле. Если подписи не совпадают — запись, скорее всего, прошла с ошибкой. 

