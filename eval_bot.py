import os, telebot

TOKEN = os.environ["TOKEN"]
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_hello(message):
	bot.reply_to(message, "Hello man")

@bot.message_handler(func = lambda m: True)
def echo_all(message):
	bot.reply_to(message, "Expression result is: " + str(eval(message.text)))

bot.infinity_polling()