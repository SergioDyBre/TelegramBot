from telegram.ext import Updater, CommandHandler


def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('1142606683:AAFHEBgNIDbqZZ6RizWYRLFmqRpr-8KRBEg', use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()