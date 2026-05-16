class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.table = [None] * self.size
        
    def calc_hv(self,key):
        return key%self.size

    def add(self, key: int) -> None:
        hv = self.calc_hv(key)
        if self.table[hv] is None:
            self.table[hv] = [key]
        else: 
            if key not in self.table[hv]:
                self.table[hv].append(key)

    def remove(self, key: int) -> None:
        hv = self.calc_hv(key)
        if self.table[hv] is not None:
            while key in self.table[hv]:
                self.table[hv].remove(key)
        

    def contains(self, key: int) -> bool:
        hv = self.calc_hv(key)

        if self.table[hv] is not None:
            return key in self.table[hv]
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)