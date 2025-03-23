import os

STARTING_DIRECTION = "E"

START_POS = (0, 0)

STARTING_WAYPOINT = (10, -1)

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


def get_relative_position(reference, target):
    rx, ry = reference
    tx, ty = target
    return (tx - rx, ty - ry)


def normalise_waypoint_position(waypoint, facing_dir):
    if facing_dir == DIRECTIONS_DICT["E"]:
        return waypoint
    elif facing_dir == DIRECTIONS_DICT["S"]:
        return (waypoint[1], -waypoint[0])
    elif facing_dir == DIRECTIONS_DICT["W"]:
        return (-waypoint[0], -waypoint[1])
    elif facing_dir == DIRECTIONS_DICT["N"]:
        return (-waypoint[1], waypoint[0])


def rotate_normalised_position(normalised_pos, new_facing_dir):
    if new_facing_dir == DIRECTIONS_DICT["E"]:
        return normalised_pos
    elif new_facing_dir == DIRECTIONS_DICT["S"]:
        return (-normalised_pos[1], normalised_pos[0])
    elif new_facing_dir == DIRECTIONS_DICT["W"]:
        return (-normalised_pos[0], -normalised_pos[1])
    elif new_facing_dir == DIRECTIONS_DICT["N"]:
        return (normalised_pos[1], -normalised_pos[0])


def get_next_direction(current_facing_dir, turn_dir, degrees):
    dir_idx = DIRECTIONS_LIST.index(current_facing_dir)

    new_idx = (dir_idx + TURN_DICT[turn_dir] * convert_angle_to_turns(degrees)) % len(
        DIRECTIONS_LIST
    )
    return DIRECTIONS_LIST[new_idx]


def get_rotated_waypoint_position(pos, waypoint, current_facing_dir, next_facing_dir):
    rel_pos = get_relative_position(pos, waypoint)

    norm_pos = normalise_waypoint_position(rel_pos, current_facing_dir)

    new_rel_pos = rotate_normalised_position(norm_pos, next_facing_dir)

    new_waypoint = (pos[0] + new_rel_pos[0], pos[1] + new_rel_pos[1])

    return new_waypoint


def get_shifted_waypoint_position(direction, amount, waypoint):
    wx, wy = waypoint

    dx, dy = DIRECTIONS_DICT[direction]
    new_wx, new_wy = wx + (dx * amount), wy + (dy * amount)

    return (new_wx, new_wy)


def use_waypoint_to_move(current_pos, waypoint, move_count):
    for _ in range(move_count):
        wx, wy = waypoint

        distance_x, distance_y = get_relative_position(current_pos, waypoint)

        current_pos = waypoint
        waypoint = (wx + distance_x, wy + distance_y)
    return (current_pos, waypoint)


def execute_instruction(instruction, pos, facing_dir, waypoint):
    command, value = instruction[0], int(instruction[1:])

    if command in "LR":
        next_dir = get_next_direction(facing_dir, command, value)

        rotated_waypoint = get_rotated_waypoint_position(
            pos, waypoint, facing_dir, next_dir
        )

        return pos, next_dir, rotated_waypoint

    if command in "NSEW":
        shifted_waypoint = get_shifted_waypoint_position(command, value, waypoint)

        return pos, facing_dir, shifted_waypoint

    if command == "F":
        new_pos, new_waypoint = use_waypoint_to_move(pos, waypoint, value)

        return new_pos, facing_dir, new_waypoint


def move_according_to_instructions(instructions, pos, facing_dir, waypoint):
    for instruction in instructions:
        pos, facing_dir, waypoint = execute_instruction(
            instruction, pos, facing_dir, waypoint
        )

    return pos


def calculate_manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def main():
    input_data = load_input("input.txt")

    instructions = input_data.splitlines()

    facing_dir = DIRECTIONS_DICT[STARTING_DIRECTION]

    end_pos = move_according_to_instructions(
        instructions, START_POS, facing_dir, STARTING_WAYPOINT
    )

    distance = calculate_manhattan_distance(START_POS, end_pos)

    print(f"The solution is: {distance}")


if __name__ == "__main__":
    main()
