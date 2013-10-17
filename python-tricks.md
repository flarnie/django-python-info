# Cool Python Tricks

## 1. List/Map Comprehensions

This is a shortcut for writing an iterator to create a list.
(Lists are like Ruby arrays.)

Details [in the docs][list-comprehensions].

[list-comprehensions]: http://docs.python.org/2/tutorial/datastructures.html#list-comprehensions

## 2. Python Generators for Large (or Infinte) Data Sets

For a large data set, a generator allows for lazy evaluation of each item one at a time, rather than loading the entire data set into memory for iteration.

For creating a generator for a large range of numbers, Python has the [built-in xrange method][xrange-python].

Example:

```python
# Large data set
# Example: sum of a large set of numbers

total = sum(n for n in xrange(1, 1000000000))
=> 499999999500000000

# Infinite data set
# Example: Finding the nth next leap year

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

```

For more, try the [Advanced Generators Tutorial at Dream in Code][adv-generators-python].


[adv-generators-python]: http://www.dreamincode.net/forums/topic/287295-advanced-python-generators/
[python-xrange]: http://docs.python.org/2/library/functions.html#xrange
