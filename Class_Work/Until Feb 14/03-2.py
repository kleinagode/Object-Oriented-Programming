def inputs():
    name1 = input("Input the name of student 1: ")
    reg_no1 = input("Input the reg. number of student 1: ")
    gpa1 = input("Input the GPA of student 1: ")

    name2 = input("Input the name of student 2: ")
    reg_no2 = input("Input the reg. number of student 2: ")
    gpa2 = input("Input the GPA of student 2: ")
  

    return reg_no1, reg_no2


def main():
    reg_no1, reg_no2 = inputs()

    if reg_no1 == reg_no2:
        print("The reg_nos are the same. Please inform your office assistant to fix it.")
    
    
   



main()