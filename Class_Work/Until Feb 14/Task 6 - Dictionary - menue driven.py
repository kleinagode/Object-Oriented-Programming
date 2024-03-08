
def menue_dictionary():

    my_students = {}
    
    while True:

        
        print("1. Add a student\n2. Delete a student\n3. Modify a student\n4. Display all the students\n5. Exit\n")
        cho = int(input("Enter your choice: "))
        if cho == 1:
            name = input("Enter a name for the new student: ")
            print("Enter lab grades with spaces: ")
            grades = input().split()
            grades = [int(i) for i in grades]
            grades.extend((sum(grades), sum(grades)/len(grades)))
            my_students[name] = grades
        elif cho == 2:
            print(my_students)
            delete = input("\nWhich student do you want to delete: ")
            del my_students[delete]
        elif cho == 3:
            modify_name = input("Which student do you want to modify: ")
            modify_grade = int(input("Which grade do you want to modify (1st, 2nd,...): ")) - 1
            new_grade = int(input("What do you want to change that grade to: "))
            my_students[modify_name][modify_grade] = new_grade
        elif cho == 4:
            print(f"\n\t\t{my_students}\n\n")
        elif cho == 5:
            break

menue_dictionary()