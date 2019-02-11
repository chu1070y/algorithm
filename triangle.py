# 총 길이 n이 주어졌을 때, 만들 수 있는 삼각형의 갯수 구허긔

count = 0
duplicate = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

def triangle(n, a = 1, b = 1):
    global count
    c = n-a-b

    if a <= b and b <= c and a + b > c and duplicate[a][b][c] == 0:
        count += 1
        print(a, b, c)
        duplicate[a][b][c] = 1

    if n == a-1 or n == b-1 or a == c or b == c:
        return

    triangle(n,a+1,b)
    triangle(n,a,b+1)

triangle(10)
print(count)