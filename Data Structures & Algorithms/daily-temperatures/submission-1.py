class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx
            stack.append((t,i))
            # for x in range(i + 1, len(temperatures)):
            #     if temperatures[x] > t:
            #         res[i] = x - i
            #         break
        return res