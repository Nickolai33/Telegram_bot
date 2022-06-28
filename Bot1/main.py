import telebot
from telebot import types

bot = telebot.TeleBot('5524995976:AAF5Q3Ij1gxhAqnjJIKFbNrUuKe6u0hNm88')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    b1 = types.KeyboardButton('Курсы валют Беларусь')
    b2 = types.KeyboardButton('Курс Биткоина к доллару')
    b3 = types.KeyboardButton('Погода в Минске')
    markup.add(b1, b2, b3)
    nick = f'Привет 👋, <b>{message.from_user.first_name}!</b>\nЕсли хочешь что-нибудь узнать,' \
           f' то нажми кнопку ниже 👇 с интересующей тебя информацией.'
    bot.send_message(message.chat.id, nick, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['exchange'])
def exchange(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Курсы валют Беларусь',
                                          url='https://myfin.by/currency/minsk'))
    bot.send_message(message.chat.id, '⬇Перейдите по ссылке⬇', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['bitcoin'])
def bitcoin(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Курс Биткоина к доллару',
                                          url='https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B1%D0%B8'
                                              '%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB'
                                              '%D0%B0%D1%80%D1%83&sxsrf=ALiCzsZ5aDADU-FtpQi2PuFBaTREUE43Ww'
                                              '%3A1656352497695&ei=8e65Yv__KcGvrgT1zYrgDA&oq=%D0%BA%D1%83%D1%80%D1%81'
                                              '+%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD%D0%B0&gs_lp'
                                              '=ugYECAEYCBIHZ3dzLXdpergBASoCCAAyBxAAGEcYsAMyBxAAGEcYsAMyBxAAGEcYsAMyBx'
                                              'AAGEcYsAMyChAAGEcYsAMYyQMyBxAAGEcYsAMyBxAAGEcYsAMyBxAAGEcYsAMyBxAAGLADG'
                                              'EMyExAuGMcBGNEDGMgDGLADGEPYAQEyExAuGMcBGNEDGMgDGLADGEPYAQEyExAuGMcBGNED'
                                              'GMgDGLADGEPYAQGQBgxI-wlQAFgAcAF4AcgBAJABAJgBAKABAKoBAOIDBCBBGADiAwQgRhg'
                                              'AiAYB&sclient=gws-wiz'))
    bot.send_message(message.chat.id, '⬇Перейдите по ссылке⬇', parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['weather'])
def weather(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Погода в Минске',
                                          url='https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0'
                                              '+%D0%B2+%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B5&oq=%D0%BF%D0%BE%D0%B3%D0'
                                              '%BE%D0%B4%D0%B0+%D0%B2+%D0%BC%D0%B8%D0%BD%D1%81%D0%BA%D0%B5&aqs=chrome'
                                              '..69i57j0i457i512j0i402j0i512l7.2127j1j9&sourceid=chrome&ie=UTF-8'))
    bot.send_message(message.chat.id, '⬇Перейдите по ссылке⬇', parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_1(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot == 'курсы валют беларусь':
        photo = open('money.bmp', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Жми ещё!', exchange(message))
    elif get_message_bot == 'курс биткоина к доллару':
        photo = open('bitcoin.bmp', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Жми ещё!', bitcoin(message))
    elif get_message_bot == 'погода в минске':
        photo = open('weather.bmp', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, 'Жми ещё!', weather(message))
    else:
        photo = open('да что ты.bmp', 'rb')
        bot.send_photo(message.chat.id, photo)
        bot.send_message(message.chat.id, '⬇⬇⬇Лучше нажми кнопки, что снизу⬇⬇⬇', parse_mode='html')


bot.polling(none_stop=True)
