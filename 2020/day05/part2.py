import os

ROWS = 128
COLS = 8


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def convert_row_to_decimal(row):
    row_len = len(row)

    decimal = 0

    for i in range(row_len):
        decimal += 2 ** i if row[row_len - 1 - i] == "B" else 0

    return decimal


def convert_col_to_decimal(col):
    col_len = len(col)

    decimal = 0

    for i in range(col_len):
        decimal += 2 ** i if col[col_len - 1 - i] == "R" else 0

    return decimal


def calculate_seat_id(row, col):
    return row * 8 + col


def find_missing_seat(grid):
    flattened_grid = [seat_coord for row in grid for seat_coord in row]

    for i in range(1, len(flattened_grid) - 1):
        if flattened_grid[i - 1] and not flattened_grid[i] and flattened_grid[i + 1]:
            seat_before_missing = flattened_grid[i - 1]
            break

    x, y = seat_before_missing

    if x + 1 == COLS:
        return (0, y + 1)
    return (x + 1, y)


def populate_grid(input_data):
    grid = [[None for col in range(COLS)] for row in range(ROWS)]

    for line in input_data.splitlines():
        row, col = line[:-3], line[-3:]

        row_decimal = convert_row_to_decimal(row)
        col_decimal = convert_col_to_decimal(col)

        grid[row_decimal][col_decimal] = (col_decimal, row_decimal)

    return grid


def main():
    input_data = load_input("input.txt")

    grid = populate_grid(input_data)

    x, y = find_missing_seat(grid)

    missing_seat_id = calculate_seat_id(y, x)

    print(f"The solution is: {missing_seat_id}")


if __name__ == "__main__":
    main()
