#2068. 최대수 구하기

T = int(input())
num = list()

for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    num.append(a)

for i in range(0, T):
    print('#{} {}' .format(i+1, max(num[i])))
