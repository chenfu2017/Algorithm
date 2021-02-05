class Solution(object):

    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        for idx, char in enumerate(s):
            if char in stack: continue
            while stack and char < stack[-1] and stack[-1] in s[idx:]:
                stack.pop()
            stack.append(char)
        return "".join(stack)


s = "cbacdcbc"
print(Solution().removeDuplicateLetters(s))
