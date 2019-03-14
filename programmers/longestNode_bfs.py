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
        queue = [start]
        visited = []
        cnt = 0

        while queue:
            pop = queue.pop(0)

            if pop == end:
                return cnt

            if pop not in visited:
                visited.append(pop)
                queue += set(map[pop]) - set(visited)

            cnt += 1

    for i in range(2,n+1):
        count[i] = loof(1,i)

    print(count)

    return answer

a = solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
print(a)
