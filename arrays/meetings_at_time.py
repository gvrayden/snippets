# We ran into this problem while designing a calendar app. There are N meetings, each is represented by an interval (start time, end time). The list of meetings are known before hand. At various times, we want to know the number of meetings currently running.

# Examples:

# meetings: (1, 4), (2, 3.2), (5, 7)
# at time 2.5: 2 meetings
# at time 4.5: 0 meetings
# at time 5.5: 1 meetings

# [0,1,2,2,0,1,1,0,0]
# [0,1,2,3,4,5,6,7,8]
#start < input_time 
# end > input_time
# [{'s':(1:1,2:1,5:1),'e':(3.2:1,4:1,7:1)}]


# import requests
# import mysql.connector
# import pandas as pd
import bisect
print('Hello')
#calender - meeting
class Calendar(object):
    start_times = []
    end_times = []
    def __init__(self, meetings):
        self.meetings = meetings
        self.start_times = [x[0] for x in  sorted(meetings, key = lambda x: x[0])]
        self.end_times = [x[1] for x in sorted(meetings, key=lambda x: x[1])]
        
    def query(self, input_time):
        # pass
        # i = 2.5
        ix = bisect.bisect_left(self.start_times, input_time) #1 None
        ix_end = bisect.bisect_left(self.end_times, input_time) #0 #None

        return ix - ix_end

cal = Calendar([(1, 4), (5, 7),(2, 3.2) ])
print('hello')
print(cal.start_times)
print(cal.end_times)
print(cal.query(5.5))