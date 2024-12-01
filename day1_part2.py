with open('day1_part1_input.txt', 'r') as f:
    left_list = []
    right_list = []
    left_dict = {}
    right_dict = {}
    for line in f:
        data = line.strip().split()
        left_list.append(int(data[0]))
        right_list.append(int(data[1]))
        if int(data[1]) not in right_dict:
            right_dict[int(data[1])] = 1
        else:
            right_dict[int(data[1])] += 1

    total_similarity = 0
    for l in left_list:
        if l not in right_dict:
            continue

        if l not in left_dict:
            total_similarity += l * right_dict[l]
            left_dict[l] = l * right_dict[l]
        else:
            total_similarity += left_dict[l]
        
    print(total_similarity)
