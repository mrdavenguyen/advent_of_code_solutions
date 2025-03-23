import os

STARTING_DIRECTION = "E"

START_POS = (0, 0)

DIRECTIONS_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

DIRECTIONS_DICT = {"E": (1, 0), "S": (0, 1), "W": (-1, 0), "N": (0, -1)}

TURN_DICT = {"L": -1, "R": 1}


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def convert_angle_to_turns(angle):
    return angle // 90


def get_next_direction(current_facing_dir, turn_dir, degrees):
    dir_idx = DIRECTIONS_LIST.index(current_facing_dir)

    new_idx = (dir_idx + TURN_DICT[turn_dir] * convert_angle_to_turns(degrees)) % len(
        DIRECTIONS_LIST
    )
    return DIRECTIONS_LIST[new_idx]


def execute_instruction(instruction, pos, facing_dir):
    command, value = instruction[0], int(instruction[1:])

    if command in "LR":
        next_dir = get_next_direction(facing_dir, command, value)

        return pos, next_dir

    x, y = pos

    if command in "NSEW":
        dx, dy = DIRECTIONS_DICT[command]

    if command == "F":
        dx, dy = facing_dir

    new_x, new_y = x + value * dx, y + value * dy
    return (new_x, new_y), facing_dir


def move_according_to_instructions(instructions, pos, facing_dir):
    for instruction in instructions:
        pos, facing_dir = execute_instruction(instruction, pos, facing_dir)

    return pos


def calculate_manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    input_data = load_input("input.txt")

    instructions = input_data.splitlines()

    facing_dir = DIRECTIONS_DICT[STARTING_DIRECTION]

    end_pos = move_according_to_instructions(instructions, START_POS, facing_dir)

    distance = calculate_manhattan_distance(START_POS, end_pos)

    print(f"The solution is: {distance}")


if __name__ == "__main__":
    main()
