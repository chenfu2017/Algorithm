def fuelup(n, dist):
    k = len(dist)-1
    count = 0
    i = 0
    fuel = n
    while i <= k:
        if n < dist[i]:
            print("不可达!")
            return
        if fuel < dist[i]:
            count += 1
            fuel = n - dist[i]
        else:
            fuel = fuel - dist[i]
        i += 1
    return count


n = 7
sum = [1, 2, 3, 4, 5, 1, 6, 6]
print('需要加油的次数为：%d' % fuelup(n, sum))
