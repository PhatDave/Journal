# TODO: Create interface for UI, access the UI through this interface
#   Expose only necessary methods
import datetime

from UI.ui import ui
from Entries.entry import Entry


class UiInterface:
	def __init__(self, todos, reminders, db):
		self.ui = ui(self)
		self.db = db
		self.todos = todos
		self.reminders = reminders
		self.Refresh()

	def Start(self):
		self.ui.Start()

	def Refresh(self):
		self.SetTodoText(str(self.todos))
		self.SetReminderText(str(self.reminders))
		self.SetLastEntry(self.db.GetLastEntry())

	def ConsoleSubmit(self, text):
		pass

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