class Solution:
    def __init__(self):
        self.weight = [
            [90, 85, 80],
            [80, 84, 79],
            [30, 47, 50],
        ]
        self.price = [
            [360, 400, 450],
            [500, 470, 510],
            [200, 180, 150]
        ]
        self.max_price = 1000
        self.min_weight = float('INF')
        self.x = []

    def supply(self, i, cp, cw, cx):
        if i == len(self.weight):
            if cw < self.min_weight:
                self.min_weight = cw
                self.x = cx.copy()
            return
        for j in range(len(self.weight[i])):
            if cp + self.price[i][j] <= self.max_price:
                self.supply(i + 1, cp + self.price[i][j], cw + self.weight[i][j], cx + [j])


s = Solution()
s.supply(0, 0, 0, [])
print(s.min_weight)
print(s.x)
