import os


def load_input(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        exit(f"File '{filename}' not found.")


def get_count_of_groups_questions(group):
    questions = set()

    for line in group.splitlines():
        for question in line:
            questions.add(question)

    return len(questions)


def main():
    input_data = load_input("input.txt")

    groups = input_data.split("\n\n")

    question_count = 0

    for group in groups:
        question_count += get_count_of_groups_questions(group)

    print(f"The solution is: {question_count}")


if __name__ == "__main__":
    main()
