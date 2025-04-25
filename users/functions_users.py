def forming_text_announcement(data: dict) -> str:
    description = data['description']
    list_going = ''
    list_not_going = ''
    if len(data['going']) != 0:
        list_going = f'\n\n<b>Приду🙂 - {len(data["going"])}</b>\n'
        list_going += ', '.join([f'<a href="tg://user?id={key}">{data["going"][key]}</a>' for key in data['going'].keys()])
    if len(data['not_going']) != 0:
        list_not_going = f'\n\n<b>Не смогу🙃 - {len(data["not_going"])}</b>\n'
        list_not_going += ', '.join([f'<a href="tg://user?id={key}">{data["not_going"][key]}</a>' for key in data['not_going'].keys()])
    return description + list_going + list_not_going


def forming_name(first_name: str|None, last_name: str|None) -> str:
    if first_name == None:
        return last_name
    elif last_name == None:
        return first_name
    return f'{first_name} {last_name}'


def cut_text(text: str) -> str:
    if 'Приду🙂' in text:
        return text[0:text.find('Приду🙂')-2]
    if 'Не смогу🙃' in text:
        return text[0:text.find('Не смогу🙃')-2]
    return text