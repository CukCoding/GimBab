import sys
r = sys.stdin.readline

mushroom = [] # 입력받는 버섯 점수 저장
score = 0
gap = 0

for i in range(10) :
    mushroom.append(int(r()))

score += mushroom[0] #첫번째 값을 넣어놓는다
gap = 100 - score #첫번째 값과 100과의 차이를 미리 집어넣는다
for i in range(1, 10) : #배열의 두번째 값부터 비교 시작
    score += mushroom[i] #score는 계속 더해주고
    temp = 100 - score
    if temp < 0 : #100과의 차이가 음수일경우 다시 양수로 바꿔주는 과정을 거쳐서 갭을 항상 양수로 유지
        temp *= -1
    if gap > temp : #전의 스코어와의 차이가 현재보다 차이가 클경우 현재의 점수와의 차이를 갭에 새롭게 저장
        gap = temp
    elif gap < temp : #전의 스코어와의 차이가 현재보다 차이가 작을경우 전의 값이 정답이므로 현재 스코어누적값에서 방금 더한 값을 뺀다
        score -= mushroom[i]
        break
    elif gap == temp : #전의 스코어와의 차이가 똑같으면 더 큰 누적점수를 출력해야하므로 그냥 브레이크 해준다
        break

print(score)