class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        res = []
        m = set()
        for i in range(n-9):
            substr = s[i:i+10]
            # print(substr)
            if substr not in m:
                m.add(substr)
            else:
                res.append(substr)
        return list(set(res))


s = "AAAAAAAAAAA"

print(Solution().findRepeatedDnaSequences(s))