class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        gap = 0
        while l < r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                gap = l
                break
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        else:
            gap = l
                        
     
        res = self.bsearch(nums[:gap],target)
        if res != -1:
            return res

        res = self.bsearch(nums[gap:],target)
        if res != -1:
            return res + gap
        return -1


    def bsearch(self, nums: List[int], target:int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) //2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
