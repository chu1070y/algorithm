def solution(B):
    O_idx = []
    X_idx = []

    # 장기말들의 인덱스 구하기
    for idx, str in enumerate(B):
        if str.find('O') != -1:
            O_idx = [idx, str.index('O')]
            continue

        if str.find('X') != -1:
            for i in range(len(str)):
                if str[i] == 'X':
                    X_idx.append([idx,i])

    # 구현 코드
    def chess(index, count=0):
        left = count
        right = count

        # 왼쪽
        if [index[0]-1, index[1]-1] in X_idx:

            if index[0] - 2 < 0 or index[1] - 2 < 0:
                None
            elif [index[0]-2, index[1]-2] in X_idx:
                None
            else:
                left = chess([index[0]-2, index[1]-2], count + 1)

        # 오른쪽
        if [index[0] - 1, index[1] + 1] in X_idx:

            if index[0] - 2 < 0  or index[1] + 2 > (len(B[0]) - 1):
                None
            elif [index[0] + 2, index[1] + 2] in X_idx:
                None
            else:
                right = chess([index[0] - 2, index[1] + 2], count + 1)


        # 결과 출력
        if left > right:
            result = left
        else:
            result = right

        return result

    return chess(O_idx)



B = ["","","","","",""]
B[0] = "..X..."
B[1] = "......"
B[2] = "....X."
B[3] = ".X...."
B[4] = "..X.X."
B[5] = "...O.."
print(solution(B))
