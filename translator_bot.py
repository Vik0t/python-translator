from googletrans import Translator
translator = Translator()
from gtts import gTTS
import telebot
from telebot import types
bot = telebot.TeleBot('6191694817:AAGW7Q40wPTqsufZqRr9UJm1OVYHtkVy23w')

@bot.message_handler(content_types=['start'])
def start(message):     
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Начать")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я бот переводчик, используй кнопки для выбора перевода)".format(message.from_user), reply_markup=markup)
bot.polling(none_stop=True)

@bot.message_handler(content_types=['text'])
def func(message):
    if message.text == "👋 Начать":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Русский")
        btn2 = types.KeyboardButton("English")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбери язык оригинала", reply_markup=markup)
        bot.register_next_step_handler(message, choose_language)
    else:
        bot.send_message(message.from_user.id, 'нажми: "Начать"')

def choose_language(message):
    if message.text.lower() == 'english':
        bot.send_message(message.from_user.id, "Введите текст для перевода :  ")
        bot.register_next_step_handler(message, rus_to_eng)
    elif message.text.lower() == 'русский':
        bot.send_message(message.from_user.id, "Введите текст для перевода:  ")
        bot.register_next_step_handler(message, eng_to_rus)
    elif (message.text.lower() == "вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Начать")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

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

