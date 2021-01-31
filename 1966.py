#1966. 숫자를 정렬하자

T = int(input())

numberList = list()
for test_case in range(T):
    numberOf = int(input())
    for i in range(numberOf):
        num = int(input())
        numberList.append(num)
    print(numberList)
