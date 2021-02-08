#1959. 두 개의 숫자열

T = int(input())

list_a = list(); list_b = list(); numSum = 0
for test_case in range(T):
    a,b = map(int, input().split())
    num_a = list(map(int, input().split()))
    num_b = list(map(int, input().split()))
    list_a = num_a
    list_b = num_b
    print(list_a, list_b)

    cal_list = [0]*min(len(list_a), len(list_b))

    for i in range(min(len(list_a), len(list_b))):
        for j in range(i+1):
            numSum += list_a[i] * list_b[j]
            print(numSum)
        print(numSum)
        cal_list[i] = numSum
        print(cal_list)
print(cal_list)



# def calc(A, B, As, Bs):
#     result = 0
#     for i in range(B - A + 1):
#         tmp = 0
#         for j in range(i, i + A):
#             tmp += (As[j - i] * Bs[j])
#         if tmp > result:
#             result = tmp
#     return result
#
#
# T = int(input())
# for t in range(1, T + 1):
#     N, K = map(int, input().split())
#     ns = list(map(int, input().split()))
#     ks = list(map(int, input().split()))
#
#     if N > K:
#         print("#{} {}".format(t, calc(K, N, ks, ns)))
#     else:
#         print("#{} {}".format(t, calc(N, K, ns, ks)))