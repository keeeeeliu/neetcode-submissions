class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = dict()
        for s_c in s:
            if s_c not in tracker:
                tracker[s_c] = 0
                tracker[s_c] += 1
            else:
                tracker[s_c] += 1
        for t_c in t:
            if t_c not in tracker:
                return False
            else:
                tracker[t_c] -= 1

        return True if all(tracker[z] == 0 for z in tracker) else False