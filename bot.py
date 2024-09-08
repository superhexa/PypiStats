import telebot
from telebot import types
from functions.big_query import PypiStats
from config import *
from functions.db import Database
import datetime

bot = telebot.TeleBot(TOKEN)
stats = PypiStats(PROJECT_ID, KEYS_JSON)
db = Database('database.db')

def create_markup():
    return types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🔗 Source Code", url="https://github.com/superhexa/PypiStats"))

def userex(handler):
    def wrapper(message):
        user_id = message.from_user.id
        if not db.user_exists(user_id):
            db.add_user(user_id)
        return handler(message)
    return wrapper

@bot.message_handler(commands=['start'])
@userex
def start(message):
    bot.send_message(message.chat.id, "👋 Send me a package name, and I'll fetch its total downloads. 📦🚀", reply_markup=create_markup())

@bot.message_handler(func=lambda m: True)
@userex
def send_stats(message):
    pkg = message.text
    pkg_data = db.get_pkg_stats(pkg)
    now = datetime.datetime.now()

    if pkg_data and (now - datetime.datetime.fromisoformat(pkg_data['timestamp'])).days < 1:
        total_downloads = pkg_data['downloads']
    else:
        total_downloads = stats.get_total_downloads(pkg)
        db.add_pkg(pkg, total_downloads, now.isoformat())

    msg = f"📦 <b>{pkg}</b> has been downloaded <b>{total_downloads}</b> times! 🚀🎉" if total_downloads else "❌ Oops! Package not found. 🔍"
    bot.send_message(message.chat.id, msg, parse_mode="HTML", reply_markup=create_markup())

bot.infinity_polling()
