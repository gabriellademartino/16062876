# -*- coding: utf-8 -*-
"""
Created on Sun Oct 08 10:20:21 2017

@author: Tamara
"""

print 'This should return my height'
foot = 30.48
height_in_cm = 5.85*foot
print height_in_cm

print 'This should return 1610.0'
mile_in_km = 1.61
mile_in_meters = mile_in_km*1000
print mile_in_meters

print 'This should return 0.1625. How many seconds per meter does it take?'
seconds_per_meter = 130.0/800.0
print seconds_per_meter
print 'This should return 261,625. How many seconds does it take to run a mile?'
seconds_per_mile = seconds_per_meter*1610.0
print seconds_per_mile
print 'The code should print the minutes it takes to run a mile in the aforementioned pace.'
minutes_per_mile = int(seconds_per_mile)/60
print minutes_per_mile
print 'The following code prints the remainder of the equation above. The remainder should be 21 seconds.'
remainder_in_seconds = int(seconds_per_mile)%60
print remainder_in_seconds
print 'If you count 4 minutes plus 21 seconds: It takes you 4:21 minutes/mile'