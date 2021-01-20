#2063. 중간값 찾기

import math

T = int(input())

a = list(map(int, input().split()))
num = sorted(a)
print(num[math.floor(len(a)/2)])
