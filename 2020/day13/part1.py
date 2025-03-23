import os


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def find_soonest_bus(timestamp, bus_ids):
    soonest_bus = None
    shortest_wait = float("inf")

    for id in bus_ids:
        time_since_last_bus = timestamp % id

        wait = id - time_since_last_bus

        if wait < shortest_wait:
            shortest_wait = wait
            soonest_bus = id

    return soonest_bus, shortest_wait


def main():
    input_data = load_input("input.txt")

    timestamp, bus_ids = input_data.splitlines()

    timestamp = int(timestamp)

    bus_ids = [int(num) for num in bus_ids.split(",") if num != "x"]

    soonest_bus, shortest_wait = find_soonest_bus(timestamp, bus_ids)

    print(f"The solution is: {soonest_bus * shortest_wait}")


if __name__ == "__main__":
    main()
