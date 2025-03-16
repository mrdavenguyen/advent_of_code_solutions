import os

def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")

def count_valid_passwords(input_list):
    password_count = 0
    for line in input_list:
        policy, password = line.split(": ")
        positions, letter = policy.split()
        position_1, position_2 = list(map(int, positions.split("-")))
        index_1, index_2 = position_1 - 1, position_2 - 1 # Zero index each position
        password_count += (password[index_1] == letter) ^ (password[index_2] == letter) # Check whether the given letter is at each index and get the XOR of both booleans
    return password_count

def main():
    input_data = load_input("input.txt")
    password_count = count_valid_passwords(input_data.splitlines())
    print(f"The solution is: {password_count}")

if __name__ == "__main__":
    main()