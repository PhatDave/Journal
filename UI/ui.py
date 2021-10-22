from UI.ui_mainwindow import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
import sys
import keyboard


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


class ui:
	def __init__(self):
		self.app = QApplication(sys.argv)
		self.window = MainWindow()
		self.window.setWindowOpacity(0.65)

		self.window.setWindowFlags(
			self.window.windowFlags() | QtCore.Qt.FramelessWindowHint)

		self.window.ui.currentEntry.textChanged.connect(self.EntryChanged)
		self.window.ui.currentEntry.returnPressed.connect(self.SubmitEntry)
		self.window.ui.console.returnPressed.connect(self.SubmitConsole)

		# Open window and focus entry
		keyboard.add_hotkey('alt+page down', self.OpenEntry,
							suppress=True, timeout=0)
		# Open window and focus console
		keyboard.add_hotkey('ctrl+page down', self.OpenConsole,
							suppress=True, timeout=0)
		# Close window
		keyboard.add_hotkey('shift+page down', self.HideWindow,
							suppress=True, timeout=0)

		self.CenterOnScreen()
		self.window.show()
		sys.exit(self.app.exec())

	def SubmitEntry(self):
		pass

	def SubmitConsole(self):
		pass

	def ShowWindow(self):
		self.window.show()
		self.window.activateWindow()

	def HideWindow(self):
		self.window.hide()

	def OpenEntry(self):
		self.ShowWindow()
		self.window.ui.currentEntry.setFocus()

	def OpenConsole(self):
		self.ShowWindow()
		self.window.ui.console.setFocus()

	def EntryChanged(self):
		self.SetText(self.window.ui.markdownPreview,
					 self.window.ui.currentEntry.toPlainText())

	def CenterOnScreen(self):
		height = 1080
		width = 1920
		x = (width - self.window.width()) / 2.0
		y = (height - self.window.height()) / 2.0
		self.window.setGeometry(int(x), int(y),
								self.window.width(),
								self.window.height())

	def SetText(self, widget, text):
		widget.setMarkdown(text)
