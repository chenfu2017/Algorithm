class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        l = [
            [1],
        ]
        for i in range(1, numRows):
            m = [1] * (i + 1)
            for j in range(1, i):
                m[j] = l[i - 1][j - 1] + l[i - 1][j]
            l.append(m)
        return l
print(Solution().generate(3))