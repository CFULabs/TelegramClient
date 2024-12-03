import json
from config import TOKEN
import logging
import telebot
from telebot import types
from funcs import*


bot = telebot.TeleBot(TOKEN)

command = (
    "/start - предисловие\n"
    "/schedule - получить расписание\n"
    "/help - список доступных комманд"
)

user = {}
date = {}
datamap = {}


@bot.message_handler(commands=['start'])
def start(message):
    speech = open('start.txt', encoding='utf-8').read()
    bot.send_message(message.chat.id, speech)


@bot.message_handler(commands=['help'])
def commands(message):
    bot.send_message(message.chat.id, f"{command}")


@bot.message_handler(commands=['schedule'])
def get_group(message):
    user["id"] = message.chat.id
    bot.send_message(message.chat.id, "Введите полное название вашей группы согласно этому примеру:\n"
                                      "ПИ-б-о-231(2)")
    bot.register_next_step_handler(message, get_week)


def get_week(message):
    global datamap
    datamap = get_full(message.text)
    # json_f = json.dumps((user | datamap), ensure_ascii=False)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    odd_week = types.KeyboardButton("Нечётная")
    even_week = types.KeyboardButton("Чётная")
    markup.add(odd_week, even_week)

    bot.send_message(message.chat.id, "Выберите чётность недели", reply_markup=markup)
    bot.register_next_step_handler(message, get_day)


def get_day(message):
    date["week"] = week(message.text)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    today = types.KeyboardButton("Сегодня")
    tomorrow = types.KeyboardButton("Завтра")
    monday = types.KeyboardButton("Понедельник")
    tuesday = types.KeyboardButton("Вторник")
    wednesday = types.KeyboardButton("Среда")
    thursday = types.KeyboardButton("Четверг")
    friday = types.KeyboardButton("Пятница")
    markup.add(today, tomorrow, monday, tuesday, wednesday, thursday, friday)

    bot.send_message(message.chat.id, "Выберите день недели", reply_markup=markup)
    bot.register_next_step_handler(message, schedule)


def schedule(message):
    date["day"] = day(message.text)
    json_data = json.dumps(date, ensure_ascii=False)
    json_datamap = json.dumps(datamap, ensure_ascii=False)
    bot.send_message(message.chat.id, f'Группа: {json_datamap}, '
                                      f'Расписание на {json_data}',
                     reply_markup=types.ReplyKeyboardRemove())


bot.polling(non_stop=True)
