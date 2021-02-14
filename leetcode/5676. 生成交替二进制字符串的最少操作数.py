class Solution:
    def minOperations(self, s: str) -> int:
        flag = '1'
        res1 = 0
        for i in s:
            if i !=flag:
                res1 +=1
            flag = '0' if flag =='1' else '1'
        res2 = 0
        flag = '0'
        for i in s:
            if i != flag:
                res2 += 1
            flag = '0' if flag == '1' else '1'
        return min(res1,res2)


s ='10'
print(Solution().minOperations(s))