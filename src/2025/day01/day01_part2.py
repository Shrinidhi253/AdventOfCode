MIN = 0
MAX = 99
START = 50

def get_rotation_val(current_val, direction, step):
    num_zeroes = 0
    while step > 0:
        if direction == "L":
            current_val -= 1
        else:
            current_val += 1

        if current_val > MAX:
            current_val = MIN

        elif current_val < MIN:
            current_val = MAX

        if current_val == 0:
            num_zeroes += 1

        step -= 1

    return current_val, num_zeroes

def main():
    rotations = []

    with open("src/2025/day01/day01_rotations_data.txt") as file:
        for line in file:
            rotations.append(line.strip())

    total_zeroes = 0
    current_val = START
    
    for rotation in rotations:
        direction, step = rotation[0], int(rotation[1:])

        current_val, num_zeroes = get_rotation_val(current_val, direction, step)

        total_zeroes += num_zeroes

    print("Num zeroes:", total_zeroes)

if __name__ == "__main__":
    main()