import os
import telebot

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_hello(message):
    """Places greeting message"""

    bot.reply_to(message, "Hello man")

@bot.message_handler(func = lambda m: True)
def echo_all(message):
    """Evals received message"""

    try:
        result = eval(message.text) # pylint: disable=eval-used
        bot.reply_to(message, "Expression result is: " + str(result))
    except SyntaxError:
        bot.reply_to(message, "Your message does not satisfy python syntax!")
    except: # pylint: disable=bare-except
        bot.reply_to(message, "Your message has an error in runtime or in 'compilation'!")

bot.infinity_polling()
