with open('day1_part1_input.txt', 'r') as f:
    left_list = []
    right_list = []
    for line in f:
        data = line.strip().split()
        left_list.append(int(data[0]))
        right_list.append(int(data[1]))

    left_list.sort()
    right_list.sort()

    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    print(total_distance)
