import bisect 
class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        even = [v for v in nums if v % 2 == 0]
        ans = []


        for l,r,k in queries:
            lo=nums[l]
            hi=nums[r]
            start = bisect.bisect_left(even,lo)
            end = bisect.bisect_right(even,hi)
            remove_cnt = end-start

            left,right = 1,k+remove_cnt
            while left<right:
                mid = (left+right)//2
                removed = bisect.bisect_right(even, 2 * mid, start, end) - start
                if mid -removed>= k:
                    right = mid
                else:
                    left=mid+1
            ans.append(2*left)

        return ans