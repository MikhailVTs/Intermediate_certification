import json


def deleting_note():

    print()
    print("Введите имя заметки, которую хотите удалить!")
    note_del = str(input("Какую заметку Вы хотите удалить: "))

    with open('Заметки.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        minimal = 0

    for txt in data['zametki']:
        if txt['Заголовок'] == note_del:
            data['zametki'].pop(minimal)
        else:
            None
        minimal = minimal + 1

    with open('Заметки.json', 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    print()
    print(f'Заметка {note_del} удалена')
    print()
