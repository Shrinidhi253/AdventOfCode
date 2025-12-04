"""
data = [
col: 0123456789    row:
    "..@@.@@@@.",   0
    "@@@.@.@.@@",   1
    "@@@@@.@.@@",   2
    "@@.@@@@.@@",   3
    ".@@@@@@@.@",   4
    ".@.@.@.@@@",   5
    "@.@@@.@@@@",   6
    ".@@@@@@@@.",   7
    "@.@.@@@.@."    8
]

let current_row = r, current_col = c
the 8 adjacent positions are: 
    (r, c+1), (r, c-1),
    (r+1, c), (r-1, c),
    (r+1, c+1), (r+1, c-1),
    (r-1, c+1), (r-1, c-1)

r+1 exists only if r < total_rows -1
r-1 exists only r > 0
c+1 exists only if c < total_cols - 1
c-1 exists only if c > 0

idea:
    1. go through each element, check its 8 adjacent positions
    2. if adjacent_position = "@", num_rolls += 1
    3. if num_rolls >= 4, move to the next position
    4. else accessible_rolls += 1
"""

def check_adjacent_positions(data, current_row, current_col):
    num_rolls = 0

    total_rows = len(data)
    total_cols = len(data[0])

    next_row_exists = True
    next_col_exists = True
    prev_row_exists = True
    prev_col_exists = True

    if current_row >= total_rows - 1:
        next_row_exists = False
    if current_row <= 0:
        prev_row_exists = False
    if current_col >= total_cols - 1:
        next_col_exists = False
    if current_col <= 0:
        prev_col_exists = False

    #Find the number of toilet rolls in the adjacent positions
    if next_col_exists and data[current_row][current_col + 1] == "@": #checks (r, c+1)
        num_rolls += 1

    if prev_col_exists and data[current_row][current_col - 1] == "@": #checks (r, c-1)
        num_rolls += 1

    if next_row_exists and data[current_row + 1][current_col] == "@": #checks (r+1, c)
        num_rolls += 1

    if prev_row_exists and data[current_row - 1][current_col] == "@": #checks (r-1, c)
        num_rolls += 1

    if next_row_exists and next_col_exists and data[current_row + 1][current_col + 1] == "@": #checks (r+1, c+1)
        num_rolls += 1

    if next_row_exists and prev_col_exists and data[current_row + 1][current_col - 1] == "@": #checks (r+1, c-1)
        num_rolls += 1

    if prev_row_exists and next_col_exists and data[current_row-1][current_col+1] == "@": #checks (r-1, c+1)
        num_rolls += 1

    if prev_row_exists and prev_col_exists and data[current_row - 1][current_col - 1] == "@": #checks (r-1, c-1)
        num_rolls += 1

    
    if num_rolls < 4:
        return True
    else:
        return False
    
def main():
    data = []

    with open("src/2025/day04/day04_rolls_data.txt") as file:
        for line in file:
            data.append(line.strip())

    accessible_rolls = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "@" and check_adjacent_positions(data, i, j):
                accessible_rolls += 1

    print("Num accessible rolls:", accessible_rolls)

if __name__ == "__main__":
    main()