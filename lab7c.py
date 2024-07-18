#!/usr/bin/env python3
# Student ID: Harsahir Singh (hs100)

class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second
    """
    def __init__(self,hour=12,minute=0,second=0):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    # Convert both time objects to seconds
    seconds1 = time_to_sec(t1)
    seconds2 = time_to_sec(t2)
    
    # Sum the seconds
    total_seconds = seconds1 + seconds2
    
    # Convert the total seconds back to a time object
    return sec_to_time(total_seconds)

def valid_time(t):
    """Check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    """Modify the time object by adding a given number of seconds, handling both positive and negative values correctly."""
    # Convert the time object to seconds
    total_seconds = time_to_sec(time)
    
    # Add the given seconds
    total_seconds += seconds
    
    # Convert back to a time object
    new_time = sec_to_time(total_seconds)
    
    # Update the original time object with the new values
    time.hour = new_time.hour
    time.minute = new_time.minute
    time.second = new_time.second

def time_to_sec(time):
    '''Convert a time object to a single integer representing the number of seconds from midnight'''
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    '''Convert a given number of seconds to a time object in hour, minute, second format'''
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes,60)
    return time
