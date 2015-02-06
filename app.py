from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

@app.route("/")
def index():
	keyword = request.args.get('keyword', 'band')
	offset = 0
	limit = 100

	from models import Post
	posts = db.session.query(Post)\
			.filter(Post.content.like('%' + keyword + '%'))\
			.order_by(Post.created_at.desc())[offset:limit]

	return render_template("index.html", posts=posts, keyword=keyword)

if __name__ == "__main__":
	app.run()
