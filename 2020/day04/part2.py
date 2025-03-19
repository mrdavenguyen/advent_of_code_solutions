import os
from re import finditer, fullmatch

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
    value_patterns = {
        "byr": r"^(?:19[2-9]\d|200[0-2])$",
        "iyr": r"^(?:201\d|2020)$",
        "eyr": r"^(?:202\d|2030)$",
        "hgt": r"^(?:(?:1[5-8]\d|19[0-3])cm|(?:59|6\d|7[0-6])in)$",
        "hcl": r"^#[0-9a-f]{6}$",
        "ecl": r"^(?:amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^[0-9]{9}$"
    }

    matched = set()

    for match in finditer(r"(\w{3}):(\S+)", passport):
        key, value = match.groups()
        if key in value_patterns:
            if not fullmatch(value_patterns[key], value):
                return False
            matched.add(key)
    required_fields = set(value_patterns.keys())
    return matched == required_fields

def main():
    input_data = load_input("input.txt")
    passports = [section.replace("\n", " ") for section in input_data.split("\n\n")]
    passport_count = get_valid_passport_count(passports)
    print(f"The solution is: {passport_count}")
    
if __name__ == "__main__":
    main()