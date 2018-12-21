class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        result=[1]*n
        i1=i2=i3=0
        c1,c2,c3=2,3,5
        for i in range(1,n):
            val =result[i]=min(c1,c2,c3)
            while c1 <= val:
                i1+=1
                c1 = 2 * result[i1]
            while c2 <= val:
                i2+=1
                c2 = 3 * result[i2]
            while c3 <= val:
                i3+=1
                c3 = 5 * result[i3]
        # print(result)
        return result[-1]

Solution().nthUglyNumber(10)
