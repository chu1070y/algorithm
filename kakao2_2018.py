
# 항상 조건 잘 확인하자 ㅠㅠ
def solution(N, stages):
    fail = {}
    answer = []
    number = len(stages)

    for i in range(1, N + 1):
        count = stages.count(i)

        if number == 0 :
            fail[i] = 0
            continue
        fail[i] = count / number
        number = number - count

    print(fail)

    answer = sorted(fail, key=fail.__getitem__, reverse=True)

    return answer


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))