# Функция должна открывать файл для чтения, сохранять из него словарь, закрыть файл.
# В словарь добавить ещё один словать с шаблоном под ключом равным title.
# Открыть файл для записи (с удалением всего, кажется режим "w"), записать новый вложенный словарь, закрыть файл
import pickle

def save_data(pattern: dict) -> bool:
    if pattern['title'] == None:
        return False
    else:
        # Открытие файла для чтения и сохранение данных
        with open('saved_patern.pickle', 'rb') as file:
            saved_pattern = pickle.load(file)
            print(f'Файл до добавления: {saved_pattern}')
        # Добавления словаря под ключом title
        if 'id' not in pattern.keys():
            pattern['id'] = len(saved_pattern)
            saved_pattern[len(saved_pattern)] = pattern
        else:
            saved_pattern[pattern['id']] = pattern
        print(f'Файл после добавления: {saved_pattern}')
        # Открытие файла для записи и загрузка вложенного словаря
        with open('saved_patern.pickle', 'wb') as file:
            pickle.dump(obj=saved_pattern, file=file)
        return True