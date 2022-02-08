import sys
r = sys.stdin.readline

mushroom = []
score = 0
gap = 0

for i in range(10) :
    mushroom.append(int(r()))

score += mushroom[0]
gap = 100 - score
for i in range(1, 10) :
    score += mushroom[i]
    temp = 100 - score
    if temp < 0 :
        temp *= -1
    if gap > temp :
        gap = temp
    elif gap < temp :
        score -= mushroom[i]
        break
    elif gap == temp :
        break

print(score)