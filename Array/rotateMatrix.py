class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while l < r :
            for i in range(r- l):
                top, bottom = l, r
                
                # Save the topleft
                topleft = matrix[top][l + i]

                # Move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move bottom right into botton left
                matrix[bottom - i][l] = matrix[bottom][r - i] 

                # Move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move saved top left into top right
                matrix[top + i][r] = topleft
            
            # Increment and decrement left right pointers
            l += 1
            r -= 1

img = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 6]
]
print(img) # Original 
s = Solution()
s.rotate(img)
print(img) # After rotation