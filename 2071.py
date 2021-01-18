#2071.평균값 구하기
T = int(input())
numbers = list()
num = list()

for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    numbers.append(num)

for num in range(0,T):
    print("#{} {}".format(num+1, round(sum(numbers[num])/10)))