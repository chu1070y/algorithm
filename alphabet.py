def alphabet():

    for i in range(ord('Z')+1 - ord('A'), 0, -1):

        for j in range(ord('A'), ord('A') + i):
            print(chr(j), end=' ')
        print('')

alphabet()

print("")
print("--재귀함수 이용--")

def alphabet_recursion(num = ord('A'), i = ord('Z') - ord('A')):

    if num > ord('A') + i:
        if num == ord('A') + 1:
            return
        print("")
        return alphabet_recursion(ord('A'), i-1)

    print(chr(num), end=" ")
    alphabet_recursion(num+1,i)

alphabet_recursion()