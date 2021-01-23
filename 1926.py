#1926. 간단한 369게임

N = int(input())

clap = [3, 6, 9]

for test_case in range(1, N+1):
    if test_case//10 in clap or test_case%10 in clap:
        if test_case//10 in clap and test_case%10 in clap:
            print("-", end="")
        print("-", end=" ")
        continue
    print(test_case, end=" ")
