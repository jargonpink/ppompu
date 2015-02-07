from app import db
from datetime import datetime

class Post(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	content = db.Column(db.Text)
	link = db.Column(db.String(200))
	crawled_at = db.Column(db.DateTime, default=datetime.now)

if __name__ == "__main__":
	db.create_all()
