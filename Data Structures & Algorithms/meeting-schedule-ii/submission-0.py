"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        max_rooms = 0
        rooms = 0
        s= e= 0
        if len(intervals) == 1:
            return 1

        start_times = sorted(i.start for i in intervals)
        end_times = sorted(i.end for i in intervals)

        print(start_times)
        print(end_times)
        
        while s< len(intervals):
            if start_times[s] < end_times[e]:
                rooms+=1
                max_rooms = max(rooms, max_rooms)
                s+=1

            else:
                rooms-=1
                e+=1
        return max_rooms





        