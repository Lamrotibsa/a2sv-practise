n = int(input())

for j in range(n):
    row , col = map(int, input().split())
    matrix = []
    for i in range(row):
        val = list(map(int, input().split()))
        matrix.append(val)

    dic1  = {}
    dic2 = {}

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            summ = row + col
            diff = row - col
            if summ in dic1:
                dic1[summ]+=matrix[row][col]
            else:
                dic1[summ] = matrix[row][col]
            if diff in dic2:
                dic2[diff]+=matrix[row][col]
            else:
                dic2[diff] = matrix[row][col]

    maxx = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            summ = row + col
            diff = row - col
            val = dic1[summ] + dic2[diff] - matrix[row][col]

            maxx = max(maxx ,val)
    print(maxx)



            


