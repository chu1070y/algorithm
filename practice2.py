
def solution(A):
    arr = [False] * len(A)

    def beadNumber(i, count=1):
        arr[i] = True

        if A[i] == initial:
            return count

        count += 1
        return beadNumber(A[i], count)

    if len(A)==0:
        return 0

    max = 0

    for j in range(len(A)):
        if arr[j] == True:
            continue

        initial = j
        result = beadNumber(j)
        if result > max:
            max = result

    return max


print(solution([5,4,0,3,1,6,2]))