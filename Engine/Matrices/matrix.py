from .operations import arithmetic as arith
from .operations import linear as lin

class Matrix:
    def __init__(self,values):
        self.values = values
        self.rows = len(values)
        self.cols = len(values[0])

    #arithmetic stuff
    def addition(self,other):
        return Matrix(arith.addition(self,other))

    def subtraction(self,other):
        return Matrix(arith.subtraction(self,other))

    def scalerMulti(self,scaler):
        return Matrix(arith.scalarMulti(self, scaler))

    def matrixMulti(self,other):
        return Matrix(arith.matrixMulti(self,other))

    #linear stuff
    def transpose(self):
        return Matrix(lin.transpose(self))

    def returnDeterminant(self):
        return lin.returnDeterminant(self.values)

    def inverseMatrix(self):
        return Matrix(lin.inverseMatrix(self))

    def toString(self):
        result = ""

        for row in self.values:
            result += str(row) + "\n"
        return result

# Matrix Operations (from simple to complex)
#
# Addition / Subtraction — both matrices must be the same size, you just add each matching element
# Scalar multiplication — multiply every element by a single number
# Matrix multiplication — the classic one, rows × columns
# Transpose — flip the matrix, rows become columns
#
# Determinant — a single number calculated from a matrix, tells you a lot about it (like whether an inverse exists)
# Inverse — like division for matrices. Only square matrices can have one, and only if the determinant isn't zero
#
# nex Implementations:
# Trace — sum of the diagonal elements of a square matrix. Very simple to implement
# Rank — how many rows are actually independent from each other (no row is just another row multiplied by something)
# Power — multiply a matrix by itself n times, like A³
# Hadamard product — element-wise multiplication, just multiply matching elements like addition
#
# Later:
# LU Decomposition — split a matrix into a lower and upper triangular matrix. Used as a stepping stone for solving equation systems
# QR Decomposition — another way to split a matrix, used a lot in numerical methods
# Solving linear equation systems — given Ax = b, find x. This is one of the most practically useful things matrices are used for
# Eigenvalues and Eigenvectors — a direction in which a matrix only stretches but doesn't rotate. Huge in physics, ML, and graphics
#
# SVD (Singular Value Decomposition) — the most powerful decomposition, used in everything from image compression to recommendation systems
# Matrix exponentiation — raising e to the power of a matrix, used in differential equations