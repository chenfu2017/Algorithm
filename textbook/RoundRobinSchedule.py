class Solution:
    def getSchedule(self, k):
        m = 2 ** k
        arr = [[0] * m for _ in range(m)]
        if k <= 0:
            return arr
        arr[0][0] = 1
        for i in range(1, k + 1):
            half = 2 ** (i - 1)
            for row in range(half):
                for col in range(half):
                    arr[row + half][col + half] = arr[row][col]
                    arr[row + half][col] = arr[row][col] + half
                    arr[row][col + half] = arr[row + half][col]
        return arr

    def show(self, arr):
        for i in arr:
            for j in i:
                print(j, end='  ')
            print()


arr = Solution().getSchedule(2)
Solution().show(arr)
