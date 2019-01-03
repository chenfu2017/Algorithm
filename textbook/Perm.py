class Solution:
    def perm(self,list, k, m):
        if k == m-1:
            print(list)
        else:
            for i in range(k,m):
                list[k], list[i] = list[i], list[k]
                self.perm(list,k+1,m)
                list[k], list[i] = list[i], list[k]

list=[1,2,3]
Solution().perm(list,0,len(list))