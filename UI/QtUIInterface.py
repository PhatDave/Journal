# TODO: Create interface for UI, access the UI through this interface
#   Expose only necessary methods
import datetime

import Entries.DatetimeParser
from UI.ui import ui
from Entries.entry import Entry
from Entries.todoEntry import TodoEntry
from Entries.reminderEntry import ReminderEntry
import datetime


# TODO: Now handle console...

class UiInterface:
	def __init__(self, todos, reminders, db):
		self.ui = ui(self)
		self.db = db
		self.todos = todos
		self.reminders = reminders
		self.datetimeParser = Entries.DatetimeParser.DatetimeParser()
		self.Refresh()

	def Start(self):
		self.ui.Start()

	def Refresh(self):
		self.SetTodoText(str(self.todos))
		self.SetReminderText(str(self.reminders))
		self.SetLastEntry(self.db.GetLastEntry())

	def ConsoleSubmit(self, text):
		if 'add' in text[:3]:
			text = text[4:]
			entry = TodoEntry(text, datetime.datetime.now())
			self.todos.AddEntry(entry)
			self.Refresh()
		elif 'rem' in text[:3]:
			text = text[4:]
			self.todos.RemoveEntry(int(text))
			self.Refresh()
		elif 'rmd' in text[:3]:
			if 'add' in text[4:7]:
				text = text[8:].split('|')
				entry = ReminderEntry()
				entry.date = self.datetimeParser.Parse(text[0].rstrip())
				if len(text) > 1:
					entry.content = text[1].rstrip()
				self.reminders.AddEntry(entry)
			elif 'rem' in text[4:7]:
				pass
			self.Refresh()
		self.ClearConsole()

	def EntrySubmit(self, text):
		entry = Entry(text, datetime.datetime.now())
		self.db.WriteEntry(entry)
		self.Refresh()

	def SetTodoText(self, text):
		self.ui.window.ui.todo.setText(text)

	def SetReminderText(self, text):
		self.ui.window.ui.reminderList.setText(text)

	def SetLastEntry(self, entry):
		self.ui.SetMarkdown(self.ui.window.ui.previousEntry, str(entry))

	def ClearEntry(self):
		self.ui.window.ui.currentEntry.setText("")

	def ClearConsole(self):
		self.ui.window.ui.console.setText("")
