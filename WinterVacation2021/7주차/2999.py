from sys import stdin

text = stdin.readline().strip()
count = len(text) #입력텍스트의 길이를 저장

arr = [] #길이의 약수를 저장할 배열

for i in range(1, count + 1) : #완전히 나눌수 있는 약수들을 arr배열에 저장
    if count % i == 0 :
        arr.append(i)

length = len(arr) # 약수의 갯수를 저장
if length % 2 == 1 : #약수의 갯수가 홀수 일 경우 R, C 는 같다 ex) 4 * 4 , 6 * 6 약수는 항상 짝이 맞는데 홀수라는 말은 거듭제곱
    R = arr[length // 2]
    C = R
else : #약수의 갯수가 짝수개면 중간의 두 수가 가장큰 R * C 가 된다
    R = arr[(length // 2) - 1]
    C = arr[length // 2]

matrix = [[0 for _ in range(R)] for _ in range(C)] #구한 R과 C를 토대로 2차원 배열 생성
for i in range(C) : #왼쪽에서 오른쪽 순으로 글자를 집어넣는다
    for j in range(R) :
        matrix[i][j] = text[(i * R) + j]

for i in range(R) : #위에서 아래 순으로 글자를 읽는다
    for j in range(C) :
        print(matrix[j][i], end="")