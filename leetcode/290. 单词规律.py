class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        m = {}
        n = {}
        str = s.split(' ')
        if len(pattern) != len(str):
            return False
        for i, j in zip(pattern, str):
            if i in m and j in n:
                if m[i] != j or n[j] != i:
                    return False
            elif i in m and j not in n:
                return False
            elif i not in m and j in n:
                return False
            else:
                m[i] = j
                n[j] = i
        return True


pattern = "abba"
str = "dog cat cat fish"
print(Solution().wordPattern(pattern, str))
