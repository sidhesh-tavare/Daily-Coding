class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s,l=0,len(nums)-1
        while s<=l:
            if nums[s]==val:
                nums[s],nums[l]=nums[l],nums[s]
                l-=1
                
            else:
                s+=1
        return s 
        