import os


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def get_sorted_joltages(input_data):
    adapter_joltages = sorted(int(line) for line in input_data.splitlines())

    charging_outlet, built_in_adapter = 0, adapter_joltages[-1] + 3

    return [charging_outlet] + adapter_joltages + [built_in_adapter]


def count_possible_adapter_arrangements(joltages):
    # Maps adapter joltage to the possible arrangements count from that point onward.
    arrangements = {}

    for i in reversed(range(len(joltages))):
        current_number = joltages[i]

        # Counts the number of arrangements possible from the current adapter onward.
        arrangements_count = 0

        if i == len(joltages) - 1:
            arrangements_count += 1
            arrangements[current_number] = arrangements_count
            continue

        j = i + 1

        while j < len(joltages):
            following_number = joltages[j]
            difference = following_number - current_number

            if difference <= 3:
                arrangements_count += arrangements[following_number]

                j += 1
            else:
                break

        arrangements[current_number] = arrangements_count

    return arrangements_count


def main():
    input_data = load_input("input.txt")

    joltages = get_sorted_joltages(input_data)

    arrangements_count = count_possible_adapter_arrangements(joltages)

    print(f"The solution is {arrangements_count}")


if __name__ == "__main__":
    main()
