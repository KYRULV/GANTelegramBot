import api_key_reader
import telebot

bot = telebot.TeleBot(api_key_reader.get())
