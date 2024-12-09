def merge(left_partial, right_partial):
    complete = []
    i, j = 0, 0

    while i < len(left_partial) and j < len(right_partial):
        if left_partial[i] <= right_partial[j]:
            complete.append(left_partial[i])
            i += 1
        else:
            complete.append(right_partial[j])
            j += 1

    complete.extend(left_partial[i:])
    complete.extend(right_partial[j:])

    return complete

def merge_sort(location_list):
    length = len(location_list)
    if length < 2:  # when recursion hits a single element.
        return location_list
    else:
        mid_point = length // 2
        return merge(
            merge_sort(location_list[:mid_point]),
            merge_sort(location_list[mid_point:]),
        )


def distances(first_list, second_list):
    first_list_sorted = merge_sort(first_list)
    second_list_sorted = merge_sort(second_list)

    return [abs(int(x) - int(y)) for x, y in zip(first_list_sorted, second_list_sorted)]


def total_distance(distances_list):
    return sum(distances_list)


def counter(second_list):
    count_dict = {}

    for number in second_list:
        if int(number) in count_dict:
            count_dict[int(number)] += 1
        else:
            count_dict[int(number)] = 1

    return count_dict

def similarity_score(count_dict, first_list):
    score = 0
    for number in first_list:
        if int(number) in count_dict:
            score += int(number) * count_dict[int(number)]
    return score


def main():
    first_list = []
    second_list = []
    with open("test.txt") as file:
        for line in file:
            entries = line.split()
            first_list += entries[0::2]
            second_list += entries[1::2]

    distance_list = distances(first_list, second_list)
    count_dict = counter(second_list)
    score = similarity_score(count_dict, first_list)

    print(score)
    print(total_distance(distance_list))



if __name__ == "__main__":
    main()
