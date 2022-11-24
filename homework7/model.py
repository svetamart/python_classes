import csv

f = ['phone_book.csv']


def create_directory():
    data = ['ID', 'Имя', 'Фамилия', 'Дата рождения', 'Место работы', 'Телефон', 'Комментарий']
    name = input("Введите имя файла латинскими буквами и не забудьте указать расширение. Пример: new_phone_book.csv ")
    with open(name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=' ')
        writer.writerow(data)
    with open(name, encoding='utf-8') as f:
        print(f.read())
    return name


def import_directory():
    new_file = input('''Введите имя файла, из которого хотите загрузить справочник. 
    Не забудьте указать расширение. Пример: phone_book.csv 
    ''')
    return new_file


def add_file(name):
    global f
    files = f
    files.append(name)
    return files


def view_directory(file):
    with open(file, encoding='utf-8') as f: 
        reader = csv.reader(f, delimiter=' ')
        for row in reader:
            print(row)


def people_id(file):
    with open(file, encoding='utf-8') as file:
        reader = csv.reader(file)
        reader = list(reader)
        line = reader[len(reader) - 1]
        id = line[0]
    return id


def add_data(file):
    answer = 1
    while answer == 1:
        with open(file, 'a', encoding='utf-8') as f: 
            writer = csv.writer(f, lineterminator='\n')
            id = people_id(file)
            data = [id, input('Имя: '), input('Фамилия: '), input('Дата рождения: '), 
            input('Место работы: '), input('Телефон: '), input('Комментарий: ')]
            writer.writerow(data)
            print(f'Вы добавили {data}')
            another_number = int(input('''Добавить дополнительный номер телефона?
            1 - да
            2 - нет 
            Ваш ответ: '''))
            if another_number == 1:
                count = 0
                how_many = int(input('''Сколько дополнительных номеров Вы хотите добавить? '''))
                while count < how_many:
                    data[5] = input('Телефон: ')
                    data[6] = input('Комментарий: ')
                    writer.writerow(data)
                    print(f'Вы добавили {data}')
                    count += 1
        answer = int(input('''Хотите добавить еще одну запись?
        1 - да
        2 - нет 
        Ваш ответ: '''))
    


def find_data(file):
    item = input('Введите информацию, которую хотите найти: ')
    with open(file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if item in row:
                print(row)
            if item not in reader:
                print('Данные не найдены') # изменила, надо тестить 
                
                

def delete_data(name):
    item = input('Введите ID записи, которую хотите удалить: ')
    with open(name, newline='', encoding='utf-8') as source:
        reader = csv.reader(source)
        reader = list(reader)
        with open(name, 'w', newline='', encoding='utf-8') as destination:
            writer = csv.writer(destination)
            writer.writerow(reader[0])
            writer.writerows(filter(lambda row: item not in row, reader[1:]))
    return name


# должна вызываться после удаления информации, чтобы обновить ID
def change_id(name):
    with open(name, 'r+', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        reader = list(reader)
        with open(name, 'w', newline='', encoding='utf-8') as destination:
            writer = csv.writer(destination)
            writer.writerow(reader[0])
            count = 1
            for line in reader[1:]: 
                for i in range(1):
                    line[0] = count
                    writer.writerow(line)
                count += 1           
    return name