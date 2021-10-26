import sqlite3
import os
from Entries.entry import Entry
from Entries.todoEntry import TodoEntry


# OK, ROWID will work, use that instead of ID
# TODO: Actually, don't be stupid, just pull all todos and when one is
#  removed update all the rest by rowid to maintain list
#  So have rows in memory, when one is removed update the DB with new indicies
#  OR BETTER YET don't use rowid at all but instead use the datetime that's already there
#  and just use indicies in the program alone, leave the DB to it's devices

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
		for i in self.cur.execute('SELECT * FROM ENTRIES ORDER BY datetime DESC LIMIT 1;'):
			entry.FromRow(i)
			break
		return entry

	def GetTODOs(self):
		todos = []
		for i in self.cur.execute('SELECT message, datetime, ROWID FROM TODO ORDER BY ROWID ASC;'):
			entry = TodoEntry()
			entry.FromRow(i)
			todos.append(entry)
		return todos

	def RemoveRow(self, table, rowID):
		self.cur.execute(f'DELETE FROM {table.upper()} WHERE ROWID={rowID};')
		self.con.commit()