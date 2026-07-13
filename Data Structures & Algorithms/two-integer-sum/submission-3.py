class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = defaultdict()
        
        res = []
        for i, n in enumerate(nums):
            if n not in lookup:
                lookup[target - n] = i

            else:
                res.append(lookup[n])
                res.append(i)
                return res
        return res