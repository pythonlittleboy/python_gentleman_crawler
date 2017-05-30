
import bisect

class SimilarQueue:
    def __init__(self, sortKey, size):
        self.list = []
        self.sortKey = sortKey
        self.size = size

    def add(self, obj):
        self.list.append(obj)

    def getList(self):
        self.list = sorted(self.list, key=lambda d: d[self.sortKey], reverse=True)

        if len(self.list) > self.size:
            self.list = self.list[0:self.size]

        return self.list;


"""
queue = SimilarQueue("s", 2)
queue.add({"s":1, "name":"a"})
queue.add({"s":2, "name":"b"})
print(queue.list)
queue.add({"s":3, "name":"c"})
print(queue.list) 
"""