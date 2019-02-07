def binaryTreeCount(a,b):

    if a == b :
        return 0

    if a > b :
        return binaryTreeCount(a//2,b) + 1
    if a < b :
        return binaryTreeCount(a,b//2) + 1

print(binaryTreeCount(4,10))