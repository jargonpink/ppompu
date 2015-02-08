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
			'message': message
		}

		if url:
			payload['url'] = url

		for userKey in PUSHOVER_USER_KEYS:
			payload['user'] = userKey

			r = requests.post(PUSHOVER_API_HOST, data=payload)

if __name__ == "__main__":
	pushover = Pushover()
	pushover.sendNotification()
