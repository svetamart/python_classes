from datetime import datetime 

def log(data):
    time = datetime.now()
    with open('log.csv', 'a', encoding='utf-8') as log:
        log.write(f'\n{time}: запущена функция {data}')

