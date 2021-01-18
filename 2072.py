#2072. 홀수만 더하기

T = int(input())
numbers = list()
num = list()
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num = list(map(int, input().split()))
    numbers.append(num)

for num in range(0, T):
    odd = 0
    for i in range(0, 10):
        if numbers[num][i] % 2 == 1:
            odd += numbers[num][i]
    print("#{} {}".format(num + 1, odd))
