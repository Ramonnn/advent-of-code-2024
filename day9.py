test = '597684543'

def read_input():
    with open('test.txt') as f:
        input = f.read().strip("\n")

    return input

def concat(input_1, input_2):
        return input_1 + input_2

def split_diskmap(diskmap):
    unpacked_map = []
    half_idx = 0
    for idx, byte in enumerate(diskmap):
        byte = int(byte)
        if idx % 2 == 0:
            addition = [str(half_idx)] * byte
            unpacked_map += addition
            half_idx += 1
        else:
            addition = ['.'] * byte
            unpacked_map += addition 
    return unpacked_map

def sort_diskmap(unpacked_map):

    forward = 0
    backward = len(unpacked_map)-1

    list_map = unpacked_map.copy()

    while list_map[forward] != '.':
        forward += 1

    while list_map[backward] == '.':
        backward -= 1

    while backward > forward:
        list_map[forward] = list_map[backward]
        list_map[backward] = '.'
        while list_map[backward] == '.':
            backward -= 1
        while list_map[forward] != '.':
            forward += 1

    cutoff = forward

    return list_map, cutoff

def calculate_checksum(list_map, cutoff):
    checksum = 0
    for i in range(0, cutoff):
        checksum += int(list_map[i]) * i

    return checksum


input = read_input()
unpacked_map = split_diskmap(input)
list_map, cutoff = sort_diskmap(unpacked_map)

# print(sort_diskmap(unpacked_map))
print(calculate_checksum(list_map, cutoff))

