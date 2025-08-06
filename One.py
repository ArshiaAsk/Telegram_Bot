from telebot import TeleBot
import time 
import requests
from config import API_token

# print(requests.get("https://api.telegram.org").status_code)

# requests.get("https://api.telegram.org/bot<7918952359:AAG4lzKbaWPZpijA9ck8deOxxUKiGgbKsXI>/deleteWebhook")

bot = TeleBot(API_token)

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, 'Hello Arshia \n What can i do for you?')
    # bot.reply_to(message, 'this is a reply')

bot.polling() 
 
 
# @bot.message_handler(content_types=['document', 'audio'])  
# def handler_docs_audio(message):
#     if message.audio:
#         bot.reply_to(message, 'this is a audio!') 
#     elif message.document:
#         bot.reply_to(message, 'this is a doc!')

 
@bot.message_handler(regexp='Arshia')
def handel_message(message):
    bot.reply_to(message, 'Arshia is here')
    
    
# @bot.message_handler(func=lambda message: message.document.mime_type == 'text/plain', content_types=['document'])
# def handel_text_doc(message):
#     bot.reply_to(message, 'this is a text file')
    

def test_message(message):
    return message.document.mime_type == 'text/plain'

@bot.message_handler(func=test_message, content_types=['document'])
def handle_text_doc(message):
    bot.reply_to(message, 'this is a text file...')


@bot.message_handler(commands=['hello'])
@bot.message_handler(func=lambda msg: msg.text == '😂')
def send_something(message):
    bot.reply_to(message, 'Emoji')
    


print('bot is running...')
bot.polling(none_stop=True, interval=0, timeout=5)


