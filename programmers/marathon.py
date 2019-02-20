def solution(participant, completion):
    answer = ''
    map = {}

    for data in participant:
        if data in map:
            map[data] += 1
        else:
            map[data] = 1

    for check in completion:
        if check in map:
            map[check] -= 1
            if map[check] == 0:
                del map[check]
        else:
            return check

    answer = list(map.keys())[0]
    return answer


data1 = ["leo", "kiki", "eden"]
compare1 = ["eden", "kiki"]
print(solution(data1,compare1))

data2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
compare2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(data2,compare2))

data3 = ["mislav", "stanko", "mislav", "ana"]
compare3 = ["stanko", "ana", "mislav"]
print(solution(data3,compare3))
