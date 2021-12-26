'''
    조건은 두개지만 결국 싼게 X보다 같거나 앞에 있으면 안된다 와 같은 말이므로 가격은 내림차순형태로
    작아져야지 X의 조건에 충족할 수 있다. 그러므로 앞의 가격이 뒤에보다 비싸기만 하면 되므로
    sort를 이용해서 정렬을 해주고 순차적으로 탐색한다
    여기서 앞의 가격보다 뒤의 가격이 더 비싸면 즉, c > maxC 일 경우 X가 되지 못하고 그러므로 maxC의 값도
    변화시키지 않는 형태로 탐색하면 된다.
'''
import sys
r = sys.stdin.readline

N = int(r())
P = []
result = 0
maxC = 10001

for i in range(N) :
    temp = list(map(int, r().split()))
    P.append(temp)

P.sort(key=lambda x : (x[0], x[1])) #정렬

for i in range(N) :
    c = P[i][1]
    if c < maxC :
        maxC = c
        result += 1

print(result)