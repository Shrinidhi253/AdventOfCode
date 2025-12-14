"""
Keep track of whether a reactor path has visited dac or fft instead of storing the whole sequence of paths
path_status of a reactor = is the name of the reactor + whether this reactor has visited dac and fft previously
"""

def find_reactor_paths(all_reactors, current_reactor, visited_dac = False, visited_fft = False, path_history = {}):
    path_status = (current_reactor, visited_dac, visited_fft)

    if path_status in path_history:
        return path_history[path_status]
    
    else:
        start_reactors = all_reactors[current_reactor]

        if start_reactors == ["out"]:
            if visited_dac and visited_fft:
                path_history[path_status] = 1
                return 1
            else:
                path_history[path_status] = 0
                return 0

        else:
            total_paths = 0

            for reactor in start_reactors:
                visited_dac = visited_dac or (reactor == "dac")
                visited_fft = visited_fft or (reactor == "fft")

                total_paths += find_reactor_paths(
                    all_reactors, 
                    reactor,
                    visited_dac,
                    visited_fft,
                )

            path_history[path_status] = total_paths

            return total_paths

def main():
    all_reactors = {}

    with open("src/2025/day11/day11_reactors_data.txt") as file:
        for line in file:
            source_reactor, connected_reactors = line.split(":")
            connected_reactors = connected_reactors.strip().split(" ")

            all_reactors[source_reactor] = connected_reactors

    num_paths = find_reactor_paths(all_reactors, "svr")
    print("Num paths:", num_paths)

if __name__ == "__main__":
    main()