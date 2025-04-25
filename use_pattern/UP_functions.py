# Функция открывает файл для чтения и загружает данные
import pickle


def load_data() -> dict:
    with open(file='saved_patern.pickle', mode='rb') as file:
        saved_pattern = pickle.load(file)
    return saved_pattern


def delete_data(pattern_id: int) -> None:
    saved_pattern = load_data()
    saved_pattern.pop(pattern_id)
    with open('saved_patern.pickle', 'wb') as file:
            pickle.dump(obj=saved_pattern, file=file)
    return