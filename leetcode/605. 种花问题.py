from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        l = len(flowerbed)
        i = 1
        print(flowerbed)
        while i < l - 1:
            if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
                n -= 1
                i += 2
                if n == 0:
                    return True
            else:
                i += 1
        return False


flowerbed = [1, 0, 1, 0, 0]
n = 1
print(Solution().canPlaceFlowers(flowerbed, n))
