from db import database

class Home(database.Model):
	__tablename__ = 'home'

	id = database.Column(database.Integer, primary_key=True)
	welcome = database.Column(database.String(500))
	activities = database.Column(database.String(500))
	contact = database.Column(database.String(500))
	description = database.Column(database.String(500))

	def __repr__(self):
		return '<Home {}>'.format(self.welcome)

class Blog(database.Model):
	__tablename__ = 'blog'

	id = database.Column(database.Integer, primary_key=True)
	category = database.Column(database.String(500))
	title = database.Column(database.String(500))
	content = database.Column(database.String(500))
	created_date = database.Column(database.Date)

	#create new database 
	def __init__ (self, category, title, content):
		self.category = category
		self.title = title
		self.content = content

	def __repr__(self):
		return '<Blog {}>'.format(self.category)
