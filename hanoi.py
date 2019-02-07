num = int(input("원반의 갯수: "))

def hanoi(n,here,by,arrive):
    if n > 0:
        hanoi(n-1,here,arrive,by)
        print("{0}번째 원반을 {1} 기둥에서 {2} 기둥으로 옮겼습니다.".format(n,here,arrive))
        hanoi(n-1,by,here,arrive)

hanoi(num,'a','b','c')
