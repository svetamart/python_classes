import telebot
from telebot.util import quick_markup

token = 'YOUR TOKEN'
bot = telebot.TeleBot(token)

result = ''
old_result = ''

keyboard = quick_markup({
    'C': {'callback_data': 'CLEAR'},
    '(': {'callback_data': '('},
    ')': {'callback_data': ')'},
    '/': {'callback_data': '/'},
    '7': {'callback_data': '7'},
    '8': {'callback_data': '8'},
    '9': {'callback_data': '9'},
    'x': {'callback_data': '*'},
    '4': {'callback_data': '4'},
    '5': {'callback_data': '5'},
    '6': {'callback_data': '6'},
    '-': {'callback_data': '-'},
    '1': {'callback_data': '1'},
    '2': {'callback_data': '2'},
    '3': {'callback_data': '3'},
    '+': {'callback_data': '+'},
    'x^2': {'callback_data': '**2'},
    '0': {'callback_data': '0'},
    '.': {'callback_data': '.'},
    '=': {'callback_data': '='},
}, row_width=4)


@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    global result, old_result
    data = query.data
    if data == 'CLEAR':
        result = ''
    elif data == '=':
        try:
            result = str(eval(result))
        except:
            result = ''
    else:
        result += data

    if result != old_result:
        if result == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                  text='0', reply_markup=keyboard)
            old_result = '0'
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id,
                                  text=result, reply_markup=keyboard)
            old_result = result


@bot.message_handler(commands=['calc'])
def calculate(message):
    global result
    bot.send_message(message.chat.id, '''Используй клавиатуру, чтобы набрать математическое выражение в строке калькулятора. \n
Жми знак "=", чтобы получить результат.''')
    if result == '':
        bot.send_message(message.from_user.id, '0', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, result, reply_markup=keyboard)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'''Привет, {message.from_user.first_name}!
Чтобы воспользоваться калькулятором, просто вызови команду /calc.''')



print('Работает!')
bot.polling()
