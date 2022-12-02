import telebot
import poly_bot_func

token = '5890280310:AAEu3PpsD3r-HR4zkaA9mTTAmfVSMA9Fiqw'
bot = telebot.TeleBot(token)

poly1 = poly_bot_func.poly1
poly2 = poly_bot_func.poly2

dict1 = poly_bot_func.dict1
dict2 = poly_bot_func.dict2

messages = {'calc': 'Введи первый полином. \n'
                    'Знаки возведения в степень ставить не нужно. '
                    'Знак умножения между коэффициентом и переменной тоже не нужен.\n'
                    'Пример: -7x5 + 22x4 - 4x3 + 28x2 - 3x - 2 = 0',
            'second_poly': 'Введи второй полином. \n'
                           'Знаки возведения в степень ставить не нужно. '
                           'Знак умножения между коэффициентом и переменной тоже не нужен.\n'
                           'Пример: -7x5 + 22x4 - 4x3 + 28x2 - 3x - 2 = 0',
            'help': 'Набери /calc, чтобы начать работу \n'
                    'Или жми /help, чтобы посмотреть справку. \n'
                    'Полиномы нужно вводить без знаков возведения в степень '
                    'и без знаков умножения между коэффициентом и переменной. \n'
                    'И не забывай разделять одночлены и математические '
                    'символы "+" и "=" пробелами. \n'
                    'Пример: 6x8 + x7 + 8x6 - 12x5 + 2x4 - 3x2 + x = 0'}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'''Привет, {message.from_user.first_name}! \n
Меня зовут Поли-Бот, и я умею складывать полиномы! \n
Как это работает? Все просто! Отправляешь мне команду /calc и следуешь инструкциям. 
Тебе нужно будет ввести полиномы, которые ты хочешь сложить, а все остальное я сделаю сам! \n
Набери /calc, чтобы начать работу \n 
Или жми /help, чтобы посмотреть справку.''')


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, messages['help'])


@bot.message_handler(commands=['calc'])
def first_polynomial(message):
    msg = bot.send_message(message.chat.id, messages['calc'])
    bot.register_next_step_handler(msg, second_polynomial)


def second_polynomial(message):
    global poly1, dict1
    poly1 = str(message.text)
    try:
        dict1 = poly_bot_func.create_dict(poly1)
        msg = bot.send_message(message.chat.id, messages['second_poly'])
        bot.register_next_step_handler(msg, result)
    except:
        msg = bot.send_message(message.chat.id, 'Кажется, что-то пошло не так. \n'
                                                'Скорее всего, полином введен неверно. Попробуй еще раз!')
        bot.send_message(message.chat.id, 'Полиномы нужно вводить без знаков возведения в степень '
                                          'и без знаков умножения между коэффициентом и переменной. \n'
                                          'И не забывай разделять одночлены и математические '
                                          'символы "+" и "=" пробелами. \n'
                                          'Пример: 6x8 + x7 + 8x6 - 12x5 + 2x4 - 3x2 + x = 0')
        bot.register_next_step_handler(msg, second_polynomial)


def result(message):
    global dict1, dict2, poly2, poly1
    poly2 = str(message.text)
    try:
        dict2 = poly_bot_func.create_dict(poly2)
        third = poly_bot_func.poly_sum(dict1, dict2)
        bot.send_message(message.chat.id, f'Вот, что у нас получилось: {poly_bot_func.result_poly(third)}')
    except:
        msg = bot.send_message(message.chat.id, 'Кажется, что-то пошло не так. \n'
                                                'Скорее всего, полином введен неверно. Попробуй еще раз!')
        bot.send_message(message.chat.id, 'Полиномы нужно вводить без знаков возведения в степень '
                                          'и без знаков умножения между коэффициентом и переменной. \n'
                                          'И не забывай разделять одночлены и математические '
                                          'символы "+" и "=" пробелами. \n'
                                          'Пример: 6x8 + x7 + 8x6 - 12x5 + 2x4 - 3x2 + x = 0')
        bot.register_next_step_handler(msg, result)


print('Работает!')
bot.polling(none_stop=True, interval=0)
