
def tuple_task():

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    credit_score = int(input("Enter your credit score: "))

    person_info = (first_name, last_name, credit_score)
    
    print(f"First name: {person_info[0]}, Last name: {person_info[1]}, Credit score: {person_info[2]}")

tuple_task()