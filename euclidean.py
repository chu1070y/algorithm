a = int(input("첫 번째 숫자를 입력해주세요: "))
b = int(input("두 번째 숫자를 입력해주세요: "))

def euclidean(x,y):

    if y == 0:
        return x

    if y > x:
        x,y = y,x

    return euclidean(y,x%y)

print(euclidean(a,b))