hour, minute = input().split()
hour = int(hour)
minute = int(minute)
if hour > 24 or minute > 60:
    print('잘못된 시간 입력입니다.')
elif minute - 45 < 0:
    if hour - 1 < 0:
        hour = 24 - 1
    else:
        hour -= 1
    minute = (60 + minute) - 45
else:
    minute -= 45

print(hour, minute)