import telebot
import schedule
import time
from random import randint

bot = telebot.TeleBot("1186453090:AAHzJtaYruWypR2Wwgg9WUzInvgcDv6y_bY")\

t = True
chat_id = -452045393

wishes_lis = ['Удачного дня🤗😊', 'Хорошей учебы👌', "Здоровья!)❤️", "Хорошо👌", "Принцесска❤️", "Доброго времени суток！👊😉", "Доброе утро принцесски❤️"]

#Понедельник
def send_мonday():
	global t
	ind = randint(0,6)
	if t == False:
	 	bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Понедельник):\n    1. Мат. анализ(4 этаж 65 кабинет)\n    2. История Украины(4 этаж 65 кабинет)\n    3. ООП на Java (6 этаж 9 кабинет)\n\n" + wishes_lis[ind])
	 	t = True
	else:
	 	bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Понедельник):\n    2. Вступ до фаху(10 этаж 2 кабинет)\n    3. ООП на Java (6 этаж 9 кабинет\n\n" + wishes_lis[ind])
	 	t = False

#Вторник
def send_tuesday():
	ind = randint(0,2)
	bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Вторник):\n    1. Мат. анализ (3 этаж 79 кабинет)\n    2.Физика(3 этаж 79 кабинет)\n\n" + wishes_lis[ind])

#Среда 
def send_wednesday():
	ind = randint(0,2)
	if t == False:
		bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Среда):\n    1. Дискретная математика (3 этаж 81 кабинет)\n    2. Английский (4 этаж 65 кабинет)\n    3. Лаб. по физике (3 этаж 35 кабинет)\n    4. Лаб. по физике (3 этаж 35 кабинет)\n\n" + wishes_lis[ind])
	else:
		bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Среда):\n    1. Дискретная математика (3 этаж 81 кабинет)\n    2. Английский (4 этаж 65 кабинет)\n    3. Лаб. по физике (3 этаж 35 кабинет)\n\n" + wishes_lis[ind])

#Четверг
def send_thursday():
	ind = randint(0,2)
	bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Четверг):\n    1. Физика(дист.)\n    2. Мат. анализ (дист.)\n\n" + wishes_lis[ind])

#Пятница
def send_friday():
	ind = randint(0,2)
	if t == False:
		bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Пятница):\n    1. ООП на Java (дист.)\n    2. История Украины (дист.)\n    3. Вступ до фаху (дист.)\n    4.Дискретная математика (дист.)\n\n" + wishes_lis[ind])
	else:
		bot.send_message(chat_id, "Доброе утро😊\n\nРасписание на сегодня(Пятница):\n    1. ООП на Java (дист.)\n    2. История Украины (дист.)\n    3. Вступ до фаху (дист.)\n    4.Мат. анализ (дист.)\n\n" + wishes_lis[ind])



schedule.every().monday.at("07:00").do(send_мonday)
schedule.every().wednesday.at("07:00").do(send_wednesday)
schedule.every().thursday.at("07:00").do(send_thursday)
schedule.every().friday.at("07:00").do(send_friday)
schedule.every().tuesday.at("07:00").do(send_tuesday)


while True:
	schedule.run_pending()
	time.sleep(1)