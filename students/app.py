student_list = []


def create_student():
    student_name = input("Student Name: ")
    student_data = {
        "name": student_name,
        "marks": []
    }
    return student_data


def add_mark(student, mark):
    student["marks"].append(mark)
    return None


def calculate_average_mark(student):
    count = len(student["marks"])
    if count == 0:
        return 0
    total = sum(student["marks"])
    return total / count


def print_student_details(student):
    # print("Name: {}".format(student["name"]))
    # print("Average: {}".format(student["marks"]))
    print("{}, average mark: {}.".format(student["name"], calculate_average_mark(student)))


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)


def menu():
    selection = input("enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to as a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")
    while selection != "q":
        if selection == "p":
            print_student_list(student_list)
        elif selection == "s":
            student_list.append(create_student())
        elif selection == "a":
            student_id = int(input("Enter the Student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)

        selection = input("enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to as a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")


menu()
