import telebot
import json
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from flask import Flask
import threading

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

# ✅ ИСПРАВЛЕННЫЙ словарь сокращений
days_map = {
    'понедельник': 'понедельник', 'пн': 'понедельник', '1': 'понедельник',
    'вторник': 'вторник', 'вт': 'вторник', '2': 'вторник',
    'среда': 'среда', 'ср': 'среда', '3': 'среда',
    'четверг': 'четверг', 'чт': 'четверг', '4': 'четверг',
    'пятница': 'пятница', 'пт': 'пятница', '5': 'пятница',
    'суббота': 'суббота', 'сб': 'суббота', '6': 'суббота',
    'воскресенье': 'воскресенье', 'вс': 'воскресенье', '7': 'воскресенье'
}

# Безопасная загрузка расписания
try:
    with open('schedule.json', 'r', encoding='utf-8') as f:
        schedule = json.load(f)
except:
    schedule = {}  # Если файла нет

# Клавиатура с днями
def get_days_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    markup.add(KeyboardButton('📅 Понедельник'), KeyboardButton('📅 Вторник'))
    markup.add(KeyboardButton('📅 Среда'), KeyboardButton('📅 Четверг'))
    markup.add(KeyboardButton('📅 Пятница'), KeyboardButton('📅 Суббота'))
    markup.add(KeyboardButton('📅 Воскресенье'))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 
        "🔔 Привет! Я бот с расписанием уроков Тимоши.\n"
        "Напиши день недели или выбери кнопку ниже:",
        reply_markup=get_days_keyboard())

@bot.message_handler(content_types=['text'])
def handle_day(message):
    day_input = message.text.lower().strip().replace('📅 ', '')
    day = days_map.get(day_input)
    
    if not day:
        bot.reply_to(message, 
            "❌ Не понял день. Выбери из кнопок или напиши: понедельник, вторник...", 
            reply_markup=get_days_keyboard())
        return
    
    if day not in schedule or not schedule[day]:
        bot.reply_to(message, f"📅 На {day.capitalize()} уроков нет!", reply_markup=get_days_keyboard())
        return
    
    text = f"📚 Расписание на <b>{day.capitalize()}</b>:\n\n"
    for lesson in schedule[day]:
        text += f"⏰ <b>{lesson['время']}</b> - {lesson['урок']}\n"
    
    bot.reply_to(message, text, parse_mode='HTML', reply_markup=get_days_keyboard())

# Веб-сервер для Render
app = Flask(__name__)

@app.route("/")
def hello():
    return "🔔 Telegram бот с расписанием уроков Тимоши работает!"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    print("Бот запущен!")
    bot.infinity_polling()
