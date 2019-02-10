# 3x3행렬 중 합이 최소가 되는 항목 선택허긔
# 각 행과 열이 중복되지 않도록 숫자를 선택하고, 선택한 숫자들의 최소값을 구하는 알고리즘

class MatrixMinimum:

    def __init__(self, data):
        self.idx = [False] * len(data[0])
        self.data = data
        self.count = len(data[0])
        self.sum = 0
        self.min = 100000

    def find(self, row = 0):

        if row == 3:
            if self.sum < self.min:
                self.min = self.sum
                return self.min

        for i in range(self.count):
            if self.idx[i] == False:
                self.sum += self.data[row][i]
                self.idx[i] = True
                self.find(row+1)
                self.idx[i] = False

        self.sum = 0
        return self.min


matrix = [[1, 5, 3], [2, 5, 7], [5, 3, 5]]
result = MatrixMinimum(matrix)
result.find()
print(result.min)

