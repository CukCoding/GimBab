def add(a, b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a//b)

def mod(a,b):
    print(a%b)

num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)

add(num1, num2)
sub(num1, num2)
mul(num1, num2)
div(num1, num2)
mod(num1, num2)