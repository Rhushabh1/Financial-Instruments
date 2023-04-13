# from quantlib import *

class Bond:
	def __init__(self, issueDate, couponRate, Ncoupon, maturity):
		self.issueDate = issueDate
		self.couponRate = couponRate
		self.Ncoupons = Ncoupons
		self.maturity = maturity
		self.buyDate = issueDate

	def cleanPrice(self):
		# return the current bond price without accrued interest
		pass

	def dirtyPrice(self):
		# return the current bond price + accrued interest
		pass
		
	def simpleYield(self):
		pass

	def YTM(self):
		# returns yield till maturity
		pass

	def RCY(self):
		# returns realized current yield
		pass
