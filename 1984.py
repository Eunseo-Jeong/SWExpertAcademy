#1984. 중간 평균값 구하기
import math

T = int(input())

num = list()

for test_case in range(T):
    a = list(map(int, input().split()))
    num.append(a)

for i in range(len(num)):
    result=(sum(num[i])-max(num[i])-min(num[i]))/8
    print("#{} {}" .format(i+1, round(result)))