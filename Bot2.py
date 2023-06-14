from googletrans import Translator
translator = Translator()
from gtts import gTTS
from telebot import types
import telebot
bot = telebot.TeleBot('6191694817:AAGW7Q40wPTqsufZqRr9UJm1OVYHtkVy23w')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        main_menu = types.InlineKeyboardMarkup() # создание клавиатуры
        main_menu.row_width = 2 # выбор размера(ширины)
        item1 = types.InlineKeyboardButton(text="Английский", callback_data = "английский")
        item2 = types.InlineKeyboardButton(text="Русский", callback_data = "русский")
        main_menu.add(item1)
        main_menu.add(item2)
        bot.send_message(message.chat.id, 'Привет. Введите язык для перевода (на который переводится) русский или английский:', reply_markup = main_menu)
    else:
        bot.send_message(message.from_user.id, 'Напиши: /start')
@bot.callback_query_handler(func=lambda call: True)
def start1(call):
    if call.data == 'английский':
        bot.send_message(call.message.chat.id, "Введите текст для перевода :  ")
        bot.register_next_step_handler(call.message, per)
    elif call.data == 'русский':
        bot.send_message(call.message.from_user.id, "Введите текст для перевода:  ")
        bot.register_next_step_handler(call.message, per1)
def per(message):
        z = translator.translate(message.text, src = "ru", dest = 'en')
        tr_word = z.text
        bot.send_message(message.from_user.id, tr_word )
        my_text = tr_word
        language = 'en'
        my_obj = gTTS(text = my_text,lang = language)
        my_obj.save('result.mp3')
        with open('result.mp3','rb') as a_f:
            audio = a_f.read()
        bot.send_audio(message.chat.id,audio)
def per1(message):
        z = translator.translate(message.text, src = "en", dest = 'ru')
        tr_word = z.text
        bot.send_message(message.from_user.id, tr_word )
        my_text = tr_word
        language = 'ru'
        my_obj = gTTS(text = my_text,lang = language)
        my_obj.save('result.mp3')
        with open('result.mp3','rb') as a_f:
            audio = a_f.read()
        bot.send_audio(message.chat.id,audio)
bot.polling()
