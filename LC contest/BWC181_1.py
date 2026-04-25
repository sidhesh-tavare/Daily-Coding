class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        strnum = str(n)
        strx = str(x)
        if strx in strnum and strnum[0]!=strx:
            return True 
        else: return False