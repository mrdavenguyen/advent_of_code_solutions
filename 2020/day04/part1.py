import os
from re import findall


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def get_valid_passport_count(passports):
    valid_count = 0

    for passport in passports:
        valid_count += is_valid_passport(passport)

    return valid_count


def is_valid_passport(passport):
    fields = [
        "byr",
        "iyr",
        "eyr",
        "hgt",
        "hcl",
        "ecl",
        "pid",
    ]  # Excluded "cid" as instructed

    pattern = "(" + "|".join(fields) + ")"
    matches = set(findall(pattern, passport))

    return all(field in matches for field in fields)


def main():
    input_data = load_input("input.txt")

    passports = [section.replace("\n", " ") for section in input_data.split("\n\n")]

    passport_count = get_valid_passport_count(passports)

    print(f"The solution is: {passport_count}")


if __name__ == "__main__":
    main()
