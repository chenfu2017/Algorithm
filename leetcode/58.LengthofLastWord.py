class Solution:
    def lengthOfLastWord(self, s):
        t = s.split()
        print(t)
        if t == []:
            return 0
        else:
            return len(t[-1])

print(Solution().lengthOfLastWord("aaaa   asdasd"))