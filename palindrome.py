# 어떤 문자열이 회문인지 판단하는 알고리즘 작성허긔

def palindrome(str):

    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return False

    return True

data1 = 'abcdcba'
data2 = 'akaaka'
data3 = 'abcdefg'

result1 = palindrome(data1)
result2 = palindrome(data2)
result3 = palindrome(data3)

if result1:
    print("data1은","회문입니다")
else :
    print("data1은","회문이 아닙니다.")

if result2:
    print("data2은","회문입니다")
else :
    print("data2은","회문이 아닙니다.")

if result3:
    print("data3은","회문입니다")
else :
    print("data3은","회문이 아닙니다.")