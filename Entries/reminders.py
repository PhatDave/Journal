import datetime


class Reminders:
	def __init__(self, rlist, db=None):
		self.rlist = rlist
		self.db = db
		self.RemoveOutOfDate()

	def RemoveOutOfDate(self):
		toBeRemoved = []
		now = datetime.datetime.now()
		for i, item in enumerate(self.rlist):
			if item.date < now:
				# self.RemoveEntry(i)
				toBeRemoved.append(i)
		for i in toBeRemoved:
			self.RemoveEntry(i + 1)

	def RemoveEntry(self, index):
		index -= 1
		self.db.RemoveRow('REMINDERS', self.rlist[index].ROWID)
		self.rlist.pop(index)

	def AddEntry(self, entry):
		if entry.date > datetime.datetime.now():
			self.rlist.append(entry)
			self.rlist.sort(key=lambda x:x.date)
			self.db.WriteEntry(entry)

	def __str__(self):
		output = ""
		for i, entry in enumerate(self.rlist):
			output += f'{i + 1}.\t{entry.FormatDate()}\t{entry.content}\n'
		return output
