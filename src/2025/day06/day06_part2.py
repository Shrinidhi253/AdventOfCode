"""
Idea:
123 328  51 64 
 45 64  387 23 
  6 98  215 314

1 2 3 _ 3 2 8 _ _ 5 1 _ 6 4 _ 
_ 4 5 _ 6 4 _ _ 3 8 7 _ 2 3 _ 
_ _ 6 _ 9 8 _ _ 2 1 5 _ 3 1 4

Some spaces (_) are boundaries between columns, some spaces align the numbers as needed
When a space is a boundary, all rows have a space at that index

j = 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
    1 2 3 | 3 2 8 | _ 5 1  |  6  4  _ 
    _ 4 5 | 6 4 _ | 3 8 7  |  2  3  _ 
    _ _ 6 | 9 8 _ | 2 1 5  |  3  1  4

current_col = 0
cepha_nums = []
for each j , j <= 14:
    check if j is a boundary
    false:
        cepha_num  = ""
        for each row:
            cepha_num += row_num or space

        add cepha_num to cepha_nums

    true:
        get operation for current_col
        if operation == "+" -> return sum cepha_nums
        else -> return product cepha_nums
        reset cepha_nums = []
        current_col + 1
"""
import re

def is_boundary(number_rows, ind):
    i = 0
    while i < len(number_rows) and (number_rows[i][ind] == " " or number_rows[i][ind] == "\n"):
        i += 1

    boundary = True
    if i < len(number_rows):
        boundary = False
    
    return boundary


def calculate_cepha_total(number_rows, operations):
    grand_total = 0

    cepha_nums_for_col = []
    current_col = 0
    for j in range(len(number_rows[0])):

        if not is_boundary(number_rows, j):
            cepha_num = ""
            for i in range(len(number_rows)):
                cepha_num += number_rows[i][j]

            cepha_nums_for_col.append(int(cepha_num))

        else:
            operation = operations[current_col]
            if operation == "+":
                col_total = 0
                col_total = sum(cepha_nums_for_col)
            else:
                col_total = 1
                for num in cepha_nums_for_col:
                    col_total *= num

            current_col += 1
            cepha_nums_for_col = []
            grand_total += col_total

    return grand_total

def main():
    with open("src/2025/day06/day06_maths_data.txt") as file:
        all_rows = []
        for line in file:
            all_rows.append(line) #append everything except newline char

    operations = re.findall(r"[\*\+]", all_rows[-1])
    number_rows = all_rows[:-1]

    grand_total = calculate_cepha_total(number_rows, operations)
    print("Grand total:", grand_total)

if __name__ == "__main__":
        main()