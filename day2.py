def difference_check(main_entry, other_entry):
    return 1 <= abs(int(main_entry) - int(other_entry)) <= 3

def trend_check(entry_a, entry_b):
    if int(entry_a) < int(entry_b):
        return -1
    if int(entry_a) > int(entry_b):
        return 1
    else:
        return 0

def safety_check_new(entries):
    trend = []
    difference = []

    for i in range(0, len(entries)-1):
        current_difference = abs(int(entries[i]) - int(entries[i+1]))
        current_trend = trend_check(entries[i], entries[i+1])
        trend.append(current_trend)
        difference.append(current_difference)

    trend_result = abs(sum(trend))
    max_difference = max(difference)
    min_difference = min(difference)


    if 1 <= min_difference and max_difference <= 3 and trend_result == len(trend):
        print(trend_result, min_difference, max_difference, entries, 'RIGHT')
        return 1
    
    print(trend_result,min_difference, max_difference, entries, 'WRONG')
    return 0

def iterate_lists(entries):
    safety_list = []
    for i in range(0, len(entries)):
        copy_entries = entries.copy()
        copy_entries.pop(i)
        safety_list.append(safety_check_new(copy_entries))

    return 1 if 1 in safety_list else 0


def main():
    count = 0
    with open("test.txt") as file:
        for line in file:
            entries = line.split()
            count += iterate_lists(entries)

    print(f'number of safe entries: {count}')


if __name__ == "__main__":
    main()

