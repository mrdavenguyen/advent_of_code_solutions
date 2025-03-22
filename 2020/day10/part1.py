import os
from collections import defaultdict


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def get_joltage_differences_dict(joltages):
    joltage_differences = defaultdict(int)

    current = 0

    for joltage in joltages:
        previous = current
        current = joltage
        difference = current - previous

        joltage_differences[difference] += 1

    return joltage_differences


def get_sorted_joltages(input_data):
    adapter_joltages = sorted(int(line) for line in input_data.splitlines())

    built_in_adapter = adapter_joltages[-1] + 3

    return adapter_joltages + [built_in_adapter]


def main():
    input_data = load_input("input.txt")

    joltages = get_sorted_joltages(input_data)

    joltage_differences = get_joltage_differences_dict(joltages)

    multiplied_differences = joltage_differences[1] * joltage_differences[3]

    print(f"The solution is: {multiplied_differences}")


if __name__ == "__main__":
    main()
