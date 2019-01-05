class Solution:
    def inverted(self,num,l):
        l.append(num%10)
        if num>0:
            self.inverted(num//10,l)


l = []
Solution().inverted(12345,l)
print(l)
