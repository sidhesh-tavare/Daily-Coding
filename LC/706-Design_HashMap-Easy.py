class MyHashMap:

    def __init__(self):
        self.size = 1000001
        self.arr = [None]* self.size
        
    def put(self, key: int, value: int) -> None:
        self.arr[key] = value         

    def get(self, key: int) -> int:
        val = self.arr[key]
        if val is None : return -1
        else: return val
        

    def remove(self, key: int) -> None:
        self.arr[key] = None

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)