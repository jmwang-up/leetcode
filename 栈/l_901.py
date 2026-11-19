class StockSpanner:

    def __init__(self):

        self.data = []

    def next(self, price: int) -> int:

        count = 1
    
        while self.data and self.data[-1][0] <= price:

            prev = self.data.pop()
            count += prev[1]

        self.data.append([price, count])
        return count