#responsible for transpose, inverse, determinant ig
#it's about a property of a matrix itself it's linear

def transpose(self):
    values = []
    for colsIndex in range(self.cols):
        row = []
        for rowIndex in range(self.rows):
            row.append(self.values[rowIndex][colsIndex])

        values.append(row)
    return values

def listTranspose(values):
    newValues = []
    for colsIndex in range(len(values[0])):
        row = []
        for rowIndex in range(len(values)):
            row.append(values[rowIndex][colsIndex])

        newValues.append(row)
    return newValues

def returnDeterminant(values):
    #uses cofactor expansion
    determinant = 0

    rows = len(values)
    cols = len(values[0])

    if rows != cols:
        print("cant calculate determinant")
        return None
    elif rows == 2:
          return calcDeterminant(values)
    elif rows == 1:
        return values[0][0]
    else:
        for colIndex in range(cols):

            maCopy = shortenMatrix(values,colIndex,0)

            if colIndex % 2 == 0:
                determinant += values[0][colIndex] * returnDeterminant(maCopy)
            else:
                determinant -= values[0][colIndex] * returnDeterminant(maCopy)

        return determinant

def calcDeterminant(values):
    return (values[0][0] * values[1][1]) - (values[0][1] * values[1][0])

def shortenMatrix(values,colIndex,rowIndex):
    maCopy = [row.copy() for row in values]
    maCopy.pop(rowIndex)
    for row in maCopy:
      del row[colIndex]
    return maCopy

def inverseMatrix(self):
    values = []
    cofactorMa = []
    newMa = []
    determinant = returnDeterminant(self.values)

    if self.rows != self.cols:
        print("cant inverse")
        return None
    elif determinant == 0:
        print("cant inverse")
        return None
    else:
        for rowIndex in range(self.rows):
            row = []
            for colIndex in range(self.cols):
                minorMa = shortenMatrix(self.values,colIndex,rowIndex)
                if (colIndex + rowIndex) % 2 == 0:
                    row.append(returnDeterminant(minorMa))
                else:
                    row.append(-1 * returnDeterminant(minorMa))
            cofactorMa.append(row)

        newMa = listTranspose(cofactorMa)

        for rowIndex in range(self.rows):
            row = []
            for colIndex in range(self.cols):
                row.append(newMa[rowIndex][colIndex] / determinant)
            values.append(row)
    return values

def traceMatrices(self):
    pass

def rankMatrices(self):
    pass
#determine rules:
# having a 2*2 matrix like this:
# 1 2
# 3 4
# determinant = 1(1 * 4) - 2(2 * 3) = -8
# general rule is:
# det = 1 * det(first minor)
#     - 2 * det(second minor)
#     + 3 * det(third minor)
#     - 4 * det(fourth minor) etc
#  vor a 3*3 matrix its like this:
# [ row1 col1   row1 col2   row1 col3 ]
# [ row2 col1   row2 col2   row2 col3 ]
# [ row3 col1   row3 col2   row3 col3 ]
#when we say we have this matrix and want to calculate the determinant we do this:
# delete row1 col1 leaving us with 4, we do the 2*2 matrix thing an get an determine