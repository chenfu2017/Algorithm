class Solution:
    def k_min(self, arr, low, high, k):
        if k > len(arr) or k < 1:
            return None
        i, j = low, high
        p = arr[low]
        while not i == j:
            while i < j and arr[j] >= p:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= p:
                i += 1
            arr[j] = arr[i]
        arr[i] = p
        if k - 1 == i:
            return arr[i]
        elif k - i > i:
            return self.k_min(arr, i + 1, high, k)
        else:
            return self.k_min(arr, low, i - 1, k)

    def k_max(self, arr, low, high, k):
        if k > len(arr) or k < 1:
            return None
        i, j = low, high
        p = arr[low]
        while not i == j:
            while i < j and arr[j] >= p:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= p:
                i += 1
            arr[j] = arr[i]
        arr[i] = p
        n = len(arr)
        if k + i == n:
            return arr[i]
        elif k + i < n:
            return self.k_max(arr, i + 1, high, k)
        else:
            return self.k_max(arr, low, i - 1, k)


arr = [7, 3, 9, 5, 1, 6, 8]
print(Solution().k_min(arr, 0, len(arr) - 1, 2))
