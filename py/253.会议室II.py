import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        # rooms = []

        # def begin(interval):
        #     return interval[0]
        # intervals.sort(key = begin)

        # heapq.heappush(rooms, intervals[0][1])
        # # maxn = 1
        # # curn = 1
        # for i in intervals[1:]:
        #     if rooms[0] <= i[0]: #每次只弹出一个会议（保证用过的房间都不回收），用于保证len(rooms)就是最大的房间数
        #         heapq.heappop(rooms)
        #     heapq.heappush(rooms, i[1])
        # return len(rooms)

        def begin(interval):
            return interval[0]
        def end(interval):
            return interval[1]
        intervals.sort(key = begin)
        ends = intervals.copy()
        ends.sort(key = end)

        i = 1
        j = 0
        n = 1
        while (i < len(intervals)):
            if (intervals[i][0] >= ends[j][1]):
                i += 1
                j += 1
            else:
                i += 1
                n += 1
        
        return n