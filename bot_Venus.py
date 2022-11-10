import telebot
import logger as lg
from info import token




bot = telebot.TeleBot(token, parse_mode='MARKDOWN')

@bot.message_handler(content_types=['sticker', 'pinned_message', 'photo', 'audio', 'video'])
def warning(message):
    bot.send_message(
        message.chat.id, f'Я тебя не понимаю. Введи: /help.')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id, f'Привет, *{message.from_user.first_name}!*\n При возникновении проблемм введи /help\nЧтобы перейти к вычислениям введи: /main')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        message.chat.id, f'/start - начать сначала (перезапустить бота)\n/main - главное меню\n/help - вызвать справку')


num1 = 0
num2 = 0
result = 0
num1_a = 0
num1_b = 0
num2_a = 0
num2_b = 0

@bot.message_handler(content_types=['text'])

def main(message):
    global num1, num2
    if message.text == '/main':
        bot.send_message(message.chat.id, f'С чем Вам предстоит работать? \n/1 - рациональные числа.\n/2 - комплекные числа.')
    bot.register_next_step_handler(message, get_operation_type)

def get_operation_type(message):

    if message.text == '/1':
        lg.logging.info('The user has selected real_number')
        bot.register_next_step_handler(message, get_num1_real)
    elif message.text == '/2':
        lg.logging.info('The user has selected complex_number')
        bot.register_next_step_handler(message, get_num1_a_complex)
    


def get_num1_real(message):
    global num1
    num1 = message.text
    num1 = int(num1)
    lg.logging.info('User entered: {num1}')
    bot.send_message(message.chat.id, f'Введите первое вещественное число: ')
    bot.register_next_step_handler(message, get_num2_real)

def get_num2_real(message):
    global num2
    num2 = message.text
    num2 = int(num2)
    lg.logging.info('User entered: {num2}')
    bot.send_message(message.chat.id, f'Введите второе вещественное число')
    bot.register_next_step_handler(message, print_operation_real)

def get_num1_a_complex(message):
    global num1_a
    num1_a = message.text
    num1_a = int(num1_a)
    lg.logging.info('User entered: {num1_a}')
    bot.send_message(message.chat.id, f'Введите для первого числа действительную часть')
    bot.register_next_step_handler(message, get_num1_b_complex)

def get_num1_b_complex(message):
    global num1_b
    num1_b = message.text
    num1_b = int(num1_b)
    lg.logging.info('User entered: {num1_b}')
    bot.send_message(message.chat.id, f'Введите для первого числа мнимую часть')
    bot.register_next_step_handler(message, get_num2_a_complex)

def get_num2_a_complex(message):
    global num2_a
    num2_a = message.text
    num2_a = int(num2_a)
    lg.logging.info('User entered: {num2_a}')
    bot.send_message(message.chat.id, f'Введите для второго числа действительную часть')
    bot.register_next_step_handler(message, get_num2_b_complex)

def get_num2_b_complex(message):
    global num2_b
    num2_b = message.text
    num2_b = int(num2_b)
    lg.logging.info('User entered: {num2_b}')
    bot.send_message(message.chat.id, f'Введите для второго числа мнимую часть')
    bot.register_next_step_handler(message, print_operation_complex)

def print_operation_real(message):
    bot.send_message(
        message.chat.id, f'Какую операцию Вы хотите выполнить? \n/sum - Сложение \n/sub - Вычитание\n/mult - Умножение\n/div - Деление\n/degree - Возведение в степень\n/pow - Извлечение корня.')
    bot.register_next_step_handler(message, get_operation_real)


def get_operation_real(message):
    global num1, num2, result

    if message.text == '/sum':       
        lg.logging.info('The user has selected sum for real_number')
        result = num1 + num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} + {num2} = {result}')
    

    elif message.text == '/sub':
        lg.logging.info('The user has selected sub for real_number')
        result = num1 - num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} - {num2} = {result}')

    elif message.text == '/mult':
        lg.logging.info('The user has selected mult for real_number')
        result = num1 * num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} * {num2} = {result}')


    elif message.text == '/div':
        lg.logging.info('The user has selected div for real_number')
        result = round(num1 / num2, 3)
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} / {num2} = {result}')


    elif message.text == '/degree':
        lg.logging.info('The user has selected degree for real_number')
        result = num1 ** num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} в степени {num2} = {result}')   

    elif message.text == '/pow':
        lg.logging.info('The user has selected pow for real_number')
        result = round(num1**(1/num2), 3)
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'Результат = {result}')  


def print_operation_complex(message):
    bot.send_message(
        message.chat.id, f'Какую операцию Вы хотите выполнить? \n/sum - Сложение \n/sub - Вычитание\n/mult - Умножение\n/div - Деление')
    bot.register_next_step_handler(message, get_operation_complex)

def get_operation_complex(message):
    global num1, num2, result, num1_a, num1_b, num2_a, num2_b
    num1 = complex(num1_a, num1_b)
    num2 = complex(num2_a, num2_b)
    
    if message.text == '/sum':       
        lg.logging.info('The user has selected sum for complex_number')
        result = num1 + num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} + {num2} = {result}')
    

    elif message.text == '/sub':
        lg.logging.info('The user has selected sub for complex_number')
        result = num1 - num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} - {num2} = {result}')

    elif message.text == '/mult':
        lg.logging.info('The user has selected mult for complex_number')
        result = num1 * num2
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} * {num2} = {result}')


    elif message.text == '/div':
        lg.logging.info('The user has selected div for real_number')
        result = round(num1 / num2, 3)
        lg.logging.info('Result operation: {result}')
        bot.send_message(
            message.chat.id, f'{num1} / {num2} = {result}')




print('server start')
bot.infinity_polling()
