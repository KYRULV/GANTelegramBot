import api_key_reader
import telebot

bot = telebot.TeleBot(api_key_reader.get())

@bot.message_handler(commands=["start"]) 
def start(message):
    print("hello")
    bot.send_message(message.chat.id, "Привет, я телеграмм бот который загадывает числа!")
    
bot.infinity_polling() 