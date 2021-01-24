#######1989. 초심자의 회문 검사
import math

T = int(input())

str = list()

for test_case in range(T):
    word = input()
    str.append(word)


for i in range(len(str)):
    num = int(len(str[i]) / 2)
    print(str[i][num], num)

    for j in range(num):
        if str[i][j]==str[i][num+1+j]:
            # print(str[i][j], str[i][num+j])
            print("#{} {}" .format(i+1, 1))
            break
        else:
            print("#{} {}" .format(i+1, 0))
            break