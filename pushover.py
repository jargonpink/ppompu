import requests
from config import *

class Pushover:

	def sendNotification(self, **kwargs):
		title = kwargs.get('title', 'empty title')
		message = kwargs.get('message', 'empty message')
		payload = {
			'token': PUSHOVER_API_KEY,
			'user': PUSHOVER_USER_KEY,
			'title': title,
			'message': message
		}

		r = requests.post(PUSHOVER_API_HOST, data=payload)

if __name__ == "__main__":
	pushover = Pushover()
	pushover.sendNotification()
