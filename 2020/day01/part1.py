import os

def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")

def get_two_sum(nums, target):
    seen = set()

    for num in nums:
        difference = target - num
        if difference in seen:
            return (num, difference)
        else:
            seen.add(num)
    return None

def get_product_of_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def main():
    target_sum = 2020

    input_data = load_input("input.txt")
    nums = list(map(int, input_data.splitlines()))

    two_sum = get_two_sum(nums, target_sum)
    product = get_product_of_numbers(two_sum)

    print(f"The solution is: {product}")


if __name__ == "__main__":
    main()
