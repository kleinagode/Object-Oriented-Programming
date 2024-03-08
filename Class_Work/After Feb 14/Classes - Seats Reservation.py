
class seats():

    def __init__(self,seat_num):
        pass
        self.seat_num = seat_num
        self.paid = 0.0
        self.name = ""

    def print_seats(self):
        print(f"{self.seat_num}: {self.name}, Paid: ${self.paid}")

    def reserve(self):
        self.name = input("Enter the name this seat will be reserved under: ")
        self.paid = float(input("Enter the ammount paid: $"))

def initialize_objects():
    seat_objects = []
    for i in range (5):
        seat_objects.append(seats(i))
    
    return seat_objects

def seat_reservation():
       
    
    while True:

        cho = input("Enter command (p/r/q)\n")

        if cho == "p":
            for item in seat_objects:
                item.print_seats()
        
        elif cho == "r":
           
            found = False
            seat_n = int(input("Enter the no. of the seat you want to reserve: "))
            
            for obj in seat_objects:
                if obj.seat_num == seat_n:
                    found = True
                    if obj.name == "":
                        obj.reserve()
                    else :
                        print("This seat is already reserved!")
                        break                        
                    
            if not found:
                print("Enter a valid seat number!")
                

        elif cho == "q":
            break
        else :
            print("Invalid choice ")
            continue


seat_objects = initialize_objects()
seat_reservation()