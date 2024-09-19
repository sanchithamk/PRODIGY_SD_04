def print_board(board):
    """Print the Sudoku board."""
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print()

def find_empty_location(board):
    """Find an empty location in the board (represented by 0)."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

def is_safe(board, row, col, num):
    """Check if it's safe to place num in the given row and column."""
    # Check if num is not in the current row
    if num in board[row]:
        return False
    
    # Check if num is not in the current column
    if num in [board[r][col] for r in range(9)]:
        return False
    
    # Check if num is not in the current 3x3 sub-grid
    start_row, start_col = row - row % 3, col - col % 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    
    return True

def solve_sudoku(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty_location = find_empty_location(board)
    if not empty_location:
        return True  # No empty location means the board is solved

    row, col = empty_location
    
    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0  # Undo the move
    
    return False

def main():
    # Example Sudoku puzzle (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Original Sudoku Puzzle:")
    print_board(board)

    if solve_sudoku(board):
        print("Solved Sudoku Puzzle:")
        print_board(board)
    else:
        print("No solution exists.")

# Run the program
if __name__ == "__main__":
    main()
