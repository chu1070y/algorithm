num = int(input("숫자를 입력하세요: "))

def factorial(data):

    if data == 0:
        return 1

    result = 1
    for i in range(1,data+1):
        result = result * i

    return result

for i in range(num+1):
    print("{0}! = {1}".format(i,factorial(i)))

# 재귀함수
print("--재귀함수 이용--")
def factorial_recursion(data):

    if data == 0:
        return 1

    return factorial_recursion(data-1)*data

for i in range(num+1):
    print('%2d! = %10d' % (i, factorial_recursion(i)))


