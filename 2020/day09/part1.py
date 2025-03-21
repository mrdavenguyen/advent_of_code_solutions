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


def main():
    input_data = load_input("input.txt")

    numbers = [int(line) for line in input_data.splitlines()]

    invalid_number = find_invalid_number_in_sequence(numbers)

    print(f"The solution is: {invalid_number}")


if __name__ == "__main__":
    main()
