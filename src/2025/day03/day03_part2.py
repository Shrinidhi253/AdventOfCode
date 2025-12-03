"""
consider a num_string of len >= 12: abcdefghijklmnopqrstuvwxyz

the largest possible number will have the largest possible first digit, 
but there must be at least 11 digits after this first digit (because we need a 12-digit number)

    1. find the largest digit from: abcdefghijklmno
    2. if largest digit is o, then the largest number has to be opqrstuvwxyz
    3. if it is for e.g. f, then look for 2nd digit from ghijklmnop (there needs to be at least 10 numbers after the 2nd digit)
    and so on

"""

def get_max_joltage(num_string, max_joltage = "", start_ind = 0, nums_remaining = 12):
    if start_ind + nums_remaining >= len(num_string):
        return max_joltage + num_string[start_ind:]
    
    elif nums_remaining == 0:
        return max_joltage
    
    else:
        end_ind = len(num_string) - nums_remaining
        largest_digit, largest_digit_ind = find_largest_digit(num_string[start_ind : end_ind + 1], start_ind)

        return get_max_joltage(num_string, 
                               max_joltage = max_joltage + largest_digit, 
                               start_ind = largest_digit_ind + 1, 
                               nums_remaining = nums_remaining - 1)


def find_largest_digit(num_string, start_ind):
    largest_digit = 0
    largest_digit_ind = 0
    
    for i in range(len(num_string)):
        if int(num_string[i]) > largest_digit:
            largest_digit = int(num_string[i])
            largest_digit_ind = i

    largest_ind_numstring = largest_digit_ind + start_ind #to convert the index of the largest digit in the substring to its index in the main string

    return str(largest_digit), largest_ind_numstring


def main():
    joltages = []

    with open("src/2025/day03/day03_joltage_data.txt") as file:
        for line in file:
            joltages.append(line.strip())

    sum_max_joltage = 0

    for joltage in joltages:
        max_joltage = get_max_joltage(joltage)
        sum_max_joltage += int(max_joltage)

    print("Sum max joltages:", sum_max_joltage)

if __name__ == "__main__":
    main()