class Solution:
    d = {')':'(','}':'{',']':'['}
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l =[]
        for i in s:
            if i in['{','[','(']:
                l.append(i)
            else:
                if(len(l)>0):
                    if l.pop()!=self.d[i]:
                        return False
                else:
                    return False
        return True if len(l) == 0 else False


print(Solution().isValid("{}}{"))