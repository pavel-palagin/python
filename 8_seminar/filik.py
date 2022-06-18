from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

# pip install python-telegram-bot - загрузить библиотеку

bot = Bot(token='5383415735:AAEk9fMkDtTps-YwioL3esJkeQaR7CVeRCU')
updater = Updater(token='5383415735:AAEk9fMkDtTps-YwioL3esJkeQaR7CVeRCU', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    arg = context.args
    if not arg:
        context.bot.send_message(update.effective_chat.id, "Привет")
    else:
        context.bot.send_message(update.effective_chat.id, f"{' '.join(arg)}")


def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Меня создала компания GB!")


def message(update, context):
    text = update.message.text
    if text.lower() == 'привет':
        context.bot.send_message(update.effective_chat.id, 'И тебе привет..')
    else:
        context.bot.send_message(update.effective_chat.id, 'я тебя не понимаю')


def unknown(update, context):
    context.bot.send_message(update.effective_chat.id, 'Ты несешь какую-то дичь...')


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown) #/game

dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print("server_started")

updater.start_polling()
updater.idle()