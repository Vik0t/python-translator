from googletrans import Translator
translator = Translator()
from gtts import gTTS
from telebot import types
import telebot
bot = telebot.TeleBot('6191694817:AAGW7Q40wPTqsufZqRr9UJm1OVYHtkVy23w')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Английский")
        item2=types.KeyboardButton("Русский")
        item3=types.KeyboardButton("Меню")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'Привет. Введите язык для перевода (на который переводится) русский или английский:', reply_markup = markup)
        bot.register_next_step_handler(message, start1)
    else:
        bot.send_message(message.from_user.id, 'Напиши: /start')
def start1(message):
    if message.text == 'Английский':
        bot.send_message(message.chat.id, "Введите текст для перевода :  ")
        bot.register_next_step_handler(message, en)
    elif message.text == 'Русский':
        bot.send_message(message.chat.id, "Введите текст для перевода:  ")
        bot.register_next_step_handler(message, ru)
    elif message.text == 'Меню':
        bot.send_message(message.chat.id, 'Привет. Введите язык для перевода (на который переводится) русский или английский:')
        bot.register_next_step_handler(message, start1)
def en(message):
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
        bot.register_next_step_handler(message, start1)
def ru(message):
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
        bot.register_next_step_handler(message, start1)
bot.polling()
