class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        print(f"Matrix Start: [{len(matrix) = }]")
        print(*matrix, sep="\n")

        N = len(matrix)

        for l in range(N // 2):
            for i in range(N - 1 - 2 * l):    
                i = i + l
                edges = [(l,i), (-(i+1), l), (-1-l, -(i+1)), (i, -1-l)]
                # do the swaps
                for _ in range(3):
                    (a, b), (c, d) = edges[_], edges[_+1]
                    matrix[a][b], matrix[c][d] = matrix[c][d], matrix[a][b]
                    # print(f"Inter {i + 1}:{_ + 1}:")
                    # print(*matrix, sep="\n")

                print(f"Rotate {i+1}:")
                print(*matrix, sep="\n")