class MyHashSet:

    def __init__(self):
        self.arr=[]

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.arr.append(key)
            

    def remove(self, key: int) -> None:
        for ele in self.arr:
            if ele == key:
                self.arr.remove(key)
                return
        

    def contains(self, key: int) -> bool:
        for ele in self.arr:
            if ele == key:
                return True
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)