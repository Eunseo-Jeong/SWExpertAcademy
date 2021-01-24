#2007. 패턴마디의 길이

T = int(input())
str = list()

for test_case in range(T):
    str.append(input())

for i in range(len(str)):
    for j in range(1, len(str[i])):
        if str[i][j]==str[i][0] and str[i][j+1]==str[i][1]:
            break
    print("#{} {}".format(i+1, j))