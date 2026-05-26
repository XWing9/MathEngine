#responsible for add, subtract, scalar multiply, matmul ig
#it's about combining matrices together it's arithmetic

def addition(self,other):
    values = []
    for i in range(self.rows):
        row = []
        for colIndex in range(self.cols):
            result = self.values[i][colIndex] + other.values[i][colIndex]
            row.append(result)
        values.append(row)
    return values

def subtraction(self,other):
    values = []
    for i in range(self.rows):
        row = []
        for colIndex in range(self.cols):
            result = self.values[i][colIndex] - other.values[i][colIndex]
            row.append(result)
        values.append(row)
    return values

def scalarMulti(self,scaler):
    values = []
    for i in range(self.rows):
        row = []
        for colIndex in range(self.cols):
            result = self.values[i][colIndex] * scaler
            row.append(result)
        values.append(row)
    return values


def matrixMulti(self, other):
    values = []
    if self.cols != other.rows:
        print("cant multiply") #rework error message
        return None
    for rowIndex in range(self.rows):
        endResult = 0
        row = []

        for colIndex in range(other.cols):
            endResult = 0
            count = 0
            for i in range(self.cols):
                result = self.values[rowIndex][i] * other.values[i][colIndex]
                endResult += result
            row.append(endResult)

        values.append(row)
    return values

def hadamardMatrix(self):
    pass

def powerMatrix(self,power):
    pass
# multiplication rules
# 2 matrix needs to have the amount of col the first has rows
#since its every num row wise in the first matrix
#gets multiplied by every num colum wise in the second matrix
# so example:
# A:          B:
# [ 1  2 ]    [ 5  6 ]
# [ 3  4 ]    [ 7  8 ]
# Row 1 from A times col 1 from B:
# 1,2 * 5,7 = (1*5) + (2*7)