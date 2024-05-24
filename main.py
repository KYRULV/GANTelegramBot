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
    bot.send_message(message.chat.id, players[cur_player_id].wished_number)

bot.infinity_polling()