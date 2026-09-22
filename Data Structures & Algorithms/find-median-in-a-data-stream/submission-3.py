class MedianFinder:
    # I know this problem
    # you need a max heap and a min heap of equal sizes on both sides.
    # one heap should not be larger than than the other heap by more than 1.
    # if we need a median we check to see if the two are the same size then we either pick the average betwee the min and max. 
    # Or we pick the top value from the larger heap
    def __init__(self):
        self.smaller = [] # max_heap negative values
        self.bigger = [] # min_heap positive values
    
    def balance(self):
        # here we check if the diff between them is more than 1 and balance
        diff = len(self.smaller) - len(self.bigger)
        if diff > 1:
            largest = -heapq.heappop(self.smaller)
            heapq.heappush(self.bigger, largest)
        elif diff < -1:
            smallest = heapq.heappop(self.bigger)
            heapq.heappush(self.smaller, -smallest)


    def addNum(self, num: int) -> None:
        if self.smaller and num > -self.smaller[0]:
            heapq.heappush(self.bigger, num)
        else:
            heapq.heappush(self.smaller, -num)
        self.balance()

    def findMedian(self) -> float:
        if len(self.smaller) == len(self.bigger):
            return (-self.smaller[0] + self.bigger[0]) / 2
        elif len(self.smaller) > len(self.bigger):
            return -self.smaller[0]
        else:
            return self.bigger[0]