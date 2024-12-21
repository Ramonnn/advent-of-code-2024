def addition(num_a, num_b):
    return num_a + num_b

def multiplication(num_a, num_b):
    return num_a * num_b

def concatenation(num_a, num_b):
    return int(str(num_a) + str(num_b))

def generate_recursion(numbers, index=1, current_value=None, list_of_values=None):
    if list_of_values is None:
        list_of_values = []

    if index == len(numbers):
        list_of_values.append(current_value)
        return list_of_values

    if current_value is None:
        current_value = numbers[0]

    generate_recursion(numbers, index + 1, addition(current_value, numbers[index]), list_of_values)
    generate_recursion(numbers, index + 1, multiplication(current_value, numbers[index]), list_of_values)
    generate_recursion(numbers, index + 1, concatenation(current_value, numbers[index]), list_of_values)

    return list_of_values


def main():
    summation = 0
    with open('test.txt') as f:
        lines = f.readlines()

    for line in lines:
        chunks = line.split(': ')
        numbers = [int(number) for number in chunks[1].split(' ')]

        values = generate_recursion(numbers)

        if int(chunks[0]) in values:
            summation += int(chunks[0])

    print(summation)

main()
