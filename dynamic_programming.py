# 중간 값을 배열에 저장하여 나중에 필요할 때 함수를 호출하지 않고 배열에서 결과 추출
# 불필요한 함수를 줄일 수 있다.
print("--cashing--")
f = [-1] * 100

def fib1(n):
    if n <= 1:
        f[n] = 1
        return 1
    elif f[n] > -1:
        return f[n]
    else:
        f[n] = fib1(n-2) + fib1(n-1)
        return f[n]

fib1(10)
print(f)

# 재귀 호출이 아닌 반복문을 통해 구하는 방법
# 반복문이 꼭 나쁜 것만은 아니다.
print("--Bottom up--")
f = [1] * 100

def fib2(n):
    f[1] = f[2] = 1
    for i in range(2,n+1):
        f[i] = f[i-1] + f[i-2]
    return f[n]

fib2(10)
print(f)


# 동적계획법의 단점: 모든 상황을 검토하기 때문에 매번 주어진 모든 상황에 대해 검토하는데 많은 시간이 필요하다.
# 이를 대체하는 방법으로 그리디 알고리즘이 있다. (경우에 따라서만)
# 동적계획법이 모든 상황을 감안해서 최적의 경로를 찾아낸다면 그리디 알고리즘은 전체적인 상황을 고려하지 않고, 그 순간순간에서 가장 빠른 경로를 검색하여 찾아주는 것이다.
# 동적계획법은 판단하기 위한 약간의 시간이 필요하고 그리디 알고리즘은 즉효성이 있는 대신 최적의 경로를 찾아주지는 않는다.



