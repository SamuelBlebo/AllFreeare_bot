from asyncore import dispatcher
from cgitb import handler
from this import d
from urllib import response
import Constants as keys
from telegram.ext import *
import Responses as R

print("Both started")


def start_command(update, context):
    update.message.reply_text("Type something to get started!")


def help_command(update, context):
    update.message.reply_text("If you need help, use google")

def handle_message(update, context):
     text = str(update.message.text).lower()
     response = R.sample_responses(text)

     update.message.reply_text(response)


def error(update, context):
    print(f"Update {update}caused error {context.error}" )


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    
    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()