import api_key_reader
import telebot
import Player
import random

bot = telebot.TeleBot(api_key_reader.get())

players = dict()

def wish_a_number():
    random_number = random.randint(0, 20)
    return random_number

@bot.message_handler(commands=["start"]) 
def start(message):
    cur_player_id = message.from_user.id
    players[cur_player_id] = Player.Player()
    players[cur_player_id].wished_number = wish_a_number()
    bot.send_message(message.chat.id, "Привет, я телеграмм бот который загадывает числа")

def message_filter(message):
    return True 

@bot.message_handler(func=message_filter) 
def on_message(message):
    try:
        guessed_number = int(message.text)
    except:
        bot.send_message(message.chat.id, "Введите число")
    cur_player_id = message.from_user.id
    wished_number = players[cur_player_id].wished_number
    if wished_number == guessed_number:
        bot.send_message(message.chat.id, "Молодец, правильно угаданое число")
    else:
        bot.send_message(message.chat.id, "Неверное число, попробуй снова")

bot.infinity_polling()