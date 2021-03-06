

def people():
    """Вывод имени владельца по номеру документа"""
    num_doc = input('Введите номер документа для поиска владельца \n')
    if base_number(num_doc):
        for record in documents:
            for val in record.values():
                if num_doc in val:
                    print('Владелец документа {} - {}'.format(num_doc, record['name']))
    else:
        question = input("Нет такого номера. Хотите внести новый документ в базу? Y/N")
        if question == 'Y':
            add_to_list(num_doc)
        else:
            print('Спасибо за ваше любопытство')


def out_list():
    """Вывод списка документов в базе"""
    print()
    print('Список документов в базе: ')
    for record in documents:
        print ("Тип док.: {type}   Номер док.: {number}   Владелец док.: {name}".format(**record))


def shelf():
    """Поиск места хранения по номеру документа"""
    num_doc = input('Введите номер документа для поиска места хранения \n')
    if in_archive(num_doc):
        for k, v in directories.items():
            if num_doc in v:
                print('Документ {} на полке {}'.format(num_doc, k))
    else:
        question = input("Нет такого номера. Хотите внести новый документ в базу? Y/N")
        if question == 'Y':
            add_to_list(num_doc)
        else:
            print('Спасибо за ваше любопытство')


def base_number(num_doc):
    """Определение есть ли документ с таким номером в базе"""
    d = set()
    for dictionary in documents:
        d.add(dictionary['number'])
    if num_doc in d:
        return True
    else:
        return False


def in_archive(num_doc):
    """Есть ли у документа место хранения"""
    d = []
    for key in directories.keys():
        d += directories[key]
    if num_doc in d:
        return True
    else:
        return False


def add_to_list(num_doc):
    """Добавляем новый документ"""
    print("Документ с номером {} будет добавлен в список".format(num_doc))
    new_rec = input('Введите тип документа, Имя владельца, Номер полки через запятую \n').split(", ")
    new_doc = {'type': new_rec[0], 'number': num_doc, 'name': new_rec[1]}
    documents.append(new_doc)
    directories[new_rec[2]] = [num_doc]
    print()
    print("Документ с {} засунут на полку {}".format(num_doc, new_rec[2]))
    out_list()


def del_record():
    """Удаление записи по номеру документа"""
    del_rec = input('Введите номер документа, который нужно удалить \n')
    if base_number(del_rec):
        for i in range(len(documents) - 1):
            if documents[i]['number'] == del_rec:
                del documents[i]
    else:
        print('Нет такого намера в базе')
    out_list()


def separator():
    """Распознавание команды"""
    in_put = input('Введите команду p, l, s, d или a \n').lower()
    if in_put == 'p':
        people()
    elif in_put == 'l':
        out_list()
    elif in_put == 's':
        shelf()
    elif in_put == 'a':
        print("Проверим, есть ли документ с таким номером на полках \nЕсли не найдем, то добавим документ в базу")
        shelf()
    elif in_put == 'd':
        del_record()
    else:
        print('Не правильная команда. Запустите еще раз')


documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

separator()





# Удаление с полки
# Добавление полки