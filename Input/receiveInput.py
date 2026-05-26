# file to collect user input
from random import choice
from Engine.Matrices import Matrix

topicsList = ["matrices", "vectors"]

def printStart():
    for topic in topicsList:
        print(topic)
    userInput = input("Enter topics first Letter: ")
    determineOperation(userInput)

def determineOperation(userInput):
    match userInput:
        case "m":
           printMatrices()
        case _:
            print("no valid topic")

def printMatrices():
    matricesOperations = ["1. Addition", "2. Subtraction","3. Matrix multiplication ",
                          "4. Scalar multiplication", "5. Transpose ", "6. Determinant",
                          "7. Inverse"]

    matrices = []
    result = None

    for operation in matricesOperations:
        print(operation)
    operation = int(input("Enter operations Number: "))

    #write smth that i dont need to write 2 matrices when i dont need them
    if operation > 3:
        matricesNum = 1
    else:
        matricesNum = 2

    for matrixNumber in range(matricesNum):
        matrixVals = []
        rows = int(input(f"Enter number of rows for matrix {matrixNumber + 1}: "))
        columns = int(input(f"Enter number of columns for matrix {matrixNumber + 1}: "))
        for rowIndex in range(rows):
            row = []

            for columnIndex in range(columns):
                value = int(input(f"Enter value for matrix {matrixNumber + 1}, row {rowIndex + 1}, column {columnIndex + 1}: "))
                row.append(value)
            matrixVals.append(row)

        matrix = Matrix(matrixVals)
        matrices.append(matrix)

    print("Entered Matrices:")
    for matrix in matrices:
        print(matrix.toString())

    match operation:
        case 1:
            result = matrices[0].addition(matrices[1])
        case 2:
            result = matrices[0].subtraction(matrices[1])
        case 3:
            result = matrices[0].scalerMulti(int(input("Enter scalar: ")))
        case 4:
            result = matrices[0].matrixMulti(matrices[1])
        case 5:
            result = matrices[0].transpose()
        case 6:
            result = matrices[0].returnDeterminant()
        case 7:
            result = matrices[0].inverseMatrix()

    if operation == 6:
        print(f"Determinant of matrix \n {matrices[0].toString()} is {result}")
    else:
        print("Result Matrix:\n" + result.toString())