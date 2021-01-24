#1986. 지그재그 숫자

N = int(input())

output = list()

for test_case in range(N):
    num = int(input())

    sum_odd = 0; sum_even = 0
    for i in range(1, num+1):
        if i%2==0:
            sum_even+=i
        else:
            sum_odd+=i
    output.append(sum_odd-sum_even)

for _ in range(len(output)):
    print("#{} {}" .format(_+1, output[_]))