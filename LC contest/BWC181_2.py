class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        n = len(nums)
        if n==0 : return -1 
        asc,desc,peak=0,0,False
        for i in range(n):
            if not peak:
                asc+=nums[i]
                if i+1<n and nums[i]>nums[i+1]:
                    peak = True
                    desc=nums[i]
                elif i==n-1:
                    desc=nums[i]
            else:
                desc+=nums[i]

        if asc>desc: return 0 
        elif desc>asc: return 1 
        else: return -1