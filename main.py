
import pandas as pd
from helpers import file as _file, cost as _cost


def _convert_to_open_ai(prompt, data):
    result = []
    for index, row in data.iterrows():
        if index == 0: continue
        r = {
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": row['Message']},
                {"role": "assistant", "content": str(row['score'])}
            ]
        }
        result.append(r)
    return result


def _pre_process_data(good_data, bad_data):
    df_concat = pd.concat([good_data, bad_data])
    df_mix = df_concat.sample(frac=1).reset_index(drop=True)
    return df_mix


def _get_train_and_test_data(data, limit: int = None, test_percent: float = None):
    if limit is not None:
        data = data.head(limit)

    train_data = data if test_percent is None else data.sample(frac=1.0 - test_percent)
    test_data = None if test_percent is None else data.sample(frac=test_percent)
    return train_data, test_data


def run():
    good_data = _file.read_file(path='data/is_not_spam.txt')
    good_data['score'] = 0

    bad_data = _file.read_file(path='data/is_spam.txt')
    bad_data['score'] = 1

    df_mix = _pre_process_data(good_data=good_data, bad_data=bad_data)
    train_data, test_data = _get_train_and_test_data(data=df_mix, limit=2000, test_percent=0.10)

    prompt = "Determina si el mensaje introducido es Spam."
    train_data_open_ai = _convert_to_open_ai(prompt=prompt, data=train_data)
    test_data_open_ai = _convert_to_open_ai(prompt=prompt, data=test_data)

    _file.write_jsonl_file(data=train_data_open_ai, path="data/train_data.jsonl")
    _file.write_jsonl_file(data=test_data_open_ai, path="data/test_data.jsonl")

    _cost.calculate_cost(training_file_path="data/train_data.jsonl")


if __name__ == '__main__':
    run()
