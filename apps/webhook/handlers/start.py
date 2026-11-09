import telebot


def start_handler(message: telebot.types.Message, bot: telebot.TeleBot) -> None:
    bot.reply_to(message, 'hello')
