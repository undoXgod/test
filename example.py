import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup

bot = telebot.TeleBot('5895040835:AAF3BCxYRIYTo-6-AfWGB0ibapxXg3-kqEM')


@bot.message_handler(commands=["start"])
def start(message):
    text = f"✌️ Приветствуем Вас!\n\n" \
           f"🔥   Этот бот создан для покупки подписок на разные сервисы!\n\n" \
           f"👇🏼   Ниже можешь ознакомиться с каталогом!\n\n"
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn = types.InlineKeyboardButton(text='🟣Discord Nitro', callback_data='btn1', parse_mode='HTML')
    btn1 = types.InlineKeyboardButton(text='🟢Spotify Premium', callback_data='btn2', parse_mode='HTML')
    btn2 = types.InlineKeyboardButton(text='🔵Telegram Premium', callback_data='btn3', parse_mode='HTML')
    markup.add(btn, btn1, btn2)
    with open('logo.png', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, reply_markup=markup, parse_mode='HTML')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        text = f"💜Discord Nitro💜\n\n" \
               f"✏️После покупки вы можете дать логин и пароль от своего аккаунта, а также возможно осуществить вход с помощью QR-код✏️\n\n" \
               f"‼️Ваш аккаунт никто не тронет, доступ нужен лишь для того, чтобы оплатить Nitro.‼️\n\n" \
               f"✅Данное Nitro не слетит и приобретается легальным способом с помощью личной банковской карты.✅\n\n"
        markupds: InlineKeyboardMarkup = types.InlineKeyboardMarkup(row_width=2)
        btnds = types.InlineKeyboardButton(text='🚕Nitro Basic', callback_data='btn1ds', parse_mode='HTML')
        btn1ds = types.InlineKeyboardButton(text='🏎Nitro Full', callback_data='btn2ds', parse_mode='HTML')
        btn2ds = types.InlineKeyboardButton(text='🚨О различиях', callback_data='btn3ds', parse_mode='HTML')
        btn3ds = types.InlineKeyboardButton(text='⬅️Вернуться назад', callback_data='btn4ds', parse_mode='HTML')
        markupds.add(btnds, btn1ds, btn2ds, btn3ds)
        with open('discordpage.jpg', 'rb') as photo:
            bot.send_photo(callback.message.chat.id, photo, caption=text, reply_markup=markupds)\


        @bot.callback_query_handler(func=lambda callback: callback.data)
        def check_callback_data(callback):
            if callback.data == 'btn4ds':
                bot.send_message(callback.message.chat.id, 'Вы вернулись в меню', reply_markup=None)

bot.polling(none_stop=True, interval=0)
