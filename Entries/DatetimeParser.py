import re
import datetime


class DatetimeParser:
	def __init__(self):
		self.coc = None
		self.Add(DatetimeStringParser())

	def Parse(self, string):
		if self.coc is not None:
			return self.FixDatetime(self.coc.Parse(string))

	def FixDatetime(self, date):
		if date.year == 1900:
			now = datetime.datetime.now()
			date = date.replace(year=now.year, month=now.month, day=now.day)
		return date

	def Add(self, parser):
		if self.coc is None:
			self.coc = parser
			return
		self.coc.Add(parser)


class Parser:
	def __init__(self):
		self.next = None

	def Add(self, parser):
		if self.next is None:
			self.next = parser
			return
		self.next.Add(parser)


class DatetimeStringParser(Parser):
	def __init__(self):
		super().__init__()
		self.parseStrings = [
			'%Y-%m-%d %H:%M:%S',
			'%Y/%m/%d %H:%M:%S',
			'%Y.%m.%d %H:%M:%S',

			'%Y-%m-%d %H:%M',
			'%Y/%m/%d %H:%M',
			'%Y.%m.%d %H:%M',

			'%m-%d %H:%M:%S',
			'%m/%d %H:%M:%S',
			'%d.%m %H:%M:%S',

			'%m-%d %H:%M',
			'%m/%d %H:%M',
			'%d.%m %H:%M',

			'%H:%M:%S',
			'%H:%M',
		]

	def Parse(self, string):
		print("Got", string)
		for i in self.parseStrings:
			try: return datetime.datetime.strptime(string, i)
			except ValueError: continue
