def solution(n, edge):
    answer = 0
    map = {}
    count = {}

    # 데이터 추리긔
    for data in edge:

        if map.get(data[0]) == None:
            map[data[0]] = [data[1]]
        else:
            map.get(data[0]).append(data[1])

        if map.get(data[1]) == None:
            map[data[1]] = [data[0]]
        else:
            map.get(data[1]).append(data[0])

    print(map)

    # 떨어진 노드 count 세긔
    def loof(start, end, cnt = [1]):

        if cnt.count(start) == 2:
            return

        # 불필요한 노드 계산하지 말긔
        if count.get(end) != None:
            if count.get(end) <= len(cnt):
                return

        if end in map.get(start):
            count[end] = len(cnt)
            return

        for i in map.get(start):
            temp = cnt[:]
            temp.append(i)
            loof(i, end, temp)

    for j in range(2,n+1):
        loof(1,j)

    print(count)

    big = max(count.values())

    for key in count.keys():
        if count.get(key) == big:
            answer = answer + 1

    return answer

a = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)
