class Solution:
    def search(self, list, target):
        j, i = 0, len(list) - 1
        while j <= i:
            mid = j + (i - j) // 2
            if list[mid] == target:
                return mid
            elif list[mid] < target:
                j = mid + 1
            else:
                i = mid - 1
        return [i, None][i < 0], [j, None][j >= len(list)]


l = [1, 2, 3, 5, 6, 7, 8]
print(Solution().search(l, 4))
