class matrixOps:
    def __init__(self,A:list[list[int]]):
        self.A = A
        self.m = len(A) # number of rows
        self.n = len(A[0]) # number of columns

    def performOps(self) -> list[list[int]]:
        B = [] # new 2d array : empty
        for i in range(len(self.A)): # access rows in the 2d array
            B.append([0]*self.n) # appeding n zeros in each row
            for j in range(len(self.A[i])): # access columns in the row
                B[i][self.n-1-j] = self.A[i][j]
        return B

if __name__ == "__main__":
    row = int(input("Enter number of rows : "))
    col = int(input("Enter number of columns : "))
    print("Enter elements of matrix press enter after each entry: ")
    matrix = []
    for i in range(row): # for loop for rows
        a = []
        for j in range(col): # for loop for col entries
            a.append(int(input()))
        matrix.append(a)
obj = matrixOps(matrix)
print(obj.performOps())

