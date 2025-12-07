def find_splits(manifold_data, path_indices = [], current_row = 0, num_splits = 0):
    if current_row == 0:
        start_index = manifold_data[0].index("S")
        return find_splits(manifold_data, [start_index], current_row + 2, num_splits = 0)

    elif current_row >= len(manifold_data):
        return num_splits
    
    else:
        #Check for each previous path index, if there is an obstacle
        new_paths = []
        new_splits = 0
        for path_index in path_indices:

            if manifold_data[current_row][path_index] == "^":
                new_splits += 1

                if (path_index + 1) not in new_paths:
                    new_paths.append(path_index + 1)
                if (path_index - 1) not in new_paths:
                    new_paths.append(path_index - 1)

            else:
                if path_index not in new_paths:
                    new_paths.append(path_index)

        return find_splits(manifold_data, new_paths, current_row + 2, num_splits + new_splits)


def main():
    manifold_data = []
    with open("src/2025/day07/day07_manifold_data.txt") as file:
        for line in file:
            manifold_data.append(line.strip())

    total_splits = find_splits(manifold_data)

    print("Total splits:", total_splits)

if __name__ == "__main__":
    main()