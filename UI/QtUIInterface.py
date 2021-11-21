import threading
import winsound

import Entries.DatetimeParser
from UI.ui import ui
from Entries.entry import Entry
from Entries.todoEntry import TodoEntry
from Entries.reminderEntry import ReminderEntry
import datetime


class UiInterface:
	def __init__(self, todos, reminders, db, beeper):
		self.ui = ui(self)
		self.todos = todos
		self.reminders = reminders
		self.db = db
		self.beeper = beeper
		self.datetimeParser = Entries.DatetimeParser.DatetimeParser()
		self.Refresh()

	def Start(self):
		self.ui.Start()

	def Refresh(self):
		self.SetTodoText(str(self.todos))
		self.SetReminderText(str(self.reminders))
		self.SetLastEntry(self.db.GetLastEntry())

	def ConsoleSubmit(self, text):
		threading.Thread(target=winsound.Beep, args=(800, 500,)).start()
		self.beeper.StopBeeping()
		if 'add' in text[:3]:
			text = text[4:]
			entry = TodoEntry(text, datetime.datetime.now())
			self.todos.AddEntry(entry)
		elif 'rem' in text[:3]:
			text = text[4:]
			self.todos.RemoveEntry(int(text))
		elif 'rmd' in text[:3]:
			if 'add' in text[4:7]:
				text = text[8:].split('|')
				entry = ReminderEntry()
				entry.date = self.datetimeParser.Parse(text[0].rstrip())
				if len(text) > 1:
					entry.content = text[1].rstrip()
				self.reminders.AddEntry(entry)
			elif 'rem' in text[4:7]:
				text = text[8:]
				self.reminders.RemoveEntry(int(text))
		self.Refresh()
		self.ClearConsole()

	def Show(self):
		self.ui.ShowWindow()

	def EntrySubmit(self, text):
		threading.Thread(target=winsound.Beep, args=(800, 500,)).start()
		self.beeper.StopBeeping()
		entry = Entry(text, datetime.datetime.now())
		self.db.WriteEntry(entry)
		self.ClearEntry()
		self.Refresh()
		self.ui.HideWindow()

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
