#-*- coding: utf-8 -*-
import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup
import re


Base = declarative_base()
engine = create_engine('mysql://gojinn:thinkbig!@34@localhost/ppomppu');
Session = sessionmaker(bind=engine)
session = Session()

class Post(Base):
	__tablename__ = 'posts'

	id = Column(Integer, primary_key=True)
	title = Column(String(100))
	content = Column(Text)
	link = Column(String(200))
	created_at = Column(DateTime, default=datetime.datetime.utcnow)
	updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

Base.metadata.create_all(engine)

class Ppomppu:
	index_url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=phone'
	board_base_url = 'http://www.ppomppu.co.kr/zboard/'

	def main(self):
		for link in self.getPageLinks(self.index_url):
			post = self.postExtractor(link)
			print post['title']
			if session.query(Post.id).filter(Post.title==post['title'], Post.content==post['content']).count() > 0:
				print 'exists'
			else:
				print 'not exists'
				session.add(Post(**post))
				session.commit()

	def getPageLinks(self, url):
		links = []
		r = requests.get(url);
		s = BeautifulSoup(r.content)
		rows = s.find_all('tr', class_=re.compile("list[0-1]"));
	
		for row in rows:
			link = row.find('font', class_='list_title').parent['href']
			links.append(link)

		return links

	def postExtractor(self, url):
		url = self.board_base_url + url
		post = dict()
		r = requests.get(url);
		s = BeautifulSoup(r.content)

		post['link'] = url
		post['title'] = s.find('font', class_='view_title2').text
		post['content'] = ''

		for text in s.find_all('table', class_='pic_bg'):
			post['content'] += str(text)

		return post

if __name__ == "__main__":
	pp = Ppomppu()
	pp.main()

