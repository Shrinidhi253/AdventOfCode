def calculate_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    x1, y1, z1 = int(x1), int(y1), int(z1)
    x2, y2, z2 = int(x2), int(y2), int(z2)

    distance = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2) ** 0.5

    return distance


def get_closest_points(all_points, num_points):
    closest_points = []

    for i in range(len(all_points)-1):
        for j in range(i+1, len(all_points)):
            point1 = all_points[i]
            point2 = all_points[j]

            distance = calculate_distance(point1, point2)

            closest_points.append((point1, point2, distance))


    n_closest_points = sorted(closest_points, key = lambda points : points[2])[:num_points]

    return n_closest_points


def find_circuits(closest_points):
    circuits = [] #stores a set of the circuits formed
    points_added = {} #keep track of which point has been added to which circuit (circuit index)

    for points_pair in closest_points:
        point1, point2 = points_pair[0], points_pair[1]

        #if point1 / point2 has already been added, get the index of the circuit in which point1 exists
        #else, create a new circuit. The index of this circuit will be the last circuit index + 1 (or the length of circuits)

        if point1 in points_added and point2 not in points_added:
            point1_circuit = points_added[point1]
            circuits[point1_circuit].add(point2)
            points_added[point2] = point1_circuit #update the circuit index of point2 to the point1 circuit index
        
        elif point2 in points_added and point1 not in points_added:
            point2_circuit = points_added[point2]
            circuits[point2_circuit].add(point1)
            points_added[point1] = point2_circuit

        elif point1 in points_added and point2 in points_added: #add/merge the circuits if point1 and point2 are added to 2 separate circuits
            point1_circuit = points_added[point1]
            point2_circuit = points_added[point2]

            if point1_circuit != point2_circuit:
                circuits[point1_circuit].update(circuits[point2_circuit])

                for point in circuits[point2_circuit]:
                    points_added[point] = point1_circuit

                circuits[point2_circuit] = set() 
                #since point2 circuit has been merged to point1_circuit, make it an empty set to avoid duplicates and circuit-index problems

        else:
            new_circuit = set({point1, point2})
            circuits.append(new_circuit)
            new_circuit_index = len(circuits) - 1

            points_added[point1] = new_circuit_index
     
            points_added[point2] = new_circuit_index

    three_largest_circuits = sorted(circuits, key = lambda circuit : len(circuit), reverse=True)[:3]

    return three_largest_circuits


def main():
    all_points = []
    with open("src/2025/day08/day08_positions_data.txt") as file:
        for line in file:
            coordinates = tuple(line.strip().split(","))
            all_points.append(coordinates)

    thousand_closest_points = get_closest_points(all_points, 1000)
    three_largest_circuits = find_circuits(thousand_closest_points)

    total = 1
    for circuit in three_largest_circuits:
        total *= len(circuit)

    print("Total:", total)

if __name__ == "__main__":
    main()