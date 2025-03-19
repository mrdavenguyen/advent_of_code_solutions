import os


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


def get_highest_seat_id(input_data):
    highest_seat_id = float("-inf")

    for line in input_data.splitlines():
        row, col = line[:-3], line[-3:]

        row_decimal = convert_row_to_decimal(row)
        col_decimal = convert_col_to_decimal(col)

        seat_id = calculate_seat_id(row_decimal, col_decimal)
        highest_seat_id = max(highest_seat_id, seat_id)

    return highest_seat_id


def main():
    input_data = load_input("input.txt")

    highest_seat_id = get_highest_seat_id(input_data)

    print(f"The solution is: {highest_seat_id}")


if __name__ == "__main__":
    main()
