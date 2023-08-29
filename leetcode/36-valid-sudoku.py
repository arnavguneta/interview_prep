import collections
def isValidSudoku(board) -> bool:
    seen_cols = {x: [0 for _ in range(9)] for x in range(9)}
    seen_rows = {x: [0 for _ in range(9)] for x in range(9)}
    squares = {(x,y): [0 for _ in range(9)] for x in range(3) for y in range(3)}
    
    for i, row in enumerate(board):
        seen_rows = [0 for _ in range(9)]
        for j, column in enumerate(row):
            if '.' == column: continue
            column = int(column)
            if seen_rows[column-1] > 0:
                return False
            seen_rows[column-1] = 1
            if seen_cols[j][column-1] > 0:
                return False
            seen_cols[j][column-1] = 1
            if squares[(i//3,j//3)][column-1] > 0 or squares[(i//3,j//3)][column-1] > 0:
                return False
            squares[(i//3,j//3)][column-1] = 1
            
    return True

# could have used hash set for better space complexity