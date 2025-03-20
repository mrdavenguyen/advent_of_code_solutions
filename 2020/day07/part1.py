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
            contained = [x[2:].rstrip(".").rstrip("s") for x in contained.split(", ")]

            bag_dict[container] = contained

    return bag_dict


def contains_shiny_gold_bag(bag, target_bag, bag_dict, memoized_bags):
    if bag in memoized_bags:
        return memoized_bags[bag]

    if target_bag in bag_dict[bag]:
        memoized_bags[bag] = True

        return True

    contains_bag = False

    for contained_bag in bag_dict[bag]:
        if contains_shiny_gold_bag(contained_bag, target_bag, bag_dict, memoized_bags):
            memoized_bags[contained_bag] = True

            contains_bag = True
        else:
            memoized_bags[contained_bag] = False

    return contains_bag


def main():
    input_data = load_input("input.txt")

    target_bag = "shiny gold bag"

    bag_dict = create_bag_dict(input_data)

    memoized_bags = {}

    target_bag_container_count = 0

    for bag in bag_dict:
        if contains_shiny_gold_bag(bag, target_bag, bag_dict, memoized_bags):
            memoized_bags[bag] = True

            target_bag_container_count += 1
        else:
            memoized_bags[bag] = False

    print(target_bag_container_count)


if __name__ == "__main__":
    main()
