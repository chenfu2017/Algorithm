import heapq

class Solution:
    def arrange(self, s, f):
        h = []
        l = []
        n = len(s)
        for i in range(n):
            heapq.heappush(h, (f[i], s[i], i))
        e = 0
        while h:
            node = heapq.heappop(h)
            end, start, i = node
            if start >= e:
                l.append(i)
                e = end
        return l


s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(Solution().arrange(s, f))
