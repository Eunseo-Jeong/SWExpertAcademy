#1976. 시각 덧셈

T = int(input())

time = list()
for test_case in range(T):
    t1, m1, t2, m2 = map(int, input().split())
    hour = t1 + t2
    minute = m1 + m2
    if minute >= 60:
        hour = hour + minute//60
        minute = minute % 60
    if hour >= 12:
        hour = hour - 12
    time.append([hour, minute])

for i in range(T):
    print("#{} {} {}" .format(i+1, time[i][0], time[i][1]))