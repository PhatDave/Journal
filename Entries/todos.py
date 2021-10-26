class TODOS:
	def __init__(self, tlist):
		self.tlist = tlist
		self.db = None

	def RemoveEntry(self, index):
		index -= 1
		self.db.RemoveRow('TODO', self.tlist[index].ROWID)

	def AddEntry(self, entry):
		self.tlist.append(entry)
		self.db.WriteEntry(entry)

	def __str__(self):
		output = ""
		for i, entry in enumerate(self.tlist):
			output += f'{i + 1}. {entry.content}\n'
		return output