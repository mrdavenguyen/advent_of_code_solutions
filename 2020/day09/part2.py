import os

PREAMBLE_LENGTH = 25


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def is_valid_number(number, preamble):
    seen = set()

    for pre_num in preamble:
        difference = number - pre_num

        if difference != pre_num and difference in seen:
            return True

        seen.add(pre_num)

    return False


def find_invalid_number_in_sequence(numbers):
    for i in range(len(numbers) - PREAMBLE_LENGTH - 1):
        preamble = numbers[i : i + PREAMBLE_LENGTH]

        next_number = numbers[i + PREAMBLE_LENGTH]

        if not is_valid_number(next_number, preamble):
            return next_number


def find_encryption_weakness(numbers, invalid_number):
    start, end = 0, 1

    while numbers[end] != invalid_number:
        contiguous_sum = sum(numbers[start:end])

        if contiguous_sum == invalid_number:
            return min(numbers[start:end]) + max(numbers[start:end])

        if contiguous_sum < invalid_number:
            end += 1

        else:
            start += 1

            if start == end:
                end += 1


def main():
    input_data = load_input("input.txt")

    numbers = [int(line) for line in input_data.splitlines()]

    invalid_number = find_invalid_number_in_sequence(numbers)

    encryption_weakness = find_encryption_weakness(numbers, invalid_number)

    print(f"The solution is: {encryption_weakness}")


if __name__ == "__main__":
    main()
