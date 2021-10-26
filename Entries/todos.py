class TODOS:
	def __init__(self, tlist, db=None):
		self.tlist = tlist
		self.db = db

	def RemoveEntry(self, index):
		index -= 1
		self.db.RemoveRow('TODO', self.tlist[index].ROWID)
		self.tlist.pop(index)

	def AddEntry(self, entry):
		self.tlist.append(entry)
		self.db.WriteEntry(entry)

	def __str__(self):
		output = ""
		for i, entry in enumerate(self.tlist):
			output += f'{i + 1}.\t{entry.content}\n'
		return output