class Solution:

    # @param A : tuple of list of integers

    # @return a list of integers

    def spiralOrder(self, A):

        colBegin = rowBegin = 0

        colEnd = len(A[0])-1

        rowEnd = len(A)-1

        arr = []

        

        while rowBegin <= rowEnd and colBegin <= colEnd:

            #traverse right

            for i in range(colBegin, colEnd+1):

                arr.append(A[colBegin][i])

            rowBegin += 1

            

            #travese down

            for i in range(rowBegin, rowEnd+1):

                arr.append(A[i][colEnd])

            colEnd -= 1

            

            #traverse left

            if rowBegin <= rowEnd:

                for i in range(colEnd, colBegin-1, -1):

                    arr.append(A[rowEnd][i])

                rowEnd -= 1

                

            #travers up

            if colBegin <= colEnd:

                for i in range(rowEnd, rowBegin-1, -1):

                    arr.append(A[i][colBegin])

                colBegin += 1

        return arr