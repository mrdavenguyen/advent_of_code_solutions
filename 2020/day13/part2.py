import os


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def calculate_lcm_of_pair(a, b):
    return (a * b) // find_gcd(a, b)


def get_earliest_timestamp_matching_consecutive_bus_ids(bus_ids):
    timestamp = 1
    step = 1

    i = 0

    while i < len(bus_ids):
        id_num, offset = bus_ids[i]

        while True:
            if (timestamp + offset) % id_num == 0:
                step = calculate_lcm_of_pair(step, id_num)

                i += 1

                break

            timestamp += step

    return timestamp


def main():
    input_data = load_input("input.txt")

    bus_ids = input_data.splitlines()[1]

    bus_ids = [(int(num), i) for i, num in enumerate(bus_ids.split(",")) if num != "x"]

    timestamp = get_earliest_timestamp_matching_consecutive_bus_ids(bus_ids)

    print(f"The solution is: {timestamp}")


if __name__ == "__main__":
    main()
