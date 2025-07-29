# import telebot

# bot = telebot.TeleBot('7918952359:AAG4lzKbaWPZpijA9ck8deOxxUKiGgbKsXI')

# @bot.message_handler(commands=['start'])
# def start_message(message):
#     bot.send_message(message.chat.id, "Please enter your name: ")
#     bot.register_next_step_handler(message, process_name)
      
# def process_name(message):
#     name = message.text
#     bot.send_message(message.chat.id, f"Hello {name} \n how old are you?")
#     bot.register_next_step_handler(message, process_age)
    
# def process_age(message):
#     age = message.text 
#     bot.send_message(message.chat.id, f"you are {age} years old")
    
    
# print('bot is runnig...')    
# bot.polling()
