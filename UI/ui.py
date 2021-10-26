import threading
import winsound

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
	def __init__(self, interface):
		self.app = QApplication(sys.argv)
		self.window = MainWindow()
		self.window.setWindowOpacity(0.85)

		self.interface = interface

		self.window.setWindowFlags(
			self.window.windowFlags() | QtCore.Qt.FramelessWindowHint)

		self.window.ui.currentEntry.textChanged.connect(self.EntryChanged)
		self.window.ui.console.textChanged.connect(self.ConsoleChanged)

		# Open window and focus entry
		keyboard.add_hotkey('alt+page down', self.OpenEntry,
							suppress=True,
							timeout=0)
		# Open window and focus console
		keyboard.add_hotkey('ctrl+page down', self.OpenConsole,
							suppress=True,
							timeout=0)
		# Close window
		keyboard.add_hotkey('shift+page down', self.HideWindow,
							suppress=True,
							timeout=0)

		self.CenterOnScreen()
		self.window.show()

	def Start(self):
		sys.exit(self.app.exec())

	def ShowWindow(self):
		self.interface.beeper.StopBeeping()
		if not self.window.isVisible():
			threading.Thread(target=winsound.Beep, args=(1200, 500,)).start()
			self.window.show()
			self.window.activateWindow()

	def HideWindow(self):
		self.interface.beeper.StopBeeping()
		if self.window.isVisible():
			threading.Thread(target=winsound.Beep, args=(800, 500,)).start()
			self.window.hide()

	def OpenEntry(self):
		self.interface.beeper.StopBeeping()
		self.ShowWindow()
		self.window.ui.currentEntry.setFocus()

	def OpenConsole(self):
		self.interface.beeper.StopBeeping()
		self.ShowWindow()
		self.window.ui.console.setFocus()

	def EntryChanged(self):
		text = self.window.ui.currentEntry.toPlainText()

		self.SetMarkdown(self.window.ui.markdownPreview, text)

		try:
			if 'ff' in text[-3:]:
				self.interface.EntrySubmit(text[:-4])
		except IndexError: pass

	def ConsoleChanged(self):
		text = self.window.ui.console.toPlainText()
		try:
			if 'ff' in text[-3:]:
				self.interface.ConsoleSubmit(text[:-3])
		except IndexError: pass

	def CenterOnScreen(self):
		height = 1080
		width = 1920
		x = (width - self.window.width()) / 2.0
		y = (height - self.window.height()) / 2.0
		self.window.setGeometry(int(x), int(y),
								self.window.width(),
								self.window.height())

	def SetMarkdown(self, widget, text):
		widget.setMarkdown(text)
