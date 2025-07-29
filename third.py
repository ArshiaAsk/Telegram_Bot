# from telebot import TeleBot
# from config import API_token
# from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

# bot = TeleBot(API_token)

# # user_ID = []

# # button1 = InlineKeyboardButton(text='button1',callback_data='btn1')
# # button1 = InlineKeyboardButton(text='button1',callback_data='btn1')
# button1 = InlineKeyboardButton(text='button1', url='https://codeyad.com')
# button2 = InlineKeyboardButton(text='button2', url='https://google.com')
# inline_keyboard = InlineKeyboardMarkup(row_width=1)
# inline_keyboard.add(button1,button2) 

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.send_message(message.chat.id, "Welcome to Arshia's Bot", reply_markup=inline_keyboard)
#     # if message.chat.id not in user_ID:
#     #     user_ID.append(message.chat.id)
        
# # @bot.callback_query_handler(func = lambda call:True)
# # def check_button(call):
# #     if call.data == 'btn1':
# #         bot.answer_callback_query(call.id, 'cose bibit', show_alert=True)
# #     elif call.data == 'btn2':
# #         bot.answer_callback_query(call.id, 'cose amat')
# #     else:
# #         print('ridi')
        
        
# # @bot.message_handler(commands=['SUPU'])
# # def send_update(message):
# #     # for id in user_ID:
# #         bot.send_message(id, "The product is available")
           
        
# bot.polling()