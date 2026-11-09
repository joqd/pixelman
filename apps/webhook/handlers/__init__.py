from telebot import TeleBot

from .start import start_handler


def register_handlers(bot: TeleBot) -> None:
    bot.register_message_handler(start_handler, commands=['start'], pass_bot=True)
