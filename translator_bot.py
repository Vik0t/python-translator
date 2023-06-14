from googletrans import Translator
translator = Translator()
from gtts import gTTS
import telebot
bot = telebot.TeleBot('6191694817:AAGW7Q40wPTqsufZqRr9UJm1OVYHtkVy23w')
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Привет. Введите язык для перевода (на который переводится) русский или английский:  ")
        bot.register_next_step_handler(message, choose_language)
    else:
        bot.send_message(message.from_user.id, 'Напиши: /start')
def choose_language(message):
    if message.text == 'английский' or message.text == 'Английский':

        bot.send_message(message.from_user.id, "Введите текст для перевода :  ")
        bot.register_next_step_handler(message, rus_to_eng)
    elif message.text == 'русский' or message.text == 'Русский':


        bot.send_message(message.from_user.id, "Введите текст для перевода:  ")
        bot.register_next_step_handler(message, eng_to_rus)
    else:
        bot.send_message(message.from_user.id, 'Напиши: /start')
def rus_to_eng(message):
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
def eng_to_rus(message):
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
