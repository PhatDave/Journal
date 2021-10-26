import sqlite3
import os
from Entries.entry import Entry


# OK, ROWID will work, use that instead of ID

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
		for i in self.cur.execute('''SELECT * FROM ENTRIES ORDER BY datetime DESC LIMIT 1'''):
			entry.FromRow(i)
			break
		return entry