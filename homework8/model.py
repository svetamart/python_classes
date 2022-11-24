import csv

name = input('''Введите имя файла, с которым хотите работать. Не забудьте указать расширение. Пример: students.csv 
''')

def view(name):
    with open(name, encoding='utf-8') as file:
        reader = csv.reader(file)
        reader = list(reader)
        for i in range(len(reader)):
            array = ' '.join(reader[i]).split(',')
            for i in array:
                print(i)

def add_data(name):
    with open(name, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, lineterminator='\n')
        id = int(student_id(name)) + 1
        data = [id, input('Имя: '), input('Фамилия: '), input('Дата рождения: '), 
            input('Группа: '), input('Факультет: ')]
        writer.writerow(data)
        print(f'Вы добавили {data}')

def student_id(name):
    with open(name, encoding='utf-8') as file:
        reader = csv.reader(file)
        reader = list(reader)
        line = reader[len(reader) - 1]
        id = line[0]
    return id


# сохранили результат во временный файл, основной остался без изменений
def delete_data(name):
    item = input('Введите ID записи, которую хотите удалить: ')
    with open(name, newline='', encoding='utf-8') as source:
        reader = csv.reader(source)
        reader = list(reader)
        tmp = 'export.csv'
        with open(tmp, 'w+', newline='', encoding='utf-8') as destination:
            writer = csv.writer(destination)
            writer.writerow(reader[0])
            writer.writerows(filter(lambda row: item not in row, reader[1:]))
    return tmp


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


# перезапись основного файла 
# вызывается после удаления и изменения информации
def save_changes(name, tmp):
    with open(tmp, newline='', encoding='utf-8') as source:
        reader = csv.reader(source)
        with open(name, 'w+', newline='', encoding='utf-8') as destination:
            writer = csv.writer(destination)
            for i in reader:
                writer.writerow(i)
    return name


def find_data(name):
    item = input('Введите информацию, которую хотите найти: ')
    with open(name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if item in row:
                print(row)


def change_data(name):
    data = input('Введите ID записи, которую хотите изменить: ')
    with open(name, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        reader = list(reader)
        tmp = 'export.csv'
        with open(tmp, 'w+', newline='', encoding='utf-8') as destination:
            writer = csv.writer(destination)
            for row in reader:
                if data in row:
                    print(row)
                    data1 = int(input('''Какую информацию нужно изменить?
                    1 - Имя
                    2 - Фамилия
                    3 - Дата рождения
                    4 - Группа
                    5 - Факультет
                    Ваш ответ: '''))
                    if data1 == 1:
                        row[1] = input('Введите имя: ')
                    elif data1 == 2:
                        row[2] = input('Введите фамилию: ')
                    elif data1 == 3:
                        row[3] = input('Введите дату рождения: ')
                    elif data1 == 4:
                        row[4] = input('Введите номер группы: ')
                    elif data1 == 5:
                        row[5] = input('Введите факультет: ')
                writer.writerow(row)
    return tmp



        

