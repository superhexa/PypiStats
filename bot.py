import telebot
from telebot import types
from functions import PypiStats
from config import *

bot = telebot.TeleBot(TOKEN)
stats = PypiStats(PROJECT_ID, KEYS_JSON)

def create_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("🔗 Source Code", url="https://github.com/superhexa/PypiStats"))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Hello! Send me a package name, and I'll fetch its total downloads. 📦🚀", reply_markup=create_markup())

@bot.message_handler(func=lambda m: True)
def send_stats(message):
    pkg = message.text
    total_downloads = stats.get_total_downloads(pkg)
    msg = (f"📦 <b>{pkg}</b> has been downloaded <b>{total_downloads}</b> times! 🚀🎉" if total_downloads else "❌ Oops! Package not found. Please try again. 🔍")
    bot.send_message(message.chat.id, msg, parse_mode="HTML", reply_markup=create_markup())

bot.infinity_polling()
