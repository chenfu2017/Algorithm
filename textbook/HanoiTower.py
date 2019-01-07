class Solotion:
    def move(self, n, a, b):
        print("第%d个盘子:%c---->%c" % (n, a, b))

    def hanoi(self, n, a, b, c):
        if n > 0:
            self.hanoi(n - 1, a, c, b)
            self.move(n, a, c)
            self.hanoi(n - 1, b, a, c)


Solotion().hanoi(3, 'a', 'b', 'c')
