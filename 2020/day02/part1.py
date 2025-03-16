def load_input(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")

def count_valid_passwords(input_list):
    password_count = 0
    for line in input_list:
        policy, password = line.split(": ")
        repetitions, letter = policy.split()
        lower_bound, upper_bound = list(map(int, repetitions.split("-")))
        letter_count = password.count(letter)
        password_count += lower_bound <= letter_count <= upper_bound
    return password_count

def main():
    input_data = load_input("input.txt")
    password_count = count_valid_passwords(input_data.splitlines())
    print(f"The solution is: {password_count}")

if __name__ == "__main__":
    main()