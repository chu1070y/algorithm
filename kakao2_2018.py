
# 미완성
# 결과는 나오지만 런타임 에러 뜸...
def solution(N, stages):
    fail = {}
    answer = []
    number = len(stages)

    for i in range(1,N+1):
        count = 0
        if i in stages:
            count = stages.count(i)

        fail[i] = count/number
        number = number - count

    print(fail)

    answer = sorted(fail, key=fail.__getitem__, reverse=True)

    return answer


print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))