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
    

def recursive_check(data, total_removed_rolls = 0):
    removed_rolls_positions = [] #list of positions of the removed rolls 
    
    new_rolls = 0
    for i in range(len(data)):
        for j in range(len(data[0])):

            if data[i][j] == "@":
                is_accessible = check_adjacent_positions(data, i, j)

                if is_accessible:
                    new_rolls += 1
                    removed_rolls_positions.append((i, j))

    if new_rolls == 0:
        return total_removed_rolls
    
    else:
        for i, j in removed_rolls_positions:
            data[i] = data[i][:j] + "." + data[i][j+1:] #update the removed rolls from "@" to "."

        return recursive_check(data, total_removed_rolls + new_rolls)


def main():
    data = []

    with open("src/2025/day04/day04_rolls_data.txt") as file:
        for line in file:
            data.append(line.strip())

    total_removed_rolls = recursive_check(data)

    print("Num removed rolls:", total_removed_rolls)

if __name__ == "__main__":
    main()