import telebot
from telebot import types
import time

count_of_str = 0
count = 0

num_of_photo_for_constr = 0
num_of_photo_for_mainten = 0
num_of_photo_for_test = 0
num_of_photo_for_deliv = 0
num_of_photo_for_desi = 0
num_of_photo_for_manuf = 0

num_of_vid_for_constr = 0
num_of_vid_for_mainten = 0
num_of_vid_for_test = 0
num_of_vid_for_deliv = 0
num_of_vid_for_desi = 0
num_of_vid_for_manuf = 0

num_of_voice_for_constr = 0
num_of_voice_for_mainten = 0
num_of_voice_for_test = 0
num_of_voice_for_deliv = 0
num_of_voice_for_desi = 0
num_of_voice_for_manuf = 0

gol_for_instr_const = 0
gol_for_instr_deliv = 0
gol_for_instr_desi = 0
gol_for_instr_maint = 0
gol_for_instr_manuf = 0
gol_for_instr_test = 0

bot = telebot.TeleBot('7081223543:AAFRPiWxB6IHMZawTxKBc-PsUQIi5MPMY5M')


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    inline_markup = types.InlineKeyboardMarkup()
    btn1 = types.KeyboardButton('Список инструкций')
    btn2 = types.KeyboardButton('Оставить ответ на инструкцию')
    btn3 = types.KeyboardButton('Прочитать инструкции')
    btn4 = types.KeyboardButton('Голосовать за инструкцию')
    btn6 = types.KeyboardButton('Посмотреть голоса за инструкции')
    btn5 = types.KeyboardButton('Просмотреть ответы на инструкцию')
    btn_in_line = types.InlineKeyboardButton('Получить ссылку на полезную статью', url='https://cyberleninka.ru/article/n/sovremennye-podhody-k-sozdaniyu-novogo-produkta-v-mashinostroenii/viewer')
    markup.add(btn1, btn3, btn2, btn4, btn5, btn6)
    inline_markup.add(btn_in_line)
    mess = f'Привет, {message.from_user.first_name}. Я - Кот - Завод. Я - главный по инструкциям. Для твоего удобства я добавил тебе клавиатуру.'
    photo = open('старт.jfif', 'rb')
    bot.send_photo(message.chat.id, photo, caption=mess, reply_markup=markup)
    bot.send_message(message.chat.id, text='Что ты можешь сделать: \n\n- Прочитать инструкции. \n\n- Оставить ответ на инструкцию - для этого используйте кнопку со смайликом 📝 в разделе добавить ответ на инструкцию. \n\n- Просмотреть все заметки об инструкциях - для этого используйте кнопку со смайликом 📖 в разделе прочитать ответы на инструкцию. \n\n- Посмотреть список инструкций. \n\n- Ты можешь проголосовать за лучшую на твой взгляд инструкцию, а затем просмотреть голоса за все инструкции в соответсвующих кнопках.', reply_markup=inline_markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, text='Вот теги, по которым ты можешь передвигаться: '
                                           '\n#Проектирование '
                                           '\n#Изготовление_деталей '
                                           '\n#Сборка '
                                           '\n#Тестирование '
                                           '\n#Отправка '
                                           '\n#Обслуживание_и_ремонт')

@bot.message_handler(content_types=["text"])
def func(message):
    global count_of_str
    global gol_for_instr_const, gol_for_instr_deliv, gol_for_instr_desi, gol_for_instr_maint, gol_for_instr_manuf, gol_for_instr_test

    us = message.text.split(':')
    print(us)

    if message.text == 'Прочитать инструкции':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Сборка')
        btn2 = types.KeyboardButton('Проектирование')
        btn3 = types.KeyboardButton('Изготовление деталей')
        btn4 = types.KeyboardButton('Тестирование')
        btn5 = types.KeyboardButton('Отправка')
        btn6 = types.KeyboardButton('Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для чтения', reply_markup=markup)

    if message.text == 'Сборка' or message.text == 'сборка':
        with open('Instructions_to_construct.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            photo1 = open('Сборка12.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1, caption=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Отправка' or message.text == 'отправка':
        with open('Instructions_to_delivery.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            photo1 = open('Отправка.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1, caption=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Проектирование' or message.text == 'проектирование':
        with open('Instructions_to_designing.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            photo1 = open('проектирование.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1, caption=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Изготовление деталей' or message.text == 'изготовление деталей':
        with open('Instructions_to_manufacturing_of_parts.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            photo1 = open('сборка (4).jpg', 'rb')
            bot.send_photo(message.chat.id, photo1, caption=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Тестирование' or message.text == 'тестирование':
        with open('Instructions_to_testing.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            photo1 = open('тестирование.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1, caption=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Обслуживание и ремонт' or message.text == 'обслуживание и ремонт':
        with open('Instructions_to_maintenance_and_repair.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            photo1 = open('обслуживание и ремонт.jpg', 'rb')
            bot.send_photo(message.chat.id, photo1, caption=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Список инструкций':
        with open('All_instructions_visible.txt', 'r', encoding='UTF-8') as file:
            visible = file.read()
            bot.send_message(message.chat.id, text=visible)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)


    if message.text == 'Посмотреть голоса за инструкции':
        bot.send_message(message.chat.id, text=f'Голоса за инструкцию "Сборка" - {gol_for_instr_const}\nГолоса за инструкцию "Отправка" - {gol_for_instr_deliv}\nГолоса за инструкцию "Обслуживание и ремонт" - {gol_for_instr_maint}\nГолоса за инструкцию "Изготовление деталей" - {gol_for_instr_manuf}\nГолоса за инструкцию "Тестировка" - {gol_for_instr_test}\nГолоса за инструкцию "Проектирование" - {gol_for_instr_desi}')

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Голосовать за инструкцию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('✋Сборка')
        btn2 = types.KeyboardButton('✋Отправка')
        btn3 = types.KeyboardButton('✋Обслуживание и ремонт')
        btn4 = types.KeyboardButton('✋Изготовление деталей')
        btn5 = types.KeyboardButton('✋Тестирование')
        btn6 = types.KeyboardButton('✋Проектирование')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn3, btn2, btn4, btn5, btn6, btn)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)

    if message.text == '✋Сборка':
        gol_for_instr_const += 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Ваш голос учтён, возвращайтесь в меню', reply_markup=markup)

    if message.text == '✋Отправка':
        gol_for_instr_deliv += 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Ваш голос учтён, возвращайтесь в меню', reply_markup=markup)

    if message.text == '✋Обслуживание и ремонт':
        gol_for_instr_maint += 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Ваш голос учтён, возвращайтесь в меню', reply_markup=markup)

    if message.text == '✋Изготовление деталей':
        gol_for_instr_manuf += 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Ваш голос учтён, возвращайтесь в меню', reply_markup=markup)

    if message.text == '✋Тестирование':
        gol_for_instr_test += 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Ваш голос учтён, возвращайтесь в меню', reply_markup=markup)

    if message.text == '✋Проектирование':
        gol_for_instr_desi += 1

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='Ваш голос учтён, возвращайтесь в меню', reply_markup=markup)

    if (message.text == 'Оставить ответ на инструкцию'):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Оставить ответ на инструкцию в виде текста')
        btn2 = types.KeyboardButton('Оставить ответ на инструкцию в виде фото')
        btn3 = types.KeyboardButton('Оставить ответ на инструкцию в виде голосового сообщения')
        btn4 = types.KeyboardButton('Оставить ответ на инструкцию в виде видео')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для ответа', reply_markup=markup)

    if message.text == 'Оставить ответ на инструкцию в виде видео':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🎬Сборка')
        btn2 = types.KeyboardButton('🎬Проектирование')
        btn3 = types.KeyboardButton('🎬Изготовление деталей')
        btn4 = types.KeyboardButton('🎬Тестирование')
        btn5 = types.KeyboardButton('🎬Отправка')
        btn6 = types.KeyboardButton('🎬Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для ответа', reply_markup=markup)

    if message.text == '🎬Сборка':

        bot.send_message(message.chat.id, 'Отправьте видео на инструкцию под названием "Сборка"')
        bot.register_next_step_handler(message, handle_video_for_constr)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🎬Проектирование':

        bot.send_message(message.chat.id, 'Отправьте видео на инструкцию под названием "Проектирование"')
        bot.register_next_step_handler(message, handle_video_for_desi)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🎬Изготовление деталей':

        bot.send_message(message.chat.id, 'Отправьте видео на инструкцию под названием "Изготовление деталей"')
        bot.register_next_step_handler(message, handle_video_for_manuf)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🎬Тестирование':

        bot.send_message(message.chat.id, 'Отправьте видео на инструкцию под названием "Тестирование"')
        bot.register_next_step_handler(message, handle_video_for_test)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🎬Отправка':

        bot.send_message(message.chat.id, 'Отправьте видео на инструкцию под названием "Отправка"')
        bot.register_next_step_handler(message, handle_video_for_deliv)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🎬Обслуживание и ремонт':

        bot.send_message(message.chat.id, 'Отправьте видео на инструкцию под названием "Обслуживание и ремонт"')
        bot.register_next_step_handler(message, handle_video_for_mainten)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Оставить ответ на инструкцию в виде голосового сообщения':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔊Сборка')
        btn2 = types.KeyboardButton('🔊Проектирование')
        btn3 = types.KeyboardButton('🔊Изготовление деталей')
        btn4 = types.KeyboardButton('🔊Тестирование')
        btn5 = types.KeyboardButton('🔊Отправка')
        btn6 = types.KeyboardButton('🔊Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для ответа', reply_markup=markup)

    if message.text == '🔊Сборка':

        bot.send_message(message.chat.id, 'Отправьте голосовое сообщение на инструкцию под названием "Сборка"')
        bot.register_next_step_handler(message, handle_voice_message_for_constr)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🔊Проектирование':

        bot.send_message(message.chat.id, 'Отправьте голосовое сообщение на инструкцию под названием "Проектирование"')
        bot.register_next_step_handler(message, handle_voice_message_for_desi)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🔊Изготовление деталей':

        bot.send_message(message.chat.id, 'Отправьте голосовое сообщение на инструкцию под названием "Изготовление деталей"')
        bot.register_next_step_handler(message, handle_voice_message_for_manuf)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🔊Тестирование':

        bot.send_message(message.chat.id, 'Отправьте голосовое сообщение на инструкцию под названием "Тестирование"')
        bot.register_next_step_handler(message, handle_voice_message_for_test)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🔊Отправка':

        bot.send_message(message.chat.id, 'Отправьте голосовое сообщение на инструкцию под названием "Отправка"')
        bot.register_next_step_handler(message, handle_voice_message_for_deliv)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '🔊Обслуживание и ремонт':

        bot.send_message(message.chat.id, 'Отправьте голосовое сообщение на инструкцию под названием "Обслуживание и ремонт"')
        bot.register_next_step_handler(message, handle_voice_message_for_mainten)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Оставить ответ на инструкцию в виде текста':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📝Сборка')
        btn2 = types.KeyboardButton('📝Проектирование')
        btn3 = types.KeyboardButton('📝Изготовление деталей')
        btn4 = types.KeyboardButton('📝Тестирование')
        btn5 = types.KeyboardButton('📝Отправка')
        btn6 = types.KeyboardButton('📝Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для ответа', reply_markup=markup)

    if message.text == '📝Сборка':

        bot.send_message(message.chat.id, 'Введите ответ на инструкцию под названием "Сборка"')
        bot.register_next_step_handler(message, save_answers_to_instr_construct)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📝Проектирование':

        bot.send_message(message.chat.id, 'Введите ответ на инструкцию под названием "Проектирование"')
        bot.register_next_step_handler(message, save_answers_to_instr_designing)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📝Изготовление деталей':

        bot.send_message(message.chat.id, 'Введите ответ на инструкцию под названием "Изготовление деталей"')
        bot.register_next_step_handler(message, save_answers_to_instr_manufacturing_of_parts)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📝Тестирование':

        bot.send_message(message.chat.id, 'Введите ответ на инструкцию под названием "Тестирование"')
        bot.register_next_step_handler(message, save_answers_to_instr_testing)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📝Отправка':

        bot.send_message(message.chat.id, 'Введите ответ на инструкцию под названием "Отправка"')
        bot.register_next_step_handler(message, save_answers_to_instr_delivery)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📝Обслуживание и ремонт':

        bot.send_message(message.chat.id, 'Введите ответ на инструкцию под названием "Обслуживание и ремонт"')
        bot.register_next_step_handler(message, save_answers_to_instr_maintenance_and_repair)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Оставить ответ на инструкцию в виде фото':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📷Сборка')
        btn2 = types.KeyboardButton('📷Проектирование')
        btn3 = types.KeyboardButton('📷Изготовление деталей')
        btn4 = types.KeyboardButton('📷Тестирование')
        btn5 = types.KeyboardButton('📷Отправка')
        btn6 = types.KeyboardButton('📷Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для ответа', reply_markup=markup)

    if message.text == '📷Сборка':

        bot.send_message(message.chat.id, 'Отправьте фото на инструкцию под названием "Сборка"')
        bot.register_next_step_handler(message, handle_photo_for_constr)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📷Проектирование':

        bot.send_message(message.chat.id, 'Отправьте фото на инструкцию под названием "Проектирование"')
        bot.register_next_step_handler(message, handle_photo_for_desi)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📷Изготовление деталей':

        bot.send_message(message.chat.id, 'Отправьте фото на инструкцию под названием "Изготовление деталей"')
        bot.register_next_step_handler(message, handle_photo_for_manuf)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📷Тестирование':

        bot.send_message(message.chat.id, 'Отправьте фото на инструкцию под названием "Тестирование"')
        bot.register_next_step_handler(message, handle_photo_for_test)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📷Отправка':

        bot.send_message(message.chat.id, 'Отправьте фото на инструкцию под названием "Отправка"')
        bot.register_next_step_handler(message, handle_photo_for_deliv)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📷Обслуживание и ремонт':

        bot.send_message(message.chat.id, 'Отправьте фото на инструкцию под названием "Обслуживание и ремонт"')
        bot.register_next_step_handler(message, handle_photo_for_mainten)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Просмотреть ответы на инструкцию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Прочитать ответы на инструкцию')
        btn2 = types.KeyboardButton('Прослушать ответы на инструкцию')
        btn3 = types.KeyboardButton('Просмотреть фото-ответы на инструкцию')
        btn4 = types.KeyboardButton('Просмотреть видео-ответы на инструкцию')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn3, btn2, btn4, btn)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)

    if message.text == 'Прослушать ответы на инструкцию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📢Сборка')
        btn2 = types.KeyboardButton('📢Проектирование')
        btn3 = types.KeyboardButton('📢Изготовление деталей')
        btn4 = types.KeyboardButton('📢Тестирование')
        btn5 = types.KeyboardButton('📢Отправка')
        btn6 = types.KeyboardButton('📢Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для просмотра ответов', reply_markup=markup)

    if message.text == '📢Сборка':
        global num_of_voice_for_constr

        if num_of_voice_for_constr == 0:
            bot.send_message(message.chat.id, 'Здесь нет голосовых')
        elif num_of_voice_for_constr == 1:
            voise = open(f'voice_message_for_constr0.ogg', 'rb')
            bot.send_voice(message.chat.id, voise)
        else:
            for i in range(num_of_voice_for_constr):
                voise = open(f'voice_message_for_constr{i}.ogg', 'rb')
                bot.send_voice(message.chat.id, voise)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📢Проектирование':
        global num_of_voice_for_desi

        if num_of_voice_for_desi == 0:
            bot.send_message(message.chat.id, 'Здесь нет голосовых')
        elif num_of_voice_for_desi == 1:
            voise = open(f'voice_message_for_desi0.ogg', 'rb')
            bot.send_voice(message.chat.id, voise)
        else:
            for i in range(num_of_voice_for_desi):
                voise = open(f'voice_message_for_desi{i}.ogg', 'rb')
                bot.send_voice(message.chat.id, voise)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📢Обслуживание и ремонт':
        global num_of_voice_for_mainten

        if num_of_voice_for_mainten == 0:
            bot.send_message(message.chat.id, 'Здесь нет голосовых')
        elif num_of_voice_for_mainten == 1:
            voise = open(f'voice_message_for_mainten0.ogg', 'rb')
            bot.send_voice(message.chat.id, voise)
        else:
            for i in range(num_of_voice_for_mainten):
                voise = open(f'voice_message_for_mainten{i}.ogg', 'rb')
                bot.send_voice(message.chat.id, voise)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📢Изготовление деталей':
        global num_of_voice_for_manuf

        if num_of_voice_for_manuf == 0:
            bot.send_message(message.chat.id, 'Здесь нет голосовых')
        elif num_of_voice_for_manuf == 1:
            voise = open(f'voice_message_for_manuf0.ogg', 'rb')
            bot.send_voice(message.chat.id, voise)
        else:
            for i in range(num_of_voice_for_manuf):
                voise = open(f'voice_message_for_manuf{i}.ogg', 'rb')
                bot.send_voice(message.chat.id, voise)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📢Отправка':
        global num_of_voice_for_deliv

        if num_of_voice_for_deliv == 0:
            bot.send_message(message.chat.id, 'Здесь нет голосовых')
        elif num_of_voice_for_deliv == 1:
            voise = open(f'voice_message_for_deliv0.ogg', 'rb')
            bot.send_voice(message.chat.id, voise)
        else:
            for i in range(num_of_voice_for_deliv):
                voise = open(f'voice_message_for_deliv{i}.ogg', 'rb')
                bot.send_voice(message.chat.id, voise)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📢Тестирование':
        global num_of_voice_for_test

        if num_of_voice_for_test == 0:
            bot.send_message(message.chat.id, 'Здесь нет голосовых')
        elif num_of_voice_for_test == 1:
            voise = open(f'voice_message_for_test0.ogg', 'rb')
            bot.send_voice(message.chat.id, voise)
        else:
            for i in range(num_of_voice_for_test):
                voise = open(f'voice_message_for_test{i}.ogg', 'rb')
                bot.send_voice(message.chat.id, voise)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Просмотреть фото-ответы на инструкцию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('💾Сборка')
        btn2 = types.KeyboardButton('💾Проектирование')
        btn3 = types.KeyboardButton('💾Изготовление деталей')
        btn4 = types.KeyboardButton('💾Тестирование')
        btn5 = types.KeyboardButton('💾Отправка')
        btn6 = types.KeyboardButton('💾Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для просмотра ответов', reply_markup=markup)

    if message.text == '💾Сборка':
        global num_of_photo_for_constr

        if num_of_photo_for_constr == 0:
            bot.send_message(message.chat.id, 'Здесь нет фото')
        elif num_of_photo_for_constr == 1:
            photo = open(f'photo_for_constr0.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            for i in range(num_of_photo_for_constr):
                photo = open(f'photo_for_constr{i}.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '💾Проектирование':
        global num_of_photo_for_desi

        if num_of_photo_for_desi == 0:
            bot.send_message(message.chat.id, 'Здесь нет фото')
        elif num_of_photo_for_desi == 1:
            photo = open(f'photo_for_desi0.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            for i in range(num_of_photo_for_desi):
                photo = open(f'photo_for_desi{i}.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '💾Изготовление деталей':
        global num_of_photo_for_manuf

        if num_of_photo_for_manuf == 0:
            bot.send_message(message.chat.id, 'Здесь нет фото')
        elif num_of_photo_for_manuf == 1:
            photo = open(f'photo_for_manuf0.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            for i in range(num_of_photo_for_manuf):
                photo = open(f'photo_for_manuf{i}.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '💾Тестирование':
        global num_of_photo_for_test

        if num_of_photo_for_test == 0:
            bot.send_message(message.chat.id, 'Здесь нет фото')
        elif num_of_photo_for_test == 1:
            photo = open(f'photo_for_test0.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            for i in range(num_of_photo_for_test):
                photo = open(f'photo_for_test{i}.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '💾Отправка':
        global num_of_photo_for_deliv

        if num_of_photo_for_deliv == 0:
            bot.send_message(message.chat.id, 'Здесь нет фото')
        elif num_of_photo_for_deliv == 1:
            photo = open(f'photo_for_deliv0.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            for i in range(num_of_photo_for_deliv):
                photo = open(f'photo_for_deliv{i}.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '💾Обслуживание и ремонт':
        global num_of_photo_for_mainten

        if num_of_photo_for_mainten == 0:
            bot.send_message(message.chat.id, 'Здесь нет фото')
        elif num_of_photo_for_mainten == 1:
            photo = open(f'photo_for_mainten0.jpg', 'rb')
            bot.send_photo(message.chat.id, photo)
        else:
            for i in range(num_of_photo_for_mainten):
                photo = open(f'photo_for_mainten{i}.jpg', 'rb')
                bot.send_photo(message.chat.id, photo)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Прочитать ответы на инструкцию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📖Сборка')
        btn2 = types.KeyboardButton('📖Проектирование')
        btn3 = types.KeyboardButton('📖Изготовление деталей')
        btn4 = types.KeyboardButton('📖Тестирование')
        btn5 = types.KeyboardButton('📖Отправка')
        btn6 = types.KeyboardButton('📖Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для просмотра ответов', reply_markup=markup)

    if message.text == '📖Сборка':
        with open('Answers_to_construct.txt', 'r', encoding='UTF-8') as file:
            txt = file.read()
            bot.send_message(message.chat.id, text=txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📖Изготовление деталей':
        with open('Answers_to_manufacturing_of_parts.txt', 'r', encoding='UTF-8') as file:
            txt = file.read()
            bot.send_message(message.chat.id, text=txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📖Проектирование':
        with open('Answers_to_designing.txt', 'r', encoding='UTF-8') as file:
            txt = file.read()
            bot.send_message(message.chat.id, text=txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📖Тестирование':
        with open('Answers_to_testing.txt', 'r', encoding='UTF-8') as file:
            txt = file.read()
            bot.send_message(message.chat.id, text=txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📖Отправка':
        with open('Answers_to_delivery.txt', 'r', encoding='UTF-8') as file:
            txt = file.read()
            bot.send_message(message.chat.id, text=txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📖Обслуживание и ремонт':
        with open('Answers_to_maintenance_and_repair.txt', 'r', encoding='UTF-8') as file:
            txt = file.read()
            bot.send_message(message.chat.id, text=txt)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Просмотреть видео-ответы на инструкцию':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('📱Сборка')
        btn2 = types.KeyboardButton('📱Проектирование')
        btn3 = types.KeyboardButton('📱Изготовление деталей')
        btn4 = types.KeyboardButton('📱Тестирование')
        btn5 = types.KeyboardButton('📱Отправка')
        btn6 = types.KeyboardButton('📱Обслуживание и ремонт')
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn)
        bot.send_message(chat_id=message.chat.id, text='Выберете инструкцию для просмотра ответов', reply_markup=markup)

    if message.text == '📱Тестирование':
        global num_of_vid_for_test

        if num_of_vid_for_test == 0:
            bot.send_message(message.chat.id, 'Здесь нет видео')
        elif num_of_vid_for_test == 1:
            video = open(f'video_for_test0.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            for i in range(num_of_vid_for_test):
                video = open(f'video_for_test{i}.mp4', 'rb')
                bot.send_video(message.chat.id, video)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📱Проектирование':
        global num_of_vid_for_desi

        if num_of_vid_for_desi == 0:
            bot.send_message(message.chat.id, 'Здесь нет видео')
        elif num_of_vid_for_desi == 1:
            video = open(f'video_for_desi0.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            for i in range(num_of_vid_for_desi):
                video = open(f'video_for_desi{i}.mp4', 'rb')
                bot.send_video(message.chat.id, video)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📱Изготовление деталей':
        global num_of_vid_for_manuf

        if num_of_vid_for_manuf == 0:
            bot.send_message(message.chat.id, 'Здесь нет видео')
        elif num_of_vid_for_manuf == 1:
            video = open(f'video_for_manuf0.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            for i in range(num_of_vid_for_manuf):
                video = open(f'video_for_manuf{i}.mp4', 'rb')
                bot.send_video(message.chat.id, video)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📱Сборка':
        global num_of_vid_for_constr

        if num_of_vid_for_constr == 0:
            bot.send_message(message.chat.id, 'Здесь нет видео')
        elif num_of_vid_for_constr == 1:
            video = open(f'video_for_constr0.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            for i in range(num_of_vid_for_constr):
                video = open(f'video_for_constr{i}.mp4', 'rb')
                bot.send_video(message.chat.id, video)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📱Отправка':
        global num_of_vid_for_deliv

        if num_of_vid_for_deliv == 0:
            bot.send_message(message.chat.id, 'Здесь нет видео')
        elif num_of_vid_for_deliv == 1:
            video = open(f'video_for_deliv0.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            for i in range(num_of_vid_for_deliv):
                video = open(f'video_for_deliv{i}.mp4', 'rb')
                bot.send_video(message.chat.id, video)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == '📱Обслуживание и ремонт':
        global num_of_vid_for_mainten

        if num_of_vid_for_mainten == 0:
            bot.send_message(message.chat.id, 'Здесь нет видео')
        elif num_of_vid_for_mainten == 1:
            video = open(f'video_for_mainten0.mp4', 'rb')
            bot.send_video(message.chat.id, video)
        else:
            for i in range(num_of_vid_for_mainten):
                video = open(f'video_for_mainten{i}.mp4', 'rb')
                bot.send_video(message.chat.id, video)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('Вернуться в меню')
        markup.add(btn)
        bot.send_message(message.chat.id, text='После операции возвращайтесь в меню', reply_markup=markup)

    if message.text == 'Вернуться в меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Список инструкций')
        btn2 = types.KeyboardButton('Оставить ответ на инструкцию')
        btn3 = types.KeyboardButton('Прочитать инструкции')
        btn4 = types.KeyboardButton('Голосовать за инструкцию')
        btn6 = types.KeyboardButton('Посмотреть голоса за инструкции')
        btn5 = types.KeyboardButton('Просмотреть ответы на инструкцию')
        markup.add(btn1, btn3, btn2, btn4, btn5, btn6)
        bot.send_message(message.chat.id, text='Выберете действие', reply_markup=markup)

def handle_photo_for_deliv(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_photo_for_deliv
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'photo_for_deliv{num_of_photo_for_deliv}.jpg', 'wb') as file:
            file.write(downloaded_file)

        num_of_photo_for_deliv += 1
        bot.reply_to(message, 'Фотография сохранена. Спасибо!')

def handle_photo_for_desi(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_photo_for_desi
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'photo_for_desi{num_of_photo_for_desi}.jpg', 'wb') as file:
            file.write(downloaded_file)

        num_of_photo_for_desi += 1
        bot.reply_to(message, 'Фотография сохранена. Спасибо!')

def handle_photo_for_mainten(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_photo_for_mainten
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'photo_for_mainten{num_of_photo_for_mainten}.jpg', 'wb') as file:
            file.write(downloaded_file)

        num_of_photo_for_mainten += 1
        bot.reply_to(message, 'Фотография сохранена. Спасибо!')

def handle_photo_for_manuf(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_photo_for_manuf
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'photo_for_manuf{num_of_photo_for_manuf}.jpg', 'wb') as file:
            file.write(downloaded_file)

        num_of_photo_for_manuf += 1
        bot.reply_to(message, 'Фотография сохранена. Спасибо!')

def handle_photo_for_test(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_photo_for_test
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'photo_for_test{num_of_photo_for_test}.jpg', 'wb') as file:
            file.write(downloaded_file)

        num_of_photo_for_test += 1
        bot.reply_to(message, 'Фотография сохранена. Спасибо!')

def handle_photo_for_constr(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_photo_for_constr
        photo = message.photo[-1]
        file_info = bot.get_file(photo.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'photo_for_constr{num_of_photo_for_constr}.jpg', 'wb') as file:
            file.write(downloaded_file)

        num_of_photo_for_constr += 1
        bot.reply_to(message, 'Фотография сохранена. Спасибо!')

def handle_voice_message_for_test(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_voice_for_test
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'voice_message_for_test{num_of_voice_for_test}.ogg', 'wb') as file:
            file.write(downloaded_file)

        num_of_voice_for_test += 1
        bot.reply_to(message, "Голосовое сообщение сохранено. Спасибо!")

def handle_voice_message_for_desi(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_voice_for_desi
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'voice_message_for_desi{num_of_voice_for_desi}.ogg', 'wb') as file:
            file.write(downloaded_file)

        num_of_voice_for_desi += 1
        bot.reply_to(message, "Голосовое сообщение сохранено. Спасибо!")

def handle_voice_message_for_deliv(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_voice_for_deliv
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'voice_message_for_deliv{num_of_voice_for_deliv}.ogg', 'wb') as file:
            file.write(downloaded_file)

        num_of_voice_for_deliv += 1
        bot.reply_to(message, "Голосовое сообщение сохранено. Спасибо!")

def handle_voice_message_for_manuf(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_voice_for_manuf
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'voice_message_for_manuf{num_of_voice_for_manuf}.ogg', 'wb') as file:
            file.write(downloaded_file)

        num_of_voice_for_manuf += 1
        bot.reply_to(message, "Голосовое сообщение сохранено. Спасибо!")

def handle_voice_message_for_mainten(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_voice_for_mainten
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'voice_message_for_mainten{num_of_voice_for_mainten}.ogg', 'wb') as file:
            file.write(downloaded_file)

        num_of_voice_for_mainten += 1
        bot.reply_to(message, "Голосовое сообщение сохранено. Спасибо!")

def handle_voice_message_for_constr(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_voice_for_constr
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'voice_message_for_constr{num_of_voice_for_constr}.ogg', 'wb') as file:
            file.write(downloaded_file)

        num_of_voice_for_constr += 1
        bot.reply_to(message, "Голосовое сообщение сохранено. Спасибо!")

def handle_video_for_constr(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_vid_for_constr
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'video_for_constr{num_of_vid_for_constr}.mp4', 'wb') as file:
            file.write(downloaded_file)

        num_of_vid_for_constr += 1
        bot.reply_to(message, "Видео сохранено. Спасибо!")

def handle_video_for_deliv(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_vid_for_deliv
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'video_for_deliv{num_of_vid_for_deliv}.mp4', 'wb') as file:
            file.write(downloaded_file)

        num_of_vid_for_deliv += 1
        bot.reply_to(message, "Видео сохранено. Спасибо!")

def handle_video_for_desi(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_vid_for_desi
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'video_for_desi{num_of_vid_for_desi}.mp4', 'wb') as file:
            file.write(downloaded_file)

        num_of_vid_for_desi += 1
        bot.reply_to(message, "Видео сохранено. Спасибо!")

def handle_video_for_manuf(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_vid_for_manuf
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'video_for_manuf{num_of_vid_for_manuf}.mp4', 'wb') as file:
            file.write(downloaded_file)

        num_of_vid_for_manuf += 1
        bot.reply_to(message, "Видео сохранено. Спасибо!")

def handle_video_for_test(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_vid_for_test
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'video_for_test{num_of_vid_for_test}.mp4', 'wb') as file:
            file.write(downloaded_file)

        num_of_vid_for_test += 1
        bot.reply_to(message, "Видео сохранено. Спасибо!")

def handle_video_for_mainten(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        global num_of_vid_for_mainten
        file_info = bot.get_file(message.video.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'video_for_mainten{num_of_vid_for_mainten}.mp4', 'wb') as file:
            file.write(downloaded_file)

        num_of_vid_for_mainten += 1
        bot.reply_to(message, "Видео сохранено. Спасибо!")

def save_answers_to_instr_construct(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        with open('Answers_to_construct.txt', 'a', encoding='UTF-8') as file:
            file.write('\n' + message.text)
        bot.send_message(message.chat.id, "Ответ сохранен. Спасибо!")


def save_answers_to_instr_delivery(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        with open('Answers_to_delivery.txt', 'a', encoding='UTF-8') as file:
            file.write('\n' + message.text)
        bot.send_message(message.chat.id, "Ответ сохранен. Спасибо!")


def save_answers_to_instr_designing(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        with open('Answers_to_designing.txt', 'a', encoding='UTF-8') as file:
            file.write('\n' + message.text)
        bot.send_message(message.chat.id, "Ответ сохранен. Спасибо!")


def save_answers_to_instr_maintenance_and_repair(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        with open('Answers_to_maintenance_and_repair.txt', 'a', encoding='UTF-8') as file:
            file.write('\n' + message.text)
        bot.send_message(message.chat.id, "Ответ сохранен. Спасибо!")


def save_answers_to_instr_manufacturing_of_parts(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        with open('Answers_to_manufacturing_of_parts.txt', 'a', encoding='UTF-8') as file:
            file.write('\n' + message.text)
        bot.send_message(message.chat.id, "Ответ сохранен. Спасибо!")


def save_answers_to_instr_testing(message):
    if message.text == 'Вернуться в меню':
        return None
    else:
        with open('Answers_to_testing.txt', 'a', encoding='UTF-8') as file:
            file.write('\n' + message.text)
        bot.send_message(message.chat.id, "Ответ сохранен. Спасибо!")


def save_new_instruction(message):
    with open('All_instructions.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{message.text}:{time.time()}\n')

    sp = []
    with open('All_instructions.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            instruct, time_creation = line.strip().split(':')
            sp.append((instruct, time_creation))

    sp.sort(key=lambda ss: ss[1])
    with open('All_instructions.txt', 'r', encoding='UTF-8') as file:
        for count_of_lines, strin in enumerate(file):
            vf = count_of_lines
        C_o_L = count_of_lines + 1

    with open('All_instructions.txt', 'w', encoding='UTF-8') as file:
        for i in range(C_o_L):
            file.write(sp[i][0] + ':')
            file.write(sp[i][1] + '\n')

    with open('All_instructions_visible.txt', 'w', encoding='UTF-8') as file:
        for i in range(C_o_L):
            file.write(sp[i][0] + '\n')

    bot.send_message(message.chat.id, "Инструкция сохранена. Спасибо!")


bot.polling(none_stop=True)