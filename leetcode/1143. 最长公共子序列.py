class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        m, n = len(text1)+1, len(text2)+1
        l = [[0] * n  for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                if text1[i-1] == text2[j-1]:
                    l[i][j] =l[i-1][j-1] + 1
                else:
                    l[i][j] =max(l[i-1][j],l[i][j-1])
        # print(l)
        return l[-1][-1]

text1 = "abcded"
text2 = "qwe"
print(Solution().longestCommonSubsequence(text1,text2))
