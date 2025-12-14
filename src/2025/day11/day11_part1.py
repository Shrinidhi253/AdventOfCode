def find_reactor_paths(all_reactors, current_reactor = "you"):
    start_reactors = all_reactors[current_reactor]

    if start_reactors == ["out"]: #base case: 1 path because "out" signifies the end of a path
        return 1

    else:
        total_paths = 0

        for reactor in start_reactors:
            #get the number of paths for each individual reactor, and then add them together
            total_paths += find_reactor_paths(all_reactors, reactor)

        return total_paths

def main():
    all_reactors = {}

    with open("src/2025/day11/day11_reactors_data.txt") as file:
        for line in file:
            source_reactor, connected_reactors = line.split(":")
            connected_reactors = connected_reactors.strip().split(" ")

            all_reactors[source_reactor] = connected_reactors

    num_paths = find_reactor_paths(all_reactors)
    print("Num paths:", num_paths)

if __name__ == "__main__":
    main()