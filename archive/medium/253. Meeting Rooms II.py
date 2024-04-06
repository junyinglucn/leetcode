# Solution A
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        event = [(_[0], 1) for _ in intervals] + [(_[1], -1) for _ in intervals]
        event.sort()
        ans = 0
        cur = 0
        for e, s in event:
            cur += s
            ans = max(ans, cur)
        return ans


# Solution B
import heapq


class Solution:
    def minMeetingRooms(self, intervals: list) -> int:
        rooms = []
        meetings = sorted(intervals, key=lambda x: x[0])
        for meeting in meetings:
            if rooms and rooms[0] <= meeting[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, meeting[1])
        return len(rooms)
