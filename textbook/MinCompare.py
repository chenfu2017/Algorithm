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
        m1 = heapq.heappop(l_min)
        m2 = heapq.heappop(l_min)
        min += m1 + m2 - 1
        heapq.heappush(l_min, m1 + m2)
        n1 = heapq.heappop(l_max)
        n2 = heapq.heappop(l_max)
        max += -n1 - n2 - 1
        heapq.heappush(l_max, n1 + n2)
    print("最少比较次数为%d，最多比较次数为%d" % (min, max))


list = [5, 12, 11, 2]
fun(list)
