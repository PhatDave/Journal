import sqlite3
import os

from Entries.reminderEntry import ReminderEntry
from Entries.entry import Entry
from Entries.todoEntry import TodoEntry


class Database:
	def __init__(self):
		self.con = None
		self.cur = None
		self.ConnectDatabase()

	def ConnectDatabase(self):
		if os.path.isfile(f'.\\Database\\Database.db'):
			self.con = sqlite3.connect(f'.\\Database\\Database.db')
			self.cur = self.con.cursor()
		else:
			print("No database found!")
			quit()

		# Maybe automatically make database one day, don't bother for now
		# self.CreateDatabase()

	def WriteEntry(self, entry):
		self.cur.execute(entry.Format())
		self.con.commit()

	def GetLastEntry(self):
		entry = Entry()
		for i in self.cur.execute(
				'SELECT * FROM ENTRIES ORDER BY datetime DESC LIMIT 1;'):
			entry.FromRow(i)
			break
		return entry

	def GetTODOs(self):
		todos = []
		for i in self.cur.execute(
				'SELECT message, datetime, ROWID FROM TODO ORDER BY ROWID ASC;'):
			entry = TodoEntry()
			entry.FromRow(i)
			todos.append(entry)
		return todos

	def GetReminders(self):
		reminders = []
		for i in self.cur.execute(
				'SELECT message, datetime, ROWID FROM REMINDERS ORDER BY datetime ASC;'):
			entry = ReminderEntry()
			entry.FromRow(i)
			reminders.append(entry)
		return reminders

	def RemoveRow(self, table, rowID):
		self.cur.execute(
			f'DELETE FROM {table.upper()} WHERE ROWID={rowID};')
		self.con.commit()
