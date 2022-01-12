import sys
r = sys.stdin.readline

cal = r()

# -를 기준으로 나눠줌
sector = cal.split('-')

number = []

for i in sector :
    plus = i.split('+')
    temp = 0
    for j in plus:
        temp += int(j)
    number.append(temp)

result = number[0]

for i in range(1, len(number)) :
    result -= number[i]

print(result)