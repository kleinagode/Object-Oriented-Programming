
class arbitrary_arguments():

    def __init__ (self, *args):

        if isinstance(args[0],str):
            self.name = f"{args[0]} {args[1]} {args[2]}"
            print(f"Your full name is {self.name}")
            print()
        
        elif len(args) == 3 and isinstance(args[0],int):
            maximum = max(args)
            print(f"The maximum value of {args} is ---> {maximum}")
            print()
        
        elif len(args) == 2 and isinstance(args[0],int):
            print(f"Your favorite value is {args[0]}")
            print()


first = input("Enter your first name: ")
second = input("Enter your second name: ")
last = input("Enter your last name: ")
test1 = arbitrary_arguments(first, second, last)

a, b, c = int(input("Enter the first number: ")), int(input("Enter the second number: ")), int(input("Enter the third number: "))
test2 = arbitrary_arguments(a, b, c)

x,y = int(input("Enter the first number: ")), int(input("Enter the second number: "))
test3 = arbitrary_arguments(x,y)
    