import requests
import misc
import io
from time import sleep

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'

#Создаем переменную для обновлений
global last_updat_id
last_update_id = 0

def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()

def get_message():
	#Получаем данные о последнем обновлении
	data = get_updates()
	last_object = data['result'][-1]
	current_update_id = last_object['update_id']
	#Сравниваем id последнего обновления с уже записанным, иначе не возвращаем ничего
	global last_update_id
	if last_update_id != current_update_id:
		last_update_id = current_update_id

		chat_id = last_object['message']['chat']['id']
		message_text = last_object['message']['text']

		message = {'chat_id': chat_id,
				   'text': message_text}
		return message
	return None

def send_message(chat_id, text='Wait a second, please...'):
	url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
	requests.get(url)

def main():
	while True:
		answer = get_message()

		if answer != None:
			chat_id = answer['chat_id']
			text = answer['text']
			if text == "Привет":
				send_message(chat_id, "И тебе привет")
		else:
			continue
		sleep(2)

if __name__ == '__main__':
	main()
