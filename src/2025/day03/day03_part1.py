def get_max_joltage(num_string):
    max_joltage = 0

    for i in range(len(num_string)-1):
        for j in range(i+1, len(num_string)):
            num = int(num_string[i] + num_string[j])

            if num > max_joltage:
                max_joltage = num

    return max_joltage


def main():
    joltages = []

    with open("src/2025/day03/day03_joltage_data.txt") as file:
        for line in file:
            joltages.append(line.strip())

    sum_max_joltage = 0

    for joltage in joltages:
        sum_max_joltage += get_max_joltage(joltage)

    print("Sum max joltages:", sum_max_joltage)

if __name__ == "__main__":
    main()