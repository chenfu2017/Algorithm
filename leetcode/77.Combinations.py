class Solution:

    res = []
    visit = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        l = []
        self.res.clear()
        self.ds(n,k,1,l)
        print(self.res)
        return self.res

    def ds(self,n,k,start,l):
        if len(l)==k:
            self.res.append(l.copy())
            return

        for i in range(start,n-(k-len(l))+2):
                l.append(i)
                self.ds(n,k,i+1,l)
                l.pop()

Solution().combine(4,2)

