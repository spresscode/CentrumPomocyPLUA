#!/usr/bin/env python
# -*- coding: utf-8 -*-
import telebot

# Подтягиваем токен бота и все необходимое для получение средств за пиццу

# Создание бота
bot = telebot.TeleBot("5143195408:AAGrrSoZ4RzSe8vmk2GUoh87ERd5wafbvlU")

# Декоратор для обработки всех текстовых сообщений
@bot.message_handler(content_types=['text'])
def all_messages(msg):
    # Получаем сообщение пользователя
    message = msg.text

    # Получаем Telegram id пользователя (очевидно, для каждого пользователя он свой)
    user_id = msg.chat.id

    # Отправляем сообщение
    bot.send_message(user_id, f"Вы написали: {message}")

# Запускаем бота, чтобы работал 24/7
if __name__ == '__main__':
    bot.polling(none_stop=True)
