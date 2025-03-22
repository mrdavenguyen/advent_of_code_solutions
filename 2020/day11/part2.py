import os
from copy import deepcopy

DIRECTIONS = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def is_occupied_seat(grid, col, row):
    return is_within_bounds(grid, col, row) and grid[row][col] == "#"


def is_within_bounds(grid, col, row):
    return 0 <= col < len(grid[0]) and 0 <= row < len(grid)


def implement_seating_based_on_rules(grid):
    new_grid = deepcopy(grid)

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            marker = grid[row][col]
            if marker == ".":
                continue
            elif marker == "L" and all_directions_first_seat_unoccupied(grid, col, row):
                new_grid[row][col] = "#"
            elif (
                marker == "#"
                and count_occupied_first_seats_in_all_directions(grid, col, row) >= 5
            ):
                new_grid[row][col] = "L"

    return new_grid


def all_directions_first_seat_unoccupied(grid, col, row):
    for x, y in DIRECTIONS:
        current_x, current_y = col, row

        while True:
            next_x, next_y = current_x + x, current_y + y

            if (
                not is_within_bounds(grid, next_x, next_y)
                or grid[next_y][next_x] == "L"
            ):
                break

            if grid[next_y][next_x] == "#":
                return False

            current_x, current_y = next_x, next_y

    return True


def count_occupied_first_seats_in_all_directions(grid, col, row):
    occupied_count = 0

    for x, y in DIRECTIONS:
        current_x, current_y = col, row

        while True:
            next_x, next_y = current_x + x, current_y + y

            if (
                not is_within_bounds(grid, next_x, next_y)
                or grid[next_y][next_x] == "L"
            ):
                break

            if grid[next_y][next_x] == "#":
                occupied_count += 1
                break

            current_x, current_y = next_x, next_y

    return occupied_count


def count_total_occupied_seats(grid):
    return sum(
        sum(grid[row][col] == "#" for col in range(len(grid[row])))
        for row in range(len(grid))
    )


def get_final_occupied_count(grid):
    prev_occupied_count = None

    while True:

        grid = implement_seating_based_on_rules(grid)

        occupied_count = count_total_occupied_seats(grid)

        if occupied_count == prev_occupied_count:
            return occupied_count

        prev_occupied_count = occupied_count


def main():
    input_data = load_input("input.txt")

    grid = [list(line) for line in input_data.splitlines()]

    occupied_count = get_final_occupied_count(grid)

    print(f"The solution is: {occupied_count}")


if __name__ == "__main__":
    main()
