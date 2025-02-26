import telebot
from Config import TOKEN, keys
from Extensions import Apiexception, Cryptoconverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Даёшь мне три параметра:\n<1. имя валюты, цену которой надо узнать> \n<2. имя валюты, в которой надо узнать цену первой валюты> \n<3. количество первой валюты>\nА я те оплеуху! Шучу, не сци, прорвёмся :)\nГлянь на список доступных валют: /values'
    bot.send_message(message.chat.id, f"Опаньки, кто к нам пожаловал, здрасте, {message.chat.first_name}")
    bot.reply_to(message, text)

@bot.message_handler(commands =['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def get_price(message: telebot.types.Message):
    try:
        daten = message.text.split(' ')
        if len(daten) !=3:
            raise Apiexception('Сказано было, три параметра! А ты чё творишь?')

        base, quote, amount = daten

        val = Cryptoconverter.converter(base, quote, amount)
        result = float(val)*float(amount)
        formatted_result = f"{result:.2f}"
        res = f' Цена {amount} {base} в {quote} ровна {formatted_result}. Зачёт, бро!'
        bot.send_message(message.chat.id, res)
    except Apiexception as e:
        bot.send_message(message.chat.id, f'Ошибка: {e}')

bot.polling(non_stop=True)