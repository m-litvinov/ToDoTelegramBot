import requests
import misc
import json

token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'

def get_updates():
	url = URL + 'getupdates'
	r = requests.get(url)
	return r.json()

def get_message():
	data = get_updates()
	chat_id = data['result'][-1]['message']['chat']['id']
	message = data['result'][-1]['message']['text']

def read_task():
	with open("todolist.json", 'r', encoding='utf-8') as tasks:
		data = json.load(tasks)
	print(data)
	return data


def main():
	read_task()
	#d = get_updates()

	#with open('updates.json', 'w') as file:
	#	json.dump(d, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
	main()