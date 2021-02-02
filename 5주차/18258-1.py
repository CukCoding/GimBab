from sys import stdin

'''
    C처럼 짰으나 어떻게 하든 시간초과가 되어버린다.
    queue1, queue2 둘 다 시간초과 클래스
    
    해결하기 위해서 파이썬 내장 디큐를 이용한다
'''
class queue1 :
    def __init__(self):
        self.cnt = 0
        self.arr = []

    def push(self, num):
        self.cnt += 1
        self.arr.append(num)

    def pop(self):
        if self.cnt == 0 :
            return -1
        else :
            temp = self.arr[0]
            del self.arr[0]
            self.cnt -= 1
            return temp

    def size(self):
        return self.cnt

    def isEmpty(self):
        if self.cnt == 0 :
            return -1
        else :
            return 0

    def front(self):
        if self.cnt == 0 :
            return -1
        else :
            return self.arr[0]

    def back(self):
        if self.cnt == 0 :
            return -1
        else :
            return self.arr[self.cnt - 1]

class queue2():
    def __init__(self):
        self.arr = []
    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if len(self.arr) == 0 :
            return -1
        else :
            return self.arr.pop(0)

    def size(self):
        return len(self.arr)

    def isEmpty(self):
        if self.size() == 0 :
            return 1
        else :
            return 0

    def front(self):
        if self.size() == 0 :
            return -1
        else :
            return self.arr[0]

    def back(self):
        if self.size() == 0 :
            return -1
        else :
            return self.arr[-1]
testCase = int(stdin.readline())
q = queue2()
for i in range(testCase) :
    cmd = stdin.readline().split()
    if cmd[0] == 'push' :
        q.push(cmd[1])
    elif cmd[0] == 'pop' :
        print(q.pop())
    elif cmd[0] == 'size' :
        print(q.size())
    elif cmd[0] == 'empty' :
        print(q.isEmpty())
    elif cmd[0] == 'front' :
        print(q.front())
    elif cmd[0] == 'back' :
        print(q.back())