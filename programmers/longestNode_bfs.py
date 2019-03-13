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
    def loof(start, end):
        queue = [(start,[start])]
        cnt = 0

        while queue:
            n, path = queue.pop(0)
            if n == end:
                cnt += 1


    return answer

a = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)
