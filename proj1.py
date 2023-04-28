import random
from telebot import types
from main import bot, photo_urls
@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Узнать")
    markup.row(button)
    bot.send_message(message.chat.id, text="А я знаю кто сегодня переспал с собакой и братом. \n А ты хочешь знать? Напиши /farid")
@bot.message_handler(commands=['farid'])
def farid(message):
    print(message)
    print("скамим мамонта")
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
    photo_url = photo_urls[random.randint(0, 7)]
    bot.send_photo(message.chat.id, photo=photo_url, caption='Он')
@bot.message_handler()
def spy(message):
    print(message)
    print(message.text)
    mt = message.text.lower()
    if "да" in mt[-2::]:
        bot.send_message(message.chat.id,"Пизда")
bot.polling(none_stop = True, interval = 0)
