number = int(input("제곱근을 구할 숫자를 입력해주세요 : "))

def squareRoot(data):

    i = 0
    while data >= 0:

        i += 1
        data = data - (2*i-1)

    return i - 1

print(squareRoot(number))