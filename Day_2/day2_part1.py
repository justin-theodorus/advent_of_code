with open('day2_input.txt', 'r') as f:
    ans = 0
    for line in f:
        data = line.rstrip().split()
        int_data = [int(item) for item in data]

        if int_data[0] < int_data[1]:
            increasing = True
        elif int_data[0] > int_data[1]:
            increasing = False
        else:
            continue
        valid = True
        for i in range(1, len(int_data)):
            if increasing:
                if not(int_data[i] > int_data[i-1] and 1 <= int_data[i] - int_data[i-1] <= 3):
                    valid = False
                    break
            else:
                if not(int_data[i] < int_data[i-1] and 1 <= int_data[i-1] - int_data[i] <= 3):
                    valid = False
                    break
        if valid:
            ans += 1
        else:
            continue
print(ans)


