from datetime import datetime, timedelta
import numpy as np 
import numpy_financial as npf
from math import ceil

'''
locals() => returns map of <variable_name, datatype>
make rates annualised => use yearFraction
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
		self.couponRate = couponRate/100
		self.couponFreq = couponFreq
		self.faceValue = faceValue
		
		self.par = 100.0 			# this is how price is quoted
		self.tenor = (self.maturityDate - self.issueDate)/365
		self.tenor = int(self.tenor.days + self.tenor.seconds/86400)
		self.couponInterval = timedelta(days=365)/self.couponFreq
		self.couponDates = self.calcCouponDates()
		self.couponFlows = self.calcCouponFlows()

	def calcCouponDates(self):
		# determine bond coupon dates
		# these will not be adjusted based on calendar dates
		return [self.issueDate + self.couponInterval*(i+1) for i in range(self.tenor*self.couponFreq)]

	def calcCouponFlows(self):
		# determine bond cash flow payment amounts without principal
		self.couponFlows = [self.faceValue*self.couponRate for i in range(self.tenor*self.couponFreq)]

	def fullPriceFromYTM(self, settlementDate, ytm):
		# calculate full price of bond from its YTM
		nper = (self.maturityDate - settlementDate)/self.couponInterval
		return -npf.pv(ytm, ceil(nper), self.faceValue*self.couponRate, self.faceValue) + self.calcAccruedInterest(settlementDate)

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

	def cleanPriceFromYTM(self, settlementDate, ytm):
		nper = (self.maturityDate - settlementDate)/self.couponInterval
		return -npf.pv(ytm, ceil(nper), self.faceValue*self.couponRate, self.faceValue)

	def dirtyPrice(self, cleanPrice, settlementDate):
		# return the current bond price + accrued interest
		return cleanPrice + self.calcAccruedInterest(settlementDate)
		
	def currentYield(self, cleanPrice):
		return (self.couponRate*self.par)/cleanPrice

	def YTM(self, settlementDate, cleanPrice):
		# returns yield to maturity
		nper = (self.maturityDate - settlementDate)/self.couponInterval
		npf.rate(ceil(nper), self.faceValue*self.couponRate, cleanPrice, self.faceValue)

	def prevCouponDate(self, settlementDate):
		prevCoupons = filter(lambda x: (settlementDate-x).days<0, self.couponDates)
		return prevCoupons[-1]

	def nextCouponDate(self, settlementDate):
		nextCoupons = filter(lambda x: (settlementDate-x).days>=0, self.couponDates)
		return nextCoupons[0]

	def calcAccruedInterest(self, settlementDate):
		prevDate = self.prevCouponDate(settlementDate)
		return [(settlementDate - prevDate)/self.couponInterval] * self.faceValue*self.couponRate

	def RCY(self, reinvestmentRate, cleanPrice, settlementDate):
		# returns realized current yield
		C = self.faceValue*self.couponRate
		factor = 1 + reinvestmentRate/self.couponFreq
		nper = ceil((self.maturityDate - settlementDate)/self.couponInterval)
		totalFutureValue = np.sum(C*np.power(factor, np.arange(nper))) + self.faceValue
		rcy = np.power(totalFutureValue/cleanPrice, 1/nper) - 1
		return rcy*self.couponFreq


	# def PV01(self):
	# 	pass
