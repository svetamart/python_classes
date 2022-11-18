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
    

def add_data(file):
    answer = 1
    while answer == 1:
        with open(file, 'a', encoding='utf-8') as f: 
            writer = csv.writer(f, lineterminator='\n')
            data = [input('ID: '), input('Имя: '), input('Фамилия: '), input('Дата рождения: '), 
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
            else:
                print('Данные не найдены') # выводит все строчки, а там, где нет нужной инфы, пишет нет данных
                                            # надо, чтобы выводил только с item
                
                

# эта функция не работает :(
def delete_data(name):
    item = input('Введите информацию, которую хотите удалить: ')
    with open(name, 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in writer:
            if item in row:
                item = ''
                print(row)
            print('Данные не найдены')

