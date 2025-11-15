import telebot
import datetime

BOT_TOKEN = "8242888193:AAHVwZKAGTacCaQrfRWVuDtZgdMbmsU30J0"
CHANNEL_ID = "-100XXXXX"  # Pon aquí el ID de tu canal (yo te digo cómo sacarlo)

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "¡Hola! Envíame el comprobante cuando pagues tu suscripción.")

bot.polling()
