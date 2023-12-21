# Fill the nxn matrix in the spiral fashion by integers in ascending order
class Matrix:
    def fillMatrixSpiral(self, n: int) -> list[list[int]]:
        mat = [[0] * n] * n
        
        # Pointers initialization
        l, r, t, b = 0, n-1 , 0, n-1
        count = 1
        
        while l <= r:
            # left to right
            for col in range(l, r + 1):
                mat[t][col] = count
                count += 1
            t += 1 # readjusting the top pointer
            
            # top to bottom
            for row in range(t, b + 1):
                mat[row][r] = count
                count += 1
            r -= 1 # readjusting the right pointer
            
            # right to left
            for col in range(r, l - 1, -1):
                mat[b][col] = count
                count += 1
            b -= 1 # readjusting the bottom pointer
            # bottom to top
            for row in range(b, t - 1, -1):
                mat[row][t] = count
                count += 1
            l += 1 # readjusting the left pointer

        return mat
            
grid = Matrix()
print(grid.fillMatrixSpiral(4))

        