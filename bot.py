import telebot
from name import *

bot = telebot.TeleBot(name)

'''
chat.type покажет, где находится данное сообщение. В private, group, supergroup или channel.
Поделиться
'''

@bot.message_handler(commands=['start', 'info'])
def welcom(message):
  markap = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
  item_1 = telebot.types.KeyboardButton('Гит аккаунты')
  item_2 = telebot.types.KeyboardButton('Как я работаю')
  markap.add(item_1, item_2)
  print(message.from_user.first_name)
  print(message.chat.type)
  if message.chat.type == "private":
    text_mes = f'Еще раз привет, вот немного инфы про наш чат\n\n{tegi}\n{mih}\n{dis}\n{opesh}\n{chats}'
    bot.send_message(message.chat.id, text_mes, parse_mode='html', reply_markup=markap)
  else: bot.send_message(message.chat.id, f"все вопросы в боте, <a>t.me/noob_b_help_bot</a>", parse_mode='html')


@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
  print(message.from_user.first_name)
  bot.reply_to(message, f"Приветствуем тебя в нашем чате) Здесь все направления поток от 20.08. <b>{message.from_user.first_name}</b>.", parse_mode='html')
  bot.send_message(message.chat.id, f"Много полезной инфы в нашем боте, жми на ссылку: , <a>t.me/noob_b_help_bot</a>", parse_mode='html')


@bot.message_handler(content_types=['text'])
def send_text(message):
  print(message.from_user.first_name)
  if message.chat.type == "private":
    if message.text == 'Гит аккаунты':
      bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG-qJjppoGmF29ULqzTxEE5JkRCi0kxQACuyMAAugDeUhba5weOQLDwiwE')
      bot.send_message(message.chat.id, git, parse_mode='html')
    if message.text == 'Как я работаю':
      bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG-qhjppoOSjtdGSZX62STpfpSy-njmQACSCAAAmCgeEhJxcQ5asECiiwE')
      bot.send_message(message.chat.id, 'Вот ссылка на гит где я живу <a></a>', parse_mode='html')






bot.polling(non_stop=True)