class Entry:
	def __init__(self, content="", date=""):
		self.content = content
		self.date = date

	def FromRow(self, row):
		self.content = row[0]
		self.date = row[1]

	def __str__(self):
		return f'{self.FormatDate()}\n{self.content}'

	def Format(self):
		return f'INSERT INTO ENTRIES(message, datetime) VALUES (\"{self.content}\", \"{str(self.date)}\")'

	def FormatDate(self):
		return str(self.date).split('.')[0]