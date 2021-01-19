#2029. 몫과 나머지 출력하기

T = int(input())
num = list()
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    num.append(a)

for i in range(0, len(num)):
    num1 = num[i][0] // num[i][1]
    num2 = num[i][0] % num[i][1]
    print('#{} {} {}' .format(i+1, num1, num2))