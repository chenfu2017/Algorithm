class Solution:
    def __init__(self):
        self.visit = []
        self.res = []

    def permute_1(self, list):
        n = len(list)
        self.visit = [False] * n

        def permute_1_detail(index, l):
            if index == n:
                if l not in self.res:
                    self.res.append(l)
                return
            for i in range(n):
                if not self.visit[i]:
                    self.visit[i] = True
                    permute_1_detail(index + 1, l + [list[i]])
                    self.visit[i] = False

        permute_1_detail(0, [])

    def permute_2(self, i, l):
        n = len(l)
        if i == n:
            print(l)
            if l not in self.res:
                self.res.append(l.copy())
            return
        for j in range(i, n):
            l[i], l[j] = l[j], l[i]
            self.permute_2(i + 1, l)
            l[i], l[j] = l[j], l[i]


s = Solution()
l = [1,2,3]
# s.permute_1(l)
s.permute_2(0, l)
for r in s.res:
    print(r)
print(len(s.res))