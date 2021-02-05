class Solution(object):
    def getIndex(self, i):
        return ord(i) - ord('a')

    def smallestSubsequence(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        m = [0] * 26
        for i in s:
            m[self.getIndex(i)] += 1
        for i in s:
            index = self.getIndex(i)
            if i in stack:
                m[index] -= 1
                continue
            while stack and stack[-1] > i and m[self.getIndex(stack[-1])]:
                stack.pop()
            stack.append(i)
            m[index] -= 1
        return ''.join(stack)


s = "cbacdcbc"
print(Solution().smallestSubsequence(s))
