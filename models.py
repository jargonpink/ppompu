from app import db
from datetime import datetime

class Post(db.Model):
	__tablename__ = 'posts'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	content = db.Column(db.Text)
	link = db.Column(db.String(200))
	created_at = db.Column(db.DateTime, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

if __name__ == "__main__":
	db.create_all()
