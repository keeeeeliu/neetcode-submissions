class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        l, r = 0, m - 1
        while True:
            i = (l + r) // 2 # index in nums1
            j = half - i - 2 # index in nums2
            
            nums1Left = nums1[i] if i >= 0 else float("-infinity")
            nums1Right = nums1[i + 1] if (i + 1) < m else float("infinity")
            nums2Left = nums2[j] if j >= 0 else float("-infinity")
            nums2Right = nums2[j + 1] if (j + 1) < n else float("infinity")
            
            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                # odd
                if total % 2:
                    return min(nums1Right, nums2Right)
                # even
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
            elif nums1Left > nums2Right:
                r = i - 1
            else:
                l = i + 1