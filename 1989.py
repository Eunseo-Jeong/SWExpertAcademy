#1989. 초심자의 회문 검사

T = int(input())

str = list()
for test_case in range(T):
    word = input()
    str.append(word)

yes=1
for i in range(len(str)):
    num = len(str[i])

    for j in range(num):
        if str[i][j] == str[i][num-1-j]:
            yes = 1
        else:
            yes = 0

    if yes == 1:
        print("#{} {}".format(i + 1, 1))
    else:
        print("#{} {}".format(i + 1, 0))


