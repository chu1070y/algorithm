# 메모리 오류 뜸
def solution(ranks):
    arr = [0]*(max(ranks)+1)

    for i in ranks:
        arr[i] += 1

    result = 0;

    for j in range(len(arr)-1):
        if arr[j] == 0 :
            continue
        if arr[j+1] == 0 :
            continue
        result += j
    return result

# 최종코드
def solution2(ranks):
    result = 0

    for i in ranks:
        if i+1 in ranks:
            result += 1

    return result

print(solution2([3,4,3,0,2,2,3,0,0]))
print(solution2([1000000000,999999999,1,2,3,4,2,1,2,1,50,76,77]))