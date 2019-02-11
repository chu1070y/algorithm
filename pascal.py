# 파스칼 삼각형 출력허긔

def pascal(n,blank=0):

    if n == 0:
        print(" " * (blank-1),1)
        return

    pascal(n-1,blank+1)

    print(" " * blank, end="")
    for i in range(n+1):
        print(comb(n,i) , end=" ")
    print("")

def comb(n, r):
    if r == 0:
        return 1
    return int(comb(n, r - 1) * (n - r + 1) / r)

pascal(7)