import datetime

def leap_year_generator(n):
  current_year = datetime.datetime.now().year
  i = 0
  year = current_year
  while i < n:
    if (year % 4 == 0):
	    if (year % 100 != 0 or year % 400 == 0):
				# it's a leap year
				i += 1
				yield year
    year += 1
      
# using the generator
for yr in leap_year_generator(10):
  print "It's leap year:", yr