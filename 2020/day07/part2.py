import os


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def create_bag_dict(input_data):
    bag_dict = {}
    for line in input_data.splitlines():
        container, contained = line.split(" contain ")

        container = container[:-1]

        if contained == "no other bags.":
            bag_dict[container] = []
        else:
            contained = [
                (int(x[:2]), x[2:].rstrip(".").rstrip("s"))
                for x in contained.split(", ")
            ]

            bag_dict[container] = contained

    return bag_dict


def count_contained_bags(containing_bag, bag_dict):
    bag_count = 1

    if bag_dict[containing_bag] == []:
        return bag_count

    for amount, bag in bag_dict[containing_bag]:
        bag_count += amount * count_contained_bags(bag, bag_dict)

    return bag_count


def main():
    input_data = load_input("input.txt")

    containing_bag = "shiny gold bag"

    bag_dict = create_bag_dict(input_data)

    # Subtract 1 to exclude the outermost bag
    bag_count = count_contained_bags(containing_bag, bag_dict) - 1

    print(f"The solution is: {bag_count}")


if __name__ == "__main__":
    main()
