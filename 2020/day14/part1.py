import os

BITMASK_LENGTH = 36


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def convert_decimal_to_n_bit_binary(n, decimal):
    binary = int(bin(decimal)[2:])

    return f"{binary:0{n}d}"


def get_programs(input_data):
    programs = [program.splitlines() for program in input_data.split("mask = ")][1:]

    for program in programs:
        for i in range(1, len(program)):
            address, decimal = program[i].split(" = ")
            address = int(address[4:-1])
            decimal = convert_decimal_to_n_bit_binary(BITMASK_LENGTH, int(decimal))

            program[i] = (address, decimal)

    return programs


def convert_binary_to_decimal(binary):
    decimal = 0

    for i in range(len(binary)):
        bit_position = len(binary) - 1 - i

        decimal += (2**i) * int(binary[bit_position])

    return decimal


def get_sum_of_all_memory_values(memory):
    return sum(memory.values())


def get_value_after_applying_bitmask(value, bitmask):
    modified_value = ""

    for i in range(len(bitmask)):
        if bitmask[i] == "X":
            modified_value += value[i]
        else:
            modified_value += bitmask[i]

    return modified_value


def execute_programs(programs):
    memory = {}

    for program in programs:
        bitmask = program[0]

        for address, binary_val in program[1:]:
            modified_binary_val = get_value_after_applying_bitmask(binary_val, bitmask)

            decimal_val = convert_binary_to_decimal(modified_binary_val)

            memory[address] = decimal_val

    return memory


def main():
    input_data = load_input("input.txt")

    programs = get_programs(input_data)

    memory = execute_programs(programs)

    memory_sum = get_sum_of_all_memory_values(memory)

    print(f"The solution is: {memory_sum}")


if __name__ == "__main__":
    main()
