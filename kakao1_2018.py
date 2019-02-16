def solution(record):

    nickname = {}

    for one in record:
        temp = one.split()
        if temp[0] != 'Leave':
            nickname[temp[1]] = temp[2]

    answer = []

    for two in record:
        temp = two.split()
        if temp[0] == 'Enter':
            answer.append(nickname[temp[1]]+"님이 들어왔습니다.")
        elif temp[0] == 'Leave':
            answer.append(nickname[temp[1]] + "님이 나갔습니다.")

    return answer


data = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(data))