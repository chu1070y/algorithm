def solution(n, edge):
    answer = 0
    map = {}
    count = {}

    # 데이터 추리긔
    for data in edge:

        if map.get(data[0]) == None:
            map[data[0]] = [data[1]]
            continue

        map.get(data[0]).append(data[1])

    print(map)

    # 떨어진 노드 count 세긔
    def loof(start, end, cnt):

        # 불필요한 노드 계산하지 말긔
        if count.get(end) != None:
            if count.get(end) <= cnt:
                print("111")
                return

        if start == end:
            print(count)
            count[end] = cnt
            return

        if map.get(start) == None:
            print("222")
            return

        for i in map.get(start):
            loof(i, end, cnt+1)

    for i in range(2,4):
        loof(1,i,0)

    return answer

a = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)
