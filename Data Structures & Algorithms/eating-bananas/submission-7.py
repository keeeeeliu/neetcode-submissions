class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        num_p = len(piles)
        if h == num_p:
            return max(piles)
        
        if h == sum(piles):
            return 1
        res = max(piles)

        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            hour = 0

            for i in range(num_p):
                hour += math.ceil(piles[i]/m)
                if hour > h:
                    l = m +1
                    break
            if hour <= h:
                r = m - 1
                if m < res:
                    res = m
      
        return res

