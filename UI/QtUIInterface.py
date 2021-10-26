# TODO: Create interface for UI, access the UI through this interface
#   Expose only necessary methods
from UI.ui import ui


class UiInterface:
	def __init__(self):
		self.ui = ui(self)

	def Start(self):
		self.ui.Start()

	def ConsoleSubmit(self, text):
		pass

	def EntrySubmit(self, text):
		pass

	def SetTodoText(self, text):
		self.ui.window.ui.todo.setText(text)

	def SetReminderText(self, text):
		self.ui.window.ui.reminderList.setText(text)