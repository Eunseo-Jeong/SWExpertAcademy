#2058. 자릿수 더하기

T = int(input())
num = 0

while T > 0:
    num += T%10
    T = T//10

print(num)
