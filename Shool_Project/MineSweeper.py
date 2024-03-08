import random
import os

#8*8 GIRD
#Randomly placed mines

def Mine_Sweeper():

    mines_locations = set() #The unique coordinates of the mines

    def Clear():
        os.system("cls")

    def Difficulty():
        
        while True:

            print("1. Easy --> 10 Mines\n2. Moderate --> 20 Mines\n3. Hard --> 40 Mines")
        
            cho = input("Choose the difficulty: ")
            if not cho.isdigit():
                Clear()
                print("Enter a number!\n")
            else:
                cho = int(cho)
                if cho == 1:
                    mines = 10
                    break
                elif cho == 2:
                    mines = 20
                    break
                elif cho == 3:
                    mines = 40
                    break
                else:
                    Clear()
                    print("Enter a valid number!\n")
                    continue 
            
        return mines

    def Unique_Mines_Coordinates_1():
        
        #Location has to be random. It has to have a random x and y. 
        #A location also has to be checked to not be the same.
        
        mines = 10
        x_list = []
        y_list = []
        xdoubled_list = []
        coordinate_check = []
        coordinates = []
        
        def create_mines_coordinates():
            for i in range(mines):
                rand1 = random.randint(0,7)
                x_list.append(rand1)
                rand2 = random.randint(0,7)
                y_list.append(rand2)
        
                
        def doubled_xs():
            #appends the xdoubled list with the doubled item and how many times it appers in the list
            xdoubled_list.clear()
            for i in range(mines):
                count_x = x_list.count(i)
                if count_x > 1:
                    xdoubled_list.append(i)
                                    
           
            
            
        def doubled_list_check():
            
            coordinate_check.clear()
            #Checking for the dubled point
            for item in xdoubled_list:
                for i in range(len(x_list)):
                    if item == x_list[i]:
                        x = x_list[i]
                        y = y_list[i]
                        coordinate_check.append([x,y])
           
               
       
        def doubled_point_replacer():
            
            point_checker = True
        
             
            while point_checker:
                switch = 0
                doubled_xs()
                doubled_list_check()
                for i in range(len(coordinate_check)-1):
                    x1,y1 = coordinate_check[i]
                    x2,y2 = coordinate_check[i+1]
                    if x1 == x2 and y1 == y2:
                        switch = 1
                        for n in range(len(x_list)):
                            if x1 == x_list[n] and y1 == y_list[n]:
                                x_list[n] = random.randint(0,7)
                                y_list[n] = random.randint(0,7)                        
                
                i += 1
            
                if switch == 0:
                    point_checker = False
               
                

       
            for i in range(len(x_list)):
                coordinates.append([x_list[i], y_list[i]])
        
        
        create_mines_coordinates()
        doubled_point_replacer()
        return coordinates
   
    def Unique_Mines_Coordinates():
        
        mines = Difficulty()
        
        while len(mines_locations) < mines:
            x = random.randint(0,7)
            y = random.randint(0,7)
            mines_locations.add((x,y))

    def Grid_creation():

        rows = 8
        columns = 8
        x_coordinates = []
        y_coordinates = []
        grid = [["   [ ]   "]*columns for _ in range(rows)] #Creates an 8*8 grid with list comprehension
        
        Unique_Mines_Coordinates() #Getting the coordinates of the mines
        for item in mines_locations:
            x, y = item
            grid[y][x] = "    X    "
    
        for i in range (8):
            x_coordinates.append(f"    {i+1}    ")
            y_coordinates.append(f"{i+1}")

        Clear()
        print("")
        print("    |",end="")        
        
        for i in range(8):
            print(x_coordinates[i], end = "")
      
        print("")
                    
        
        print("_"*75)
        k = 0
        for item in grid:
            print("    |")
            print(f" {y_coordinates[k]}  |",end="")
            k += 1
            for el in item:
                print(f"{el}", end="")
            print("\n    |")
        
        print("\n")
         
    def Dig_Location():

        x = int(input("Enter the X coordinate: "))
        y = int(input("Enter the Y coordinate: "))

        return x,y


    Grid_creation()
   
        
         

Mine_Sweeper()




