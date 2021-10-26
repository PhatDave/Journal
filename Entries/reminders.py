class Reminders:
	def __init__(self, rlist, db=None):
		self.rlist = rlist
		self.db = db

	def RemoveEntry(self, index):
		index -= 1
		self.db.RemoveRow('REMINDERS', self.rlist[index].ROWID)

	def AddEntry(self, entry):
		self.rlist.append(entry)
		self.db.WriteEntry(entry)

	def __str__(self):
		output = ""
		for i, entry in enumerate(self.rlist):
			output += f'{i + 1}. {entry.FormatDate()} {entry.content}\n'
		return output