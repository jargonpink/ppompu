import requests
from config import *

class Pushover:

	def sendNotification(self, **kwargs):
		title = kwargs.get('title', 'empty title')
		message = kwargs.get('message', 'empty message')
		url = kwargs.get('url')

		payload = {
			'token': PUSHOVER_API_KEY,
			'title': title,
			'user': PUSHOVER_GROUP_KEY,
			'message': message
		}

		if url:
			payload['url'] = url

		r = requests.post(PUSHOVER_API_HOST, data=payload)

if __name__ == "__main__":
	pushover = Pushover()
	pushover.sendNotification()
