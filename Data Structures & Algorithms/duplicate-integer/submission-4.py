class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        container = set()
        for n in nums:
            if n not in container:
                container.add(n)
            else:
                return True
        return False

        