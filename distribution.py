a = [75,25,6,73,43,46,31,13,60,90,5,43,35,65,100,28,83,95,35,45,-1]

# for문 이용
def dist(data):

    result = [0]*11

    for num in data:

        if num == -1:
            break
        result[num//10] += 1

    return result

count = dist(a)

for i in range(11):
    print("{0} 점대 : {1}명".format(i*10,count[i]))

print("")

print("--재귀함수 이용--")
# 재귀함수 이용
result_cur = [0]*11

def dist_cur(data):

    if data[0] == -1:
        return

    result_cur[data.pop(0)//10] += 1

    dist_cur(data)

dist_cur(a)

for i in range(11):
    print("{0} 점대 : {1}명".format(i*10,result_cur[i]))