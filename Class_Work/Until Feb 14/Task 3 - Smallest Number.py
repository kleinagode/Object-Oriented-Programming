
def smallest_number():

    numbers_input = input("Enter the numbers seperated by a space: ")
    numbers = numbers_input.split()

    smallest_number = min(numbers)

    print(f"The smallest number you entered is {smallest_number}")

smallest_number()