import sys
r = sys.stdin.readline

N = int(r())
cnt = 0
for i in range(N) :
    before = []
    word = list(r().strip())

    if len(word) == 1 :
        cnt += 1
        continue
    else :
        b_wd = word[0] #이전 단어를 첫번째 단어로 설정
        before.append(b_wd) #이전에 나왔던 알파벳 목록 배열에 첫번째 단어를 넣는다
        for j in range(1, len(word)):  # 단어 하나를 한글자씩 탐색 시작 , 두번째 단어부터 시작한다
            check = 0
            if word[j] == b_wd: #이전 알파벳이랑 같은경우 다음 알파벳으로 컨티뉴
                continue
            else:
                for k in before: #이전에 나왔던 알파벳 배열의 요소들과 비교하기 위한 포문
                    if k == word[j]: # 이전에 나왔던 알파벳과 같을경우 반복문 종료하고 다음 단어로 넘어감 / check 를 1로 설정
                        check = 1
                        break

                if check == 1: # 반복문 다 돌고 체크가 1일경우 반복문 종료
                    break
                else: #체크가 1이 아니면 이전에 없던 알파벳이므로 이전 알파벳에 현재의 알파벳을 저장하고, 이전에 나왔던 알파벳 저장 배열에
                      #현재의 알파벳을 추가해준다. 그리고 다음 알파벳 탐색하기 위해 컨티뉴
                    b_wd = word[j]
                    before.append(b_wd)
                    continue
        if check == 0: #반복문이 다 끝낫을시 check가 0이면 그룹단어이므로 cnt를 1 올려준다
            cnt += 1

print(cnt)