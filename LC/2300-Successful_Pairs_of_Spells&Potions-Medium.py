class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)

        def valid_checker(spell):
            l,h = 0,n-1
            while l<=h:
                m=(l+h)//2
                if spell*potions[m]>=success:
                    h=m-1
                else:
                    l=m+1
            return n-l
        
        for sp in spells:
            res.append(valid_checker(sp))
        return res
        