import os


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def create_grid(input_data):
    return [list(line) for line in input_data.splitlines()]


def is_a_tree(grid, x, y):
    return grid[y][x] == "#"


def get_instructions_list(instructions_data):
    instructions_list = [line.split(", ") for line in instructions_data.splitlines()]

    for i in range(len(instructions_list)):
        instructions_list[i][0] = int(instructions_list[i][0].split()[1])
        instructions_list[i][1] = int(instructions_list[i][1].split()[1].rstrip("."))

    return instructions_list


def count_tree_collisions(instructions, grid):
    pos = (0, 0)

    tree_collisions = 0

    dx, dy = instructions

    while pos[1] < len(grid):
        x, y = pos

        tree_collisions += is_a_tree(grid, x, y)

        new_x, new_y = (x + dx) % len(grid[0]), y + dy
        pos = (new_x, new_y)

    return tree_collisions


def main():
    input_data = load_input("input_part1.txt")

    instructions_data, grid_data = input_data.split("\n\n")

    instructions_list = get_instructions_list(instructions_data)

    grid = create_grid(grid_data)

    tree_collision_count = count_tree_collisions(instructions_list[0], grid)

    print(f"The solution is: {tree_collision_count}")


if __name__ == "__main__":
    main()
