import threading
import time

class SpawnThread:
	def __init__(self, interval, ui):
		self.interval = interval
		self.ui = ui
		self.thread = threading.Thread(target=self.Run)
		self.thread.start()

	def Run(self):
		while True:
			self.ui.Show()
			time.sleep(self.interval)
