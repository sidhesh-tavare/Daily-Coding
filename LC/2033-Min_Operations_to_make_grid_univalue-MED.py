class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        res,arr=0,[]
        for row in grid:
            for num in row:
                arr.append(num)

        arr.sort()
        n = len(arr)
        fin = arr[n//2]

        for num in arr:
            if num%x!=fin%x: return -1 
            else:
                res+=abs(num-fin)//x
        return res
        
        