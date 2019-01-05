def fuelup(n, k, sum):
    count = 0
    i = 0
    fuel = n
    while i <= k:
        if n < sum[i]:
            print("不可达!")
            return
        if fuel < sum[i]:
            count += 1
            fuel = n - sum[i]
        else:
            fuel = fuel - sum[i]
        i += 1
    return count


n = k = 7
sum = [1, 2, 3, 4, 5, 1, 6, 6]
print('需要加油的次数为：%d' % fuelup(n, k, sum))
