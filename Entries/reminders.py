class Reminders:
	# TODO: Check if any reminders are past due and remove them
	def __init__(self, rlist, db=None):
		self.rlist = rlist
		self.db = db

	def RemoveEntry(self, index):
		index -= 1
		self.db.RemoveRow('REMINDERS', self.rlist[index].ROWID)
		self.rlist.pop(index)

	def AddEntry(self, entry):
		self.rlist.append(entry)
		self.db.WriteEntry(entry)

	def __str__(self):
		output = ""
		for i, entry in enumerate(self.rlist):
			output += f'{i + 1}.\t{entry.FormatDate()}\t{entry.content}\n'
		return output