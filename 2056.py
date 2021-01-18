#2056.연월일 달력

T = int(input())
date = list()

odd=['01','03','05','07','08','10','12']
even=['04','06','09','11']

for test_case in range(1, T+1):
    str = input()
    if str[4:6] in odd: #31일까지
        if 0<int(str[6:])<=31:
            str = str[0:4]+"/"+str[4:6]+"/"+str[6:]
            date.append(str)
        else:
            date.append('-1')
    elif str[4:6] in even: #30일까지
        if 0<int(str[6:])<=30:
            str = str[0:4]+"/"+str[4:6]+"/"+str[6:]
            date.append(str)
        else:
            date.append('-1')
    elif str[4:6]=='02': #2월만
        if 0<int(str[6:])<=28:
            str = str[0:4] + "/" + str[4:6] + "/" + str[6:]
            date.append(str)
        else:
            date.append('-1')
    else:
        date.append('-1')

for _ in range(len(date)):
    print(date[_])


# num = int(input())
# for i in range(1, num+1):
#     a = input()
#     year = int(a[0:4])
#     month = int(a[4:6])
#     day = int(a[6:])
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     ans = -1
#     if month<=12 and month>=1:
#         if day<=days[month-1] and day >=1:
#             ans=a[0:4]+"/"+a[4:6]+"/"+a[6:8]
#     print("#{} {}".format(i, ans))