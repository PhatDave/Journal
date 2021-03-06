import datetime


class TodoEntry:
	def __init__(self, content="", date=""):
		self.content = content
		self.date = date
		self.ROWID = None

	def FromRow(self, row):
		self.content = row[0]
		self.date = datetime.datetime.strptime(row[1], '%Y-%m-%d %H:%M:%S.%f')
		self.ROWID = row[2]

	def __str__(self):
		return f'{self.content}, {str(self.date)}'

	def Format(self):
		return f'INSERT INTO TODO(message, datetime) VALUES (\"{self.content}\", \"{str(self.date)}\")'