# 2005. 파스칼의 삼각형

T = int(input())

for test_case in range(T):
    num = int(input())

    list = [[1] * _ for _ in range(1, num+1)]
    for i in range(num):
        for j in range(i):
            if i==num-1:
                break
            list[i+1][j+1] = list[i][j] + list[i][j+1]
    print("#{}" .format(test_case + 1))
    for i in range(num):
        for j in range(i+1):
            print(list[i][j], end=" ")
        print("")
    # print(list)