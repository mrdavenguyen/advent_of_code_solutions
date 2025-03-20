import os

ACCUMULATE = "acc"
JUMP = "jmp"
NO_OPERATION = "nop"


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def execute_instruction(instruction, argument, accumulator_val):
    offset = argument if instruction == JUMP else 1

    accumulator_val += argument if instruction == ACCUMULATE else 0

    return offset, accumulator_val


def find_accumulator_value_at_loop(program):
    visited = set()

    accumulator_val = 0

    position = 0

    while position < len(program):
        if position in visited:
            return accumulator_val

        visited.add(position)

        instruction, argument = program[position]

        offset, accumulator_val = execute_instruction(
            instruction, int(argument), accumulator_val
        )

        position += offset

    return accumulator_val


def main():
    input_data = load_input("input.txt")

    program = [line.split() for line in input_data.splitlines()]

    accumulator_val = find_accumulator_value_at_loop(program)

    print(f"The solution is: {accumulator_val}")


if __name__ == "__main__":
    main()
