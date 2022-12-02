import view
import model
import logger

name = model.name

def run():
    running = True
    while running:
        task = view.operation()
        if task == 1:
            logger.log(f'{model.view_file.__name__} для просмотра базы данных')
            model.view_file(name)
        elif task == 2:
            logger.log(f'{model.add_data.__name__} для добавления данных')
            model.add_data(name)
        elif task == 3:
            logger.log(f'{model.change_data.__name__} для изменения данных')
            new = model.change_data(name)
            ask = int(input(f'''Сохранить изменения в файле {name}? 
            1 - да
            2 - нет
            Ваш ответ: '''))
            if ask == 1:
                logger.log(f'{model.save_changes.__name__} для сохранения изменений')
                model.save_changes(name, new)
                print('Изменения сохранены')
            else:
                logger.log('None, предыдущие изменения не сохранены')
                print('Изменения не сохранены')
        elif task == 4:
            logger.log(f'{model.find_data.__name__} для поиска данных')
            model.find_data(name)
        elif task == 5:
            logger.log(f'{model.delete_data.__name__} для удаления данных')
            new = model.delete_data(name)
            ask = int(input(f'''Сохранить изменения в файле {name}? 
            1 - да
            2 - нет
            Ваш ответ: '''))
            if ask == 1:
                logger.log(f'{model.save_changes.__name__} для сохранения изменений')
                model.save_changes(name, new)
                print('Изменения сохранены')
                model.change_id(name)
                logger.log(f'{model.change_id.__name__} для обновления списка ID после удаления данных')
            else:
                logger.log('None, предыдущие изменения не сохранены')
                print('Изменения не сохранены')
        else:
            logger.log('None, выход из приложения')
            running = False