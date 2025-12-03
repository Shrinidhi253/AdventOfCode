def check_repeated_seq(main_seq):
    main_seq_len = len(main_seq)
    sub_seq = main_seq[ : main_seq_len // 2]

    return sub_seq * 2 == main_seq
        
def get_sum_invalid(lower, upper):
    sum_invalid = 0
    for num in range(lower, upper + 1):
        is_invalid = check_repeated_seq(str(num))

        if is_invalid:
            sum_invalid += num

    return sum_invalid

def main():
    IDs = []

    with open("src/2025/day02/day02_IDs_data.txt") as file:
        IDs = file.readline().split(",")
    
    sum_invalid = 0

    for range in IDs:
        lower, upper = range.split("-")
        lower, upper = int(lower), int(upper)

        sum_invalid += get_sum_invalid(lower, upper)

    print("Sum invalid:", sum_invalid)

if __name__ == "__main__":
    main()