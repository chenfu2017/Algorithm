class Solution:

    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.strip().split()))


s = "   a good   example"
print(Solution().reverseWords(s))
