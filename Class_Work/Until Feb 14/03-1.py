
def inputs():
    name = input("Input your name: ")
    reg_no = input("Input your reg. number: ")
    gpa = input("Input your GPA: ")

    name_len = len(name)

    return name, reg_no, gpa, name_len


def main():
    name, reg_no, gpa, name_len = inputs()

    print(f"Hey {name}, your reg_no is {reg_no}, your GPA is {gpa}, the length of your name is: {name_len}")
    print("Welcome to python programming")



main()