from bisect import insort
from collections import defaultdict
class MyCalendarThree:

    def __init__(self):
        self.bookings = []
        self.d = defaultdict(lambda: 0)

    def book(self, start: int, end: int) -> int:
        if start not in self.d:
            insort(self.bookings, start)
        if end not in self.d:
            insort(self.bookings, end)
        self.d[start] += 1
        self.d[end] -= 1
        
        curr = 0
        best = float('-inf')
        for i in self.bookings:
            curr += self.d[i]
            best = max(best, curr)
        return best


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)