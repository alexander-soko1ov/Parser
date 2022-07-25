from datetime import datetime

import telebot

from parser import main_handler, STATUS, FAILED, SUCCESS


HELP_MSG = """Просто отправь задачу в сообщении!
Примеры:
- Выйти на пробежку завтра утром
- Сделать отчёт в 17:00 13 декабря 2023 года
"""

with open('TOKEN') as f:
    TOKEN = f.read()

bot = telebot.TeleBot(TOKEN)


def send_task_confirmation(json_task: dict, chat_id: int):
    msg  = f"Задача: {json_task['TEXT']}\n"
    date = json_task['DATE']
    if not json_task['PARAMS']['repeat_every']:
        msg += f"Повторять: Никогда\n"
    else:
        msg += f"Повторять: {json_task['PARAMS']['repeat_every']}\n"
    msg += f"Выполнить в {date['hour']}:{date['minute']} {date['day']}.{date['month']}.{date['year']}\n"
    msg += '\nВерно?'

    # keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    # btn = telebot.types.KeyboardButton("Потвердить")

    keyboard = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton('Потвердить', callback_data="Потвердить")
    keyboard.add(btn)

    bot.send_message(chat_id, msg, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(q: telebot.types.CallbackQuery):
    if q.data == "Потвердить":
        bot.send_message(q.message.chat.id, "Задача создана! :)")
        bot.edit_message_text(q.message.text, q.message.chat.id, q.message.id)
        # bot.delete_message(q.message.chat.id, q.message.id)
        bot.answer_callback_query(q.id, "Задача создана!")


@bot.message_handler(commands=['start'])
def start_cmd(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.full_name}! Отправь задачу в сообщении!')


@bot.message_handler(commands=['help'])
def help_cmd(message: telebot.types.Message):
    bot.send_message(message.chat.id, HELP_MSG)


@bot.message_handler(content_types=['text'])
def task_handler(message: telebot.types.Message):
    msg = message.text
    print(msg)

    json_output = main_handler(msg)
    print(json_output)
    if json_output[STATUS] == SUCCESS:
        send_task_confirmation(json_output, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Не могу создать задачу :(\nПопробуй ещё раз!")


if __name__ == '__main__':
    print('Запуск бота...')
    bot.infinity_polling()