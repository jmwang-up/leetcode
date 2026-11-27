class ProductOfNumbers:

    def __init__(self):
        
        self.data = [1]

    def add(self, num: int) -> None:
        """
        num = 1
        前缀积 1
        num = 2
        前缀积
        1 * 2 2 -> 1, 2
        num = 3
        1, 2, 6
        num = 4  [1, 2, 3, 4]
        1, 2, 6, 24 倒数第k个 

        1 2 0 3 4
        1 2 0 3 12
        3 12
        总后缀积 / ans[-k - 1]
        """
        if num == 0:
            self.product = [1]
            return

        self.data.append(self.data[-1] * num)

    def getProduct(self, k: int) -> int:

        if k >= len(self.data):
            return 0
        return self.data[-1] // self.data[-k - 1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)