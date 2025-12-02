def check_repeated_seq(main_seq, current_seq_len = 1):
    current_sub_seq = main_seq[:current_seq_len]

    if current_seq_len >= 0.5 * len(main_seq): #base case: minimum repetition = 2, when half the seq gets repeated
        return (current_sub_seq * 2 == main_seq)
    
    else:
        num_repetitions = len(main_seq) // current_seq_len #a sub_seq of length 2 must repeat 3 times in a main_seq of length 6

        if current_sub_seq * num_repetitions == main_seq:
            return True
        else:
            return check_repeated_seq(main_seq, current_seq_len + 1)


def get_sum_invalid(lower, upper):
    sum_invalid = 0
    for num in range(lower, upper + 1):
        is_invalid = check_repeated_seq(str(num))

        if is_invalid:
            sum_invalid += num

    return sum_invalid


def main():
    IDs = []

    with open("./src/2025/day02_IDs_data.txt") as file:
        IDs = file.readline().split(",")

    sum_invalid = 0

    for range in IDs:
        lower, upper = range.split("-")
        lower, upper = int(lower), int(upper)

        sum_invalid += get_sum_invalid(lower, upper)

    print("Sum invalid:", sum_invalid)

if __name__ == "__main__":
    main()