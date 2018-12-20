class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        digits[n-1]+=1
        while digits[n-1]>9 and n>=2:
            digits[n - 1] =0
            digits[n - 2] +=1
            n = n -1
        if digits[0]==10:
            digits[0]=0
            digits.insert(0,1)
        return digits

digits=[1,9,9]
print(Solution().plusOne(digits))