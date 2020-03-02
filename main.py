from telegram.ext import Updater, CommandHandler


def hello_handler(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def bye_handler(update, context):
    update.message.reply_text("Talogo {}".format(update.message.from_user.first_name))


updater = Updater('1142606683:AAFHEBgNIDbqZZ6RizWYRLFmqRpr-8KRBEg', use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello_handler))
updater.dispatcher.add_handler(CommandHandler('bye', bye_handler))

updater.start_polling()
updater.idle()