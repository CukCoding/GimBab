'''
    두개의 사이트가 같은 점에 연결되는 경우의 수를 제외한 경우의 수는
    M * (M-1) * ... * (M-N+1) 까지 곱하게 된다. 여기서 다리가 겹쳐지면 안되는데,
    이것은 N의 사이트에서 밑에 있는 다리가 위에 있는 다리가 연결된 점보다 위 쪽 점을 연결할 수 없다는 것과 같다.
    그래서 그러한 경우의 수를 지우려면 N!으로 나누어 주어야 한다.

    그 과정은 brigeStruct라는 함수에서 이루어지고 결과 값을 리턴해준다.
'''


from sys import stdin

def bridgeStruct(n, m) :
    total = 1
    fact = 1
    site = m

    for i in range(n) :
        total *= site
        site -= 1

    for j in range(1, n + 1) :
        fact *= j

    return total/fact

result = []
testCase = int(stdin.readline())

for i in range(testCase) :
    N, M = stdin.readline().split()
    N = int(N)
    M = int(M)
    result.append(int(bridgeStruct(N, M)))

for j in result :
    print(j)