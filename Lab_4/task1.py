# TODO решите задачу
import json

INPUT_FILE = 'input.json'

def task() -> float:
    with open(INPUT_FILE) as f:
        data = json.load(f)

    list_ = [i["score"] * i["weight"] for i in data]
    return round(sum(list_), 3)


print(task())
