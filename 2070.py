#2070. 큰놈, 작은 놈, 같은 놈

T = int(input())
num = list()

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    num.append(a)

for i in range(0, T):
    if num[i][0] > num[i][1]:
        print('#{} {}' .format(i+1,'>'))
    elif num[i][0] < num[i][1]:
        print('#{} {}' .format(i+1,'<'))
    elif num[i][0] == num[i][1]:
        print('#{} {}' .format(i+1,'='))