i=1

def solution(A):
    global i;
    if i not in A:
        return i

    i += 1
    return solution(A)


print(solution([1,3,6,4,1,2]))