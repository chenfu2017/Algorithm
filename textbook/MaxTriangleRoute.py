list = [
            [7],
          [3, 8],
         [8, 1, 0],
       [2, 7, 4, 4],
      [4, 5, 2, 6, 5]
]


def fun():
    m = list.copy()
    for i in range(1, len(list)):
        for j in range(len(list[i])):
            if j == 0:
                m[i][j] = m[i][j] + m[i - 1][j]
            elif j == len(list[i]) - 1:
                m[i][j] = m[i][j] + m[i - 1][j - 1]
            else:
                m[i][j] = m[i][j] + max(m[i - 1][j], m[i - 1][j - 1])
    print(m)
    return max(m[len(m) - 1])

print("最长路径为%d" % fun())
