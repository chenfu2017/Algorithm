import heapq


def fun(list):
    n = len(list)
    l_min = list.copy()
    heapq.heapify(l_min)
    l_max = []
    for i in list:
        heapq.heappush(l_max, -i)
    min = 0
    max = 0
    for i in range(n - 1):
        m = heapq.nsmallest(2, l_min)
        min += m[0] + m[1] - 1
        heapq.heappop(l_min)
        heapq.heappop(l_min)
        heapq.heappush(l_min, m[0] + m[1])
        n = heapq.nsmallest(2, l_max)
        max += -n[0] - n[1] - 1
        heapq.heappop(l_max)
        heapq.heappop(l_max)
        heapq.heappush(l_max, n[0] + n[1])
    print("最少比较次数为%d，最多比较次数为%d" % (min, max))


list = [5, 12, 11, 2]
fun(list)
