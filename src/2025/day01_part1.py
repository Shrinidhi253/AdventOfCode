MIN = 0
MAX = 99
START = 50

def get_rotation_val(current_val, rotation):
    direction, step = rotation[0], int(rotation[1:])

    if direction == "L":
        rotation_val = current_val - step
    
    else:
        rotation_val = current_val + step

    wrapped_rotation_val = rotation_val % (MAX + 1)

    return wrapped_rotation_val

def main():
    rotations = []

    with open("src/2025/day01_rotations_data.txt") as file:
        for line in file:
            rotations.append(line.strip())

    num_zeroes = 0
    current_val = START
    i = 0

    while i < len(rotations):
        current_val = get_rotation_val(current_val, rotations[i])

        if current_val == 0:
            num_zeroes += 1

        i += 1

    print("Num zeroes:", num_zeroes)

if __name__ == "__main__":
    main()