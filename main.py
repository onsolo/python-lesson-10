# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.
# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

import telebot
import datetime

templates = {
    'помогите': 'Что случилось?',
    'сколько звёзд на небе?': 'Считаю...',
    'позови человека': 'Я и есть человек',
    'у меня завис компьютер': 'Попробуйте его перезагрузить',
}

bot = telebot.TeleBot("5912551029:AAFQjpbDMSwWNvupbX0YLEH8ZVLFWecHvck", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def message_listener(message):
    with open('appeals.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{datetime.datetime.now()}:{message.from_user.first_name}:{message.text}\n')

    with open('appeals.txt', 'r', encoding='UTF-8') as file:
        appeal = file.readlines()[-1]
        appeal_text = appeal.split(':')[-1].rstrip('\n')

        answer = templates.get(appeal_text.lower())
        if answer is not None:
            bot.send_message(message.chat.id, answer)


bot.infinity_polling()
