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

def get_product_of_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

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
    input_data = load_input("input_part2.txt")

    instructions_data, grid_data = input_data.split("\n\n")

    instructions_list = get_instructions_list(instructions_data)

    grid = create_grid(grid_data)

    tree_collisions_counts = [count_tree_collisions(instructions, grid) for instructions in instructions_list]

    product_of_tree_collisions = get_product_of_numbers(tree_collisions_counts)

    print(f"The solution is: {product_of_tree_collisions}")

if __name__ == "__main__":
    main()