class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        i = j = 0
        s = m + n
        l = 0
        c = 0
        for index in range(s // 2+1):
            l = c
            if i < m and j < n:
                if nums1[i] <= nums2[j]:
                    c = nums1[i]
                    i += 1
                else:
                    c = nums2[j]
                    j += 1
            elif i >= m and j < n:
                c = nums2[j]
                j += 1
            else:
                c = nums1[i]
                i += 1
        if s %2 ==0:
            return (c+l)/2
        else:
            return c

a = [1,3,5,7,16]
b = [2,6,8]
print(Solution().findMedianSortedArrays(a,b))