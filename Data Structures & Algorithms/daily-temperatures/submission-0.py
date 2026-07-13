class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            for x in range(i + 1, len(temperatures)):
                if temperatures[x] > t:
                    res[i] = x - i
                    break
        return res