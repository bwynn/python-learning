#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

#construct a basic timedelta and print it
#print timedelta(days=365, hours=5, minutes=1)

# print today's date
#print "today is: " + str(datetime.now())

# print today's date one year from now
#print "one year from now it will be: " + str(datetime.now() + timedelta(days=365))

# create a timedelta that uses more than one argument
# print "in two weeks and 3 days it will be: " + str(datetime.now() + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
#t = datetime.now() - timedelta(weeks=1)
#s = t.strftime("%A %B %d, %Y")
#print "one week ago it was " + s

# How many days until April Fools Day?
today = date.today() # get today's date
afd = date(today.year, 4, 1) # get April fools for the same year
# use date comparison to see if april fools has already gone for the
# year. if it has, use the replace() function to get the date for next year
if afd < today:
    print "April Fool's day already went by %d days ago" % ((today-afd).days)
    afd = afd.replace(year=today.year + 1) # if so, get the date for next year

# Now calculate the amount of time until next April Fools Day
time_to_afd = abs(afd - today)
print time_to_afd.days, "days unitl next April Fools Day!"
