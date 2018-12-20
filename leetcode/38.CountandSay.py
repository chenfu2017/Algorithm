class Solution(object):

    l = ["1","11"]
    def countAndSay(self, n):
        if len(self.l)>=n:
            return self.l[n-1]

        def countSay(string):
            res, count = "", 1
            for i in range(1, len(string)):
                if string[i - 1] == string[i]:
                    count += 1
                else:
                    res += str(count) + string[i - 1]
                    count = 1
                if i == len(string) - 1: res += str(count) + string[i]
            return res

        for i in range(n-len(self.l)):
            self.l.append(countSay(self.l[-1]))
        return self.l[n-1]
Solution().countAndSay(3)
print(Solution().countAndSay(5))
