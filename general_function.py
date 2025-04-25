from datetime import datetime, timedelta

def convert_date(text: str) -> datetime:
    text = text.strip()
    for char in {'/', ',', ' ', '-'}:
        if char in text:
            text = text.replace(char, '.')
    try:
        datetime.strptime(text, '%d.%m')
    except ValueError:
        return 'Неверный формат даты'
    else:
        text += datetime.strftime(datetime.today(), '.%Y')
        return datetime.strptime(text, '%d.%m.%Y')
