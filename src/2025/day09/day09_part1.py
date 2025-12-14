def get_max_area(red_tiles_positions):
    max_area = 0

    for i in range(len(red_tiles_positions) - 1):
        x1, y1 = red_tiles_positions[i]

        for j in range(i+1, len(red_tiles_positions)):
            x2, y2 = red_tiles_positions[j]

            if (x1 != x2) and (y1 != y2):
                length = abs(x2 - x1) + 1
                width = abs(y2 - y1) + 1
                area = length * width

                if area > max_area:
                    max_area = area
    
    return max_area


def main():
    red_tiles_positions = []

    with open("src/2025/day09/day09_tiles_data.txt") as file:
        for line in file:
            x, y = line.strip().split(",")
            red_tiles_positions.append((int(x), int(y)))

    max_area = get_max_area(red_tiles_positions)

    print("Max area:", max_area)


if __name__ == "__main__":
    main()