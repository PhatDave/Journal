import datetime
import threading
import time
from winsound import Beep

import keyboard


class Beeper:
	def __init__(self, reminders):
		self.reminders = reminders
		self.thread = threading.Thread(target=self.Run)
		self.beepThread = threading.Thread(target=self.Beep)
		self.beepSem = threading.Semaphore(0)
		self.isBeeping = False
		self.beepThread.start()

		# keyboard.add_hotkey('shift+ctrl+end', self.StartBeeping)

	def Start(self):
		self.thread.start()

	def Run(self):
		while True:
			try:
				if self.reminders.rlist[0].date <= datetime.datetime.now():
					self.StartBeeping()
			except IndexError: pass
			time.sleep(0.5)

	def Beep(self):
		while True:
			if self.isBeeping:
				Beep(1200, 500)
			else:
				self.beepSem.acquire()

	def StartBeeping(self):
		if not self.isBeeping:
			self.isBeeping = True
			self.beepSem.release()

	def StopBeeping(self):
		if self.isBeeping:
			self.isBeeping = False