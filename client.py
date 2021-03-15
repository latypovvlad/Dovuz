import telebot
import Const
bot = telebot.TeleBot(Const.token)
from telebot import types

def aliasUser(message):
    return '@' + message.from_user.username

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":         #Отвечает пользователю на слово "привет"
        keyboard = types.InlineKeyboardMarkup()
        key_faq = types.InlineKeyboardButton(text='FAQ', callback_data='faq') #кнопка FAQ
        keyboard.add(key_faq)
        key_events = types.InlineKeyboardButton(text='Просмотреть мероприятия', callback_data='events') #кнопка Посмотреть мероприятия
        keyboard.add(key_events)
        bot.send_message(message.from_user.id, text='Привет, чем я могу тебе помочь?', reply_markup=keyboard)
    elif message.text == "/help": #Отвечает пользователю на слово "/хелп
        keyboard = types.InlineKeyboardMarkup()
        key_faq = types.InlineKeyboardButton(text='FAQ', callback_data='faq')
        keyboard.add(key_faq)
        key_events = types.InlineKeyboardButton(text='Просмотреть мероприятия', callback_data='events')
        keyboard.add(key_events)
        bot.send_message(message.from_user.id, text='Привет, чем я могу тебе помочь?', reply_markup=keyboard)
    elif message.text == "/start": #Отвечает пользователю на слово "/старт, и говорит какая роль"
        if message.chat.id == Const.chat_ID_Admin:
            texts = "Здраствуйте {}, вы админ!".format(aliasUser(message))
            bot.send_message(chat_id=message.chat.id, text=texts)
        else:
            texts = "Здраствуйте {}!".format(aliasUser(message))
            bot.send_message(chat_id=message.chat.id, text=texts)
    else: #когда пользователь что-то невнятное написал
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "faq":  #присылает faq когда пользователь нажимает на кнопку FAQ
        bot.send_message(call.message.chat.id, "Как опубликовать анонс в канале? \n"
		"Увидели мероприятие? Заполните форму ниже: \n"
		"site \n"
		"Являетесь организатором мероприятия? Заполните форму ниже: \n"
		"site \n"
		"\n"		
		"Как скоро будет опубликовано мое мероприятие?\n"
		"Обычно мы публикуем мероприятия в течение 2-14 дней в зависимости от заполненности графика.\n")
    if call.data == "events": 
        bot.send_message(call.message.chat.id, "Календарь мероприятий: site \n"
        	"Канал в телеграмме с мероприятими :  site \n"
        	"Группа в вк с мероприятими: site")
        m= "/"
        bot.send_message(chat_id=Const.chat_ID_Admin2, text=m)
            #присылает ссылки где можно посмотреть мероприятия когда пользователь нажимает на кнопку "Посмотреть мероприятия""
#тут классно было бы написать функцию что бот присылает мероприятия из бд, а не ссылки кидает где можно посмотреть
bot.polling(none_stop=True, interval=0)
