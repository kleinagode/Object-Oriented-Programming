class AgeTooYoungError(Exception):
    pass

class InvalidMajorError(Exception):
    pass

def collecting_inputs():
    while True:
        try:
            name = input("Enter the name of the student: ")
            age = int(input("Enter the student's age: "))
            reg_number = int(input("Enter the registration number: "))
            major = input("Enter the name of the program: ")

            if age <= 0:
                raise ValueError("Invalid age")
            elif age < 18:
                raise AgeTooYoungError("You must be at least 18 years old to register.")

            if major.lower() not in ["cs", "engineering"]:
                raise InvalidMajorError("Your major must be CS or Engineering.")

            print(f"Welcome {name}")
            break

        except ValueError as ve:
            print(ve)
        except AgeTooYoungError as atye:
            print(atye)
        except InvalidMajorError as ime:
            print(ime)


if __name__ == "__main__":
    collecting_inputs()
