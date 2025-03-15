def get_three_sum(nums, target):
    nums.sort()
    for i in range(len(nums) - 2):
        low = i + 1
        high = len(nums) - 1
        while low < high:
            total = nums[i] + nums[low] + nums[high]
            if total == target:
                return (nums[i], nums[low], nums[high])
            elif total < target:
                low += 1
            elif total > target:
                high -= 1
    return None

def get_product_of_numbers(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def load_input(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")

def main():
    target_sum = 2020

    input_data = load_input("input.txt")
    nums = list(map(int, input_data.splitlines()))
    three_sum = get_three_sum(nums, target_sum)
    product = get_product_of_numbers(three_sum)

    print(f"The solution is: {product}")

if __name__ == "__main__":
    main()



