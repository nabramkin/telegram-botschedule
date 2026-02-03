{\rtf1\ansi\ansicpg1251\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import telebot\
import json\
import os\
from telebot.types import ReplyKeyboardMarkup, KeyboardButton\
\
TOKEN = os.getenv('TOKEN')  # \uc0\u1058 \u1086 \u1082 \u1077 \u1085  \u1080 \u1079  \u1087 \u1077 \u1088 \u1077 \u1084 \u1077 \u1085 \u1085 \u1099 \u1093  Render\
bot = telebot.TeleBot(TOKEN)\
\
# \uc0\u1057 \u1083 \u1086 \u1074 \u1072 \u1088 \u1100  \u1076 \u1083 \u1103  \u1086 \u1073 \u1088 \u1072 \u1073 \u1086 \u1090 \u1082 \u1080  \u1089 \u1086 \u1082 \u1088 \u1072 \u1097 \u1077 \u1085 \u1080 \u1081 \
days_map = \{\
    '\uc0\u1087 \u1086 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1080 \u1082 ': '\u1087 \u1086 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1080 \u1082 ', '\u1087 \u1085 ': '\u1087 \u1086 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1080 \u1082 ', '1': '\u1087 \u1086 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1080 \u1082 ',\
    '\uc0\u1074 \u1090 \u1086 \u1088 \u1085 \u1080 \u1082 ': '\u1074 \u1090 \u1086 \u1088 \u1085 \u1080 \u1082 ', '\u1074 \u1090 ': '\u1074 \u1090 \u1086 \u1088 \u1085 \u1080 \u1082 ', '2': '\u1074 \u1090 \u1086 \u1088 \u1085 \u1080 \u1082 ',\
    '\uc0\u1089 \u1088 \u1077 \u1076 \u1072 ': '\u1089 \u1088 \u1077 \u1076 \u1072 ', '\u1089 \u1088 ': '\u1089 \u1088 \u1077 \u1076 \u1072 ', '3': '\u1089 \u1088 \u1077 \u1076 \u1072 ',\
    '\uc0\u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 ': '\u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 ', '\u1095 \u1090 ': '\u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 ', '4': '\u1095 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 ',\
    '\uc0\u1087 \u1103 \u1090 \u1085 \u1080 \u1094 \u1072 ': '\u1087 \u1103 \u1090 \u1085 \u1080 \u1094 \u1072 ', '\u1087 \u1090 ': '\u1087 \u1103 \u1090 \u1085 \u1080 \u1094 \u1072 ', '5': '\u1087 \u1103 \u1090 \u1085 \u1080 \u1094 \u1072 ',\
    '\uc0\u1089 \u1091 \u1073 \u1073 \u1086 \u1090 \u1072 ': '\u1089 \u1091 \u1073 \u1073 \u1086 \u1090 \u1072 ', '\u1089 \u1073 ': '\u1089 \u1091 \u1073 \u1073 \u1086 \u1090 \u1072 ', '6': '\u1089 \u1091 \u1073 \u1073 \u1086 \u1090 \u1072 ',\
    '\uc0\u1074 \u1086 \u1089 \u1082 \u1088 \u1077 \u1089 \u1077 \u1085 \u1100 \u1077 ': '\u1074 \u1086 \u1089 \u1082 \u1088 \u1077 \u1089 \u1077 \u1085 \u1100 \u1077 ', '\u1074 \u1089 ': '\u1074 \u1086 \u1089 \u1082 \u1088 \u1077 \u1089 \u1077 \u1085 \u1100 \u1077 ', '7': '\u1074 \u1086 \u1089 \u1082 \u1088 \u1077 \u1089 \u1077 \u1085 \u1100 \u1077 '\
\}\
\
# \uc0\u1047 \u1072 \u1075 \u1088 \u1091 \u1079 \u1082 \u1072  \u1088 \u1072 \u1089 \u1087 \u1080 \u1089 \u1072 \u1085 \u1080 \u1103 \
with open('schedule.json', 'r', encoding='utf-8') as f:\
    schedule = json.load(f)\
\
# \uc0\u1050 \u1083 \u1072 \u1074 \u1080 \u1072 \u1090 \u1091 \u1088 \u1072  \u1089  \u1076 \u1085 \u1103 \u1084 \u1080 \
def get_days_keyboard():\
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)\
    markup.add(KeyboardButton('\uc0\u55357 \u56517  \u1055 \u1086 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1080 \u1082 '), KeyboardButton('\u55357 \u56517  \u1042 \u1090 \u1086 \u1088 \u1085 \u1080 \u1082 '))\
    markup.add(KeyboardButton('\uc0\u55357 \u56517  \u1057 \u1088 \u1077 \u1076 \u1072 '), KeyboardButton('\u55357 \u56517  \u1063 \u1077 \u1090 \u1074 \u1077 \u1088 \u1075 '))\
    markup.add(KeyboardButton('\uc0\u55357 \u56517  \u1055 \u1103 \u1090 \u1085 \u1080 \u1094 \u1072 '), KeyboardButton('\u55357 \u56517  \u1057 \u1091 \u1073 \u1073 \u1086 \u1090 \u1072 '))\
    markup.add(KeyboardButton('\uc0\u55357 \u56517  \u1042 \u1086 \u1089 \u1082 \u1088 \u1077 \u1089 \u1077 \u1085 \u1100 \u1077 '))\
    return markup\
\
@bot.message_handler(commands=['start'])\
def start(message):\
    bot.reply_to(message, \
        "\uc0\u55357 \u56596  \u1055 \u1088 \u1080 \u1074 \u1077 \u1090 ! \u1071  \u1073 \u1086 \u1090  \u1089  \u1088 \u1072 \u1089 \u1087 \u1080 \u1089 \u1072 \u1085 \u1080 \u1077 \u1084  \u1091 \u1088 \u1086 \u1082 \u1086 \u1074 .\\n"\
        "\uc0\u1053 \u1072 \u1087 \u1080 \u1096 \u1080  \u1076 \u1077 \u1085 \u1100  \u1085 \u1077 \u1076 \u1077 \u1083 \u1080  \u1080 \u1083 \u1080  \u1074 \u1099 \u1073 \u1077 \u1088 \u1080  \u1082 \u1085 \u1086 \u1087 \u1082 \u1091  \u1085 \u1080 \u1078 \u1077 :",\
        reply_markup=get_days_keyboard())\
\
@bot.message_handler(content_types=['text'])\
def handle_day(message):\
    day_input = message.text.lower().strip().replace('\uc0\u55357 \u56517  ', '')\
    day = days_map.get(day_input)\
    \
    if not day:\
        bot.reply_to(message, \
            "\uc0\u10060  \u1053 \u1077  \u1087 \u1086 \u1085 \u1103 \u1083  \u1076 \u1077 \u1085 \u1100 . \u1042 \u1099 \u1073 \u1077 \u1088 \u1080  \u1080 \u1079  \u1082 \u1085 \u1086 \u1087 \u1086 \u1082  \u1080 \u1083 \u1080  \u1085 \u1072 \u1087 \u1080 \u1096 \u1080 : \u1087 \u1086 \u1085 \u1077 \u1076 \u1077 \u1083 \u1100 \u1085 \u1080 \u1082 , \u1074 \u1090 \u1086 \u1088 \u1085 \u1080 \u1082 ...", \
            reply_markup=get_days_keyboard())\
        return\
    \
    if day not in schedule or not schedule[day]:\
        bot.reply_to(message, f"\uc0\u55357 \u56517  \u1053 \u1072  \{day.capitalize()\} \u1091 \u1088 \u1086 \u1082 \u1086 \u1074  \u1085 \u1077 \u1090 !", reply_markup=get_days_keyboard())\
        return\
    \
    text = f"\uc0\u55357 \u56538  \u1056 \u1072 \u1089 \u1087 \u1080 \u1089 \u1072 \u1085 \u1080 \u1077  \u1085 \u1072  <b>\{day.capitalize()\}</b>:\\n\\n"\
    for lesson in schedule[day]:\
        text += f"\uc0\u9200  <b>\{lesson['\u1074 \u1088 \u1077 \u1084 \u1103 ']\}</b> - \{lesson['\u1091 \u1088 \u1086 \u1082 ']\}\\n"\
    \
    bot.reply_to(message, text, parse_mode='HTML', reply_markup=get_days_keyboard())\
\
print("\uc0\u1041 \u1086 \u1090  \u1079 \u1072 \u1087 \u1091 \u1097 \u1077 \u1085 !")\
bot.infinity_polling()\
}