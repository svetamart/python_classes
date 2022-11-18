import model
import view

files = model.f

def run():
    running = True
    while running:
        task = view.operation()
        if task == 1:
            create = model.create_directory()
            if create not in files:
                files.append(create)
                answer1 = view.create_success()
                if answer1 == 1:
                    model.add_data(create)
                if answer1 == 3:
                    exit()
            else:
                print('Файл с таким именем уже существует.')
        if task == 2:
            uploaded = model.import_directory()
            if uploaded not in files:
                model.add_file(uploaded)
                message = view.upload()
                if message == 1:
                    model.view_directory(uploaded)
                if message == 3:
                    exit()
            else:
                print('Кажется, что-то пошло не так :( Возможно, файл с таким названием уже существует.')
        if task == 3:
            print(f'Доступные файлы: {files}')
            file = input('Введите имя файла, который хотите просмотреть. Пример: new_phone_book.csv ')
            if file not in files:
                answer2 = int(input(('''Похоже, этого файла нет в списке. Хотите его добавить?
                1 - да
                2 - нет
                Ваш ответ: ''')))
                if answer2 == 1:
                    model.add_file(file)
                    message = view.upload()
                    if message == 1:
                        model.view_directory(file)
                    if message == 3:
                        exit()
            model.view_directory(file)
        if task == 4:
            print(f'Доступные файлы: {files}')
            file = input('Введите имя файла, в который хотите добавить данные. Пример: new_phone_book.csv ')
            if file not in files:
                answer3 = int(input(('''Похоже, этого файла нет в списке. Хотите его добавить?
                1 - да
                2 - нет
                Ваш ответ: ''')))
                if answer3 == 1:
                    model.add_file(file)
                    message = view.upload()
                    if message == 1:
                        model.view_directory(file)
                    if message == 3:
                        exit()
            model.view_directory(file)
            model.add_data(file)
        if task == 5:
            print(f'Доступные файлы: {files}')
            file = input('Введите имя файла, в котором хотите найти данные. Пример: new_phone_book.csv ')
            if file not in files:
                answer4 = int(input(('''Похоже, этого файла нет в списке. Хотите его добавить?
                1 - да
                2 - нет
                Ваш ответ: ''')))
                if answer4 == 1:
                    model.add_file(file)
                    message = view.upload()
                    if message == 1:
                        model.view_directory(file)
                    if message == 3:
                        exit()
            model.find_data(file)
        if task == 6:
            print(files)
        if task == 7:
            print(f'Доступные файлы: {files}')
            file = input('Введите имя файла, из которого хотите удалить данные. Пример: new_phone_book.csv ')
            if file not in files:
                answer5 = int(input(('''Похоже, этого файла нет в списке. Хотите его добавить?
                1 - да
                2 - нет
                Ваш ответ: ''')))
                if answer5 == 1:
                    model.add_file(file)
                    message = view.upload()
                    if message == 1:
                        model.view_directory(file)
                    if message == 3:
                        exit()
            model.view_directory(file)
            model.delete_data(file)
        if task == 8:
            exit()
