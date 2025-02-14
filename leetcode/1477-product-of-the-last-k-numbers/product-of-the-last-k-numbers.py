class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]  # Initialize with 1 to handle product of empty list scenario

    def add(self, num: int) -> None:
        if num == 0:
            # If a zero is added, reset the list to contain only 1 (will handle any future zero product calculations)
            self.arr = [1]
        else:
            # Append the cumulative product (prod[i] = prod[i-1] * num)
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.arr):
            return 0  # If `k` is larger than the length, we can't compute the product
        # Return the product of the last k elements
        return self.arr[-1] // self.arr[-k-1]



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)