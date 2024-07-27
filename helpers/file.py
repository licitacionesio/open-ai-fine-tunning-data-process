import pandas as pd
import json as _json


def read_file(path):
    with open(path, 'r') as file:
        lines = file.readlines()
    elements = [line.strip() for line in lines]
    df = pd.DataFrame(elements, columns=['Message'])
    return df


def write_jsonl_file(data, path):
    with open(path, 'w') as file:
        for item in data:
            json_line = _json.dumps(item, ensure_ascii=False)
            file.write(json_line + '\n')
