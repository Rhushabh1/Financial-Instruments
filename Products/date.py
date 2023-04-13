


def convertToDays(date):
	return (date.year*12 + date.month)*30 + date.day


def convertToDate(days):
	month, day = days//30, days%30
	year, month = month//12, month%12
	return Date(day, month, year)


class Date:
	# 30 days in a month
	# 12 months in a year
	def __init__(self, day, month, year):
		self.day = day
		self.month = month
		self.year = year


	def __str__(self):
		return "{}-{}-{}".format(self.day, self.month, self.year)

	def __add__(self, other):
		days = convertToDays(self) + convertToDays(other)
		return convertToDate(days)

	def __sub__(self, other):
		days = convertToDays(self) - convertToDays(other)
		return convertToDate(days)