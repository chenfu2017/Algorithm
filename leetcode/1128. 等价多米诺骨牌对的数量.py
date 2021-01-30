class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        m = {}
        n = len(dominoes)
        for i in range(n):
            l = dominoes[i]
            e,d = l[0],l[1]
            if e > d:
                l[0],l[1] = l[1] ,l[0]
            sum = l[0] * 10 + l[1]
            if sum in m:
                m[sum] += 1
            else:
                m[sum] = 1
        res = 0
        print(m)
        for i in m:
            res += m[i] * (m[i]-1)
        return res//2


dominoes = [[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]
print(Solution().numEquivDominoPairs(dominoes))