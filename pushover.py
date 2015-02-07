import requests
from config import *

class Pushover:

	def sendNotification(self, **kwargs):
		title = kwargs.get('title', 'empty title')
		message = kwargs.get('message', 'empty message')

		for userKey in PUSHOVER_USER_KEYS:
			payload = {
				'token': PUSHOVER_API_KEY,
				'user': userKey,
				'title': title,
				'message': message
			}

			r = requests.post(PUSHOVER_API_HOST, data=payload)

if __name__ == "__main__":
	pushover = Pushover()
	pushover.sendNotification()
