import telebot
import datetime
from name import *
import threading
import work_with_json
bot = telebot.TeleBot(name)


@bot.message_handler(commands=['start', 'info'])
def welcom(message):
    markap = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_1 = telebot.types.KeyboardButton('Гит аккаунты')
    item_2 = telebot.types.KeyboardButton('Как я работаю')
    item_3 = telebot.types.KeyboardButton("Как быстро развернуть бота")
    item_4 = telebot.types.KeyboardButton("Задать таймер для себя")
    item_5 = telebot.types.KeyboardButton("Оповестить подпольный чат и в лс")
    item_6 = telebot.types.KeyboardButton("Подписаться/отписаться от уведомлений")
    markap.add(item_1, item_2, item_3, item_4, item_6, item_5)
    log_write(message)
    print(message.chat.type)
    if message.chat.type == "private":
        text_mes = f'Еще раз привет, вот немного инфы про наш чат\n\n{tegi}\n{mih}\n{dis}\n{opesh}\n{chats}'
        bot.send_message(message.chat.id, text_mes, parse_mode='html', reply_markup=markap)
    else: bot.send_message(message.chat.id, f"все вопросы в боте, <a>t.me/noob_b_help_bot</a>", parse_mode='html')

@bot.message_handler(content_types=['new_chat_members'])
def new_member(message):
    log_write(message)
    bot.reply_to(message, f"Приветствуем тебя <b>{message.from_user.first_name}</b> в нашем чате) Здесь все направления поток от 20.08.", parse_mode='html')
    bot.send_message(message.chat.id, f"Много полезной инфы в нашем боте, жми на ссылку: , <a>t.me/noob_b_help_bot</a>", parse_mode='html')

@bot.message_handler(content_types=['text'])
def send_text(message):
    log_write(message)
    if message.chat.type == "private":
        if message.text == 'Гит аккаунты':
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG-qJjppoGmF29ULqzTxEE5JkRCi0kxQACuyMAAugDeUhba5weOQLDwiwE')
            bot.send_message(message.chat.id, git, parse_mode='html')

        elif message.text == 'Как я работаю':
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEG-qhjppoOSjtdGSZX62STpfpSy-njmQACSCAAAmCgeEhJxcQ5asECiiwE')
            bot.send_message(message.chat.id, 'Вот ссылка на гит где я живу <a>https://github.com/makaroch/dot_underground_chat.git</a>', parse_mode='html')

        elif message.text == "Как быстро развернуть бота":
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEHAAF2Y6iJ02z_5_CkAAG2wH9LJ02VGuiaAAJ-HwACcFd4SJGOadUnYK2ULAQ')
            bot.send_message(message.chat.id, f"Вот ссылочка с видосом по которому развернули меня: <a>https://www.youtube.com/watch?v=INcuG3R5KDw</a>", parse_mode='html')

        elif message.text == "Задать таймер для себя":
            bot.send_message(message.chat.id, 'Что будем запоминать? Если нужно отменить установку напиши "стоп"(введенная фраза выведитcя целиком)')
            bot.register_next_step_handler(message, get_alert)

        elif message.text == "Подписаться/отписаться от уведомлений":
            result = work_with_json.on_of_alert(message.chat.id)
            if result:
                bot.send_message(message.chat.id, "Готово, вы подписанны на рассылку, теперь бот будет писать в лс.")
            else: bot.send_message(message.chat.id, "Готово, вы отписаны бот больше не будет писать в лс.")

        elif message.text == "Оповестить подпольный чат и в лс":
            if (message.from_user.username == "ek_Alexey") or (message.from_user.username == "justwind14"):
                bot.send_message(message.chat.id, 'Что будем запоминать? Если нужно отменить установку напиши "стоп".(введенная фраза выведитcя целиком)')
                bot.register_next_step_handler(message, get_alert_mod)
            else:
                bot.send_message(message.chat.id, f"Сори бро эта опция доступна только Михаилу( @justwind14 )")

        else:
            bot.send_message(message.chat.id, "Солнце, давай покачто по кнопочкам пж)")


user_dikt = {}

def get_alert_mod(message):
    if message.text == "стоп":
        bot.send_message(message.chat.id, "Установка таймера отменена")
        return
    user_dikt[podpoln] = [message.text]
    bot.send_message(message.chat.id, f'Запомнил, {message.chat.first_name}, через сколько минут напомнить? Если нужно отменить установку напиши "стоп"')
    bot.register_next_step_handler(message, get_time_mod)

def get_time_mod(message):
    if message.text == "стоп":
        bot.send_message(message.chat.id, "Установка таймера отменена")
        return
    user_dikt[podpoln].append(message.text)
    while message.text.isdigit() != True:
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста 😉')
        bot.register_next_step_handler(message, get_time)
        user_dikt[message.chat.id].pop()
        break
    else:
        print(user_dikt)
        chat_id = podpoln # эти 2 переменные чинят баг описанный ниже
        text = user_dikt[chat_id][0]

        def say_alert():
            chat_id_list = work_with_json.take_user_id()
            for chat_id_json in chat_id_list:
                bot.send_message(chat_id_json, f'НАПОМИНАЮ: {text}')# баг если кидать нескоько таймеров с одного id и указывать няпрямую
                                                        #  bot.send_message(message.chat.id, f'НАПОМИНАЙ: {user_dikt[message.chat.id][0]}')

                                                        # alert в словаре перетирается последним и выводится не то сообщение
        bot.send_message(message.chat.id, "Принято")
        timer = threading.Timer(int(user_dikt[chat_id][1]) * 60, say_alert)
        timer.start()

def get_alert(message):
    if message.text == "стоп":
        bot.send_message(message.chat.id, "Установка таймера отменена" )
        return
    user_dikt[message.chat.id] = [message.text]
    bot.send_message(message.chat.id, f'Запомнил, {message.chat.first_name}, через сколько минут напомнить? Если нужно отменить установку напиши "стоп"')
    bot.register_next_step_handler(message, get_time)

def get_time(message):
    if message.text == "стоп":
        bot.send_message(message.chat.id, "Установка таймера отменена")
        return
    user_dikt[message.chat.id].append(message.text)
    while message.text.isdigit() != True:
        bot.send_message(message.chat.id, 'Цифрами, пожалуйста 😉')
        bot.register_next_step_handler(message, get_time)
        user_dikt[message.chat.id].pop()
        break
    else:
        print(user_dikt)
        chat_id = message.chat.id # эти 2 переменные чинят баг описанный ниже
        text = user_dikt[message.chat.id][0]

        def say_alert():
            bot.send_message(chat_id, f'НАПОМИНАЮ: {text}')# баг если кидать нескоько таймеров с одного id и указывать няпрямую
                                                        #  bot.send_message(message.chat.id, f'НАПОМИНАЙ: {user_dikt[message.chat.id][0]}')
                                                        # alert в словаре перетирается последним и выводится не то сообщение

        bot.send_message(message.chat.id, "Принято")
        timer = threading.Timer(int(user_dikt[message.chat.id][1]) * 60, say_alert)
        timer.start()


def log_write(message):
    today = datetime.datetime.today()
    time = today.strftime("%Y-%m-%d-%H.%M.%S")  # 2017-04-05-00.18.00
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(f'в {time} пользователь {message.from_user.first_name} с id {message.chat.id} и username {message.from_user.username}  сказал: {message.text}\n')



bot.infinity_polling()
#bot.polling(non_stop=True)