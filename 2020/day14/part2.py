import os

BITMASK_LENGTH = 36


class BinaryTree:
    def __init__(self, binary=""):
        # A str representation of the binary path up to and including the current node.
        self.binary = binary
        # A list of next nodes where each index corresponds to the next binary bit.
        self.nxt = [None, None]


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
            address = convert_decimal_to_n_bit_binary(
                BITMASK_LENGTH, int(address[4:-1])
            )
            decimal = int(decimal)

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


def write_to_all_possible_memory_addresses(
    memory, node, decoded_address, value, index=0
):
    if index == len(decoded_address):
        address = convert_binary_to_decimal(node.binary)
        memory[address] = value

        return

    bit = decoded_address[index]
    branches = [0, 1] if bit == "X" else [int(bit)]

    for branch in branches:
        binary = node.binary + str(branch)

        if not node.nxt[branch]:
            node.nxt[branch] = BinaryTree(binary)

        write_to_all_possible_memory_addresses(
            memory, node.nxt[branch], decoded_address, value, index + 1
        )


def get_decoded_address(address, bitmask):
    decoded_address = ""

    for i in range(len(bitmask)):
        if bitmask[i] == "0":
            decoded_address += address[i]
        else:
            decoded_address += bitmask[i]

    return decoded_address


def execute_programs(programs):
    memory = {}
    root = BinaryTree()

    for program in programs:
        bitmask = program[0]

        for address, value in program[1:]:
            decoded_address = get_decoded_address(address, bitmask)

            write_to_all_possible_memory_addresses(memory, root, decoded_address, value)
    return memory


def main():
    input_data = load_input("input.txt")

    programs = get_programs(input_data)

    memory = execute_programs(programs)

    memory_sum = get_sum_of_all_memory_values(memory)

    print(f"The solution is: {memory_sum}")


if __name__ == "__main__":
    main()
