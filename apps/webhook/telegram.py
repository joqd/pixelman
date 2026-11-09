import telebot
from django.conf import settings
from telebot import apihelper

from .handlers import register_handlers

apihelper.API_URL = settings.LOCAL_TELEGRAM_API + '/bot{0}/{1}'

bot = telebot.TeleBot(settings.BOT_TOKEN, use_class_middlewares=True)

register_handlers(bot)
