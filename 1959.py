#1959. 두 개의 숫자열


def calc(A, B, As, Bs):
    max = 0
    for i in range(B - A + 1):
        tmp = 0
        for j in range(i, i + A):
            tmp += (As[j - i] * Bs[j])
        if tmp > max:
            max = tmp
    return max


T = int(input())

for t in range(1, T + 1):
    len1, len2 = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    if len1 > len2:
        print("#{} {}".format(t, calc(len2, len1, list_b, list_a)))
    else:
        print("#{} {}".format(t, calc(len1, len2, list_a, list_b)))