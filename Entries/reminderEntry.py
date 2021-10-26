# TODO: Add date parsing for console interaction

class ReminderEntry:
	def __init__(self, content="", date=""):
		self.content = content
		self.date = date

	def FromRow(self, row):
		self.content = row[0]
		self.date = row[1]

	def __str__(self):
		return f'{self.content}, {str(self.date)}'

	def Format(self):
		return f'INSERT INTO REMINDERS(message, datetime) VALUES (\"{self.content}\", \"{str(self.date)}\")'