# for storing the minimum falling sum
sum = 0
# to store each path
path = []

def solution(matrix, row, col):
    global sum, path
    # checking for limits
    if row < 0 or row > len(matrix)-1 or col < 0 or col > len(matrix[0])-1:
        # if path is not completed yet then return
        if len(path) != len(matrix):
            return
        # otherwise get the sum of path
        t = 0
        for i in path:
            t += i
        if sum == 0 or t < sum:
            sum = t
        return
    # traversing the whole first row
    solution(matrix, row, col+1)
    # appending each coordinate in matrix
    path.append(matrix[row][col])
    # traversing the whole falling path
    solution(matrix, row + 1, col - 1)
    solution(matrix, row + 1, col)
    solution(matrix, row + 1, col + 1)
    # at the end we also need to empty the path to store other paths
    path.pop()

# entrypoint
def main():
    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    solution(matrix, 0, 0)
    print(sum)
 

if __name__ == "__main__":
    main()