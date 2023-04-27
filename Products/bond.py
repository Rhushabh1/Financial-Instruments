from datetime import datetime, timedelta

'''
locals() => returns map of <variable_name, datatype>
'''


class Bond:
	def __init__(self, 
				issueDate,			# when the bond is issued
				maturityDate,		# when the bond will mature
				couponeRate=4.0,		# annualised coupon rate
				couponFreq=2,			# frequency of bond coupons in a year
				faceValue=100.0 	# par value of the bond
				):
		if issueDate >= maturityDate:
			raise Exception("Issue Date must preceed Maturity Date")
		self.issueDate = issueDate
		self.maturityDate = maturityDate
		self.couponRate = couponRate
		self.couponFreq = couponFreq
		self.faceValue = faceValue
		self.par = 100.0 			# this is how price is quoted

	# def calcCouponDates(self):
	# 	# determine bond coupon dates
	# 	# these will note be adjusted based on calendar dates
	# 	pass

	# def calcCouponFlows(self):
	# 	# determine bond cash flow payment amounts without principal
	# 	pass

	# def priceFromYTM(self, settlementDate, ytm):
	# 	# calculate full price of bond from its YTM
	# 	pass

	# def principal(self, settlementDate, y):
	# 	# calculate principal value of the bond based on the face value from its discount margin
	# 	pass

	# def DV01(self, settlementDate, ytm):
	# 	# calculate risk or dP/dy of the bond by bumping
	# 	pass

	# def cleanPrice(self, cleanPrice, spotDate):
	# 	# return the current bond price without accrued interest
	# 	# add clean price to the data
	# 	pass

	# def cleanPriceFromYTM(self, settlementDate, ytm):
	# 	pass

	# def dirtyPrice(self):
	# 	# return the current bond price + accrued interest
	# 	pass
		
	# def currentYield(self, cleanPrice):
	# 	pass

	# def YTM(self, settlementDate, cleanPrice):
	# 	# returns yield to maturity
	# 	pass

	# def calcAccruedInterest(self, settlementDate):
	# 	pass

	# def RCY(self):
	# 	# returns realized current yield
	# 	pass

	# def PV01(self):
	# 	pass
