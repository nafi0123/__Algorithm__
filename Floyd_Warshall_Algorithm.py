class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = float('inf')
                if i == j:
                    matrix[i][j] = 0
        

        

V = 4
matrix = [[-1] * V for _ in range(V)]
matrix[0][1] = 2
matrix[1][0] = 1
matrix[1][2] = 3
matrix[3][0] = 3
matrix[3][1] = 5
matrix[3][2] = 4

obj = Solution()
obj.shortest_distance(matrix)

for row in matrix:
    print(" ".join(map(str, row)))
