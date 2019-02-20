def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(len(phone_book)):

            if phone_book[i] == phone_book[j]:
                continue

            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False

    return answer

data = ["119", "97674223", "1195524421"]
print(solution(data))

aa = ["113", "12340", "123440", "12345", "98346"]
print(solution(aa))