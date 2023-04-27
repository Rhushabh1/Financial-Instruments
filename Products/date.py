from datetime import datetime


'''
https://docs.python.org/3/library/datetime.html#
timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

Attributes (datetime) :-
min			The minimum representable DateTime
max			The maximum representable DateTime
resolution	The minimum possible difference between datetime objects
year		The range of year must be between MINYEAR and MAXYEAR
month		The range of month must be between 1 and 12
day			The range of day must be between 1 and number of days in the given month of the given year
hour		The range of hour must be between 0 and 24 (not including 24)
minute		The range of minute must be between 0 and 60 (not including 60)
second		The range of second must be between 0 and 60 (not including 60)
microsecond	The range of microsecond must be between 0 and 1000000 (not including 1000000)
tzinfo		The object containing timezone information
fold		Represents if the fold has occurred in the time or not

Class Functions (datetime) :-
astimezone()		Returns the DateTime object containing timezone information.
combine()			Combines the date and time objects and return a DateTime object
ctime()				Returns a string representation of date and time
date()				Return the Date class object
fromisoformat()		Returns a datetime object from the string representation of the date and time
fromordinal()		Returns a date object from the proleptic Gregorian ordinal, where January 1 of year 1 has ordinal 1. The hour, minute, second, and microsecond are 0
fromtimestamp()		Return date and time from POSIX timestamp
isocalendar()		Returns a tuple year, week, and weekday
isoformat()			Return the string representation of date and time
isoweekday()		Returns the day of the week as integer where Monday is 1 and Sunday is 7
now()				Returns current local date and time with tz parameter
replace()			Changes the specific attributes of the DateTime object
strftime()			Returns a string representation of the DateTime object with the given format
strptime()			Returns a DateTime object corresponding to the date string
time()				Return the Time class object
timetuple()			Returns an object of type time.struct_time
timetz()			Return the Time class object
today()				Return local DateTime with tzinfo as None
toordinal()			Return the proleptic Gregorian ordinal of the date, where January 1 of year 1 has ordinal 1
tzname()			Returns the name of the timezone
utcfromtimestamp()	Return UTC from POSIX timestamp
utcoffset()			Returns the UTC offset
utcnow()			Return current UTC date and time
weekday()			Returns the day of the week as integer where Monday is 0 and Sunday is 6

Operations (timedelta) :-
Addition (+)		Adds and returns two timedelta objects
Subtraction (-)		Subtracts and returns two timedelta objects
Multiplication (*)	Multiplies timedelta object with float or int 
Division (/)		Divides the timedelta object with float or int
Floor division (//)	Divides the timedelta object with float or int and return the int of floor value of the output 
Modulo (%)			Divides two timedelta object and returns the remainder
+(timedelta)		Returns the same timedelta object
-(timedelta)		Returns the resultant of -1*timedelta
abs(timedelta)		Returns the +(timedelta) if timedelta.days > 1=0 else returns -(timedelta)
str(timedelta)		Returns a string in the form (+/-) day[s],  HH:MM:SS.UUUUUU
repr(timedelta)		Returns the string representation in the form of the constructor call

'''


class Date(datetime):
	def __init__(self, ):
		# *args = non-keyworded arguments
		# **kwargs = keyworded arguments
		super(Date, self).__init__(*args, **kwargs)