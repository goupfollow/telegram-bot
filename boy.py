import os
import telebot

TOKEN = os.getenv("8413326343:AAFuwj5YWbwhu24OMOS-MJX1tEBkVIBYvcE")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot is Online 🔥")

bot.infinity_polling()
