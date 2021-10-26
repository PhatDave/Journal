import datetime
import threading
import time
from winsound import Beep


class Beeper:
	def __init__(self, reminders):
		self.reminders = reminders
		self.thread = threading.Thread(target=self.Run)
		self.beepThread = threading.Thread(target=self.Beep)
		self.beepSem = threading.Semaphore(1)
		self.isBeeping = False

	def Start(self):
		self.thread.start()

	def Run(self):
		while True:
			if self.reminders.rlist[0].date <= datetime.datetime.now():
				self.StartBeeping()
			time.sleep(0.5)

	def Beep(self):
		while True:
			self.beepSem.acquire()
			Beep(1200, 500)
			self.beepSem.release()

	def StartBeeping(self):
		if not self.isBeeping:
			self.isBeeping = True
			self.beepThread.start()
			self.beepSem.release()

	def StopBeeping(self):
		if self.isBeeping:
			self.beepSem.acquire()

