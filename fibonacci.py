print("--반복문 이용--")

def fibonacci(n):
    a=0
    b=1

    if n == 0:
        return 0

    for i in range(1,n+1):
        c = a
        a += b
        b = c

    return a

for i in range(15):
    print(fibonacci(i), end=" ")

print("")
print("")
print("--재귀함수 이용--")

def fibonacci_recursion(n):

    if n==1:
        return 1

    if n==0:
        return 0

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

for i in range(15):
    print(fibonacci_recursion(i), end=" ")

print("")
print("")
print("--동적계획법 이용--")

def fibonacci_array(n):
    arr = [0,1]

    for i in range(2,n):
        arr.append(arr[i-1] + arr[i-2])

    return arr

print(fibonacci_array(15))


