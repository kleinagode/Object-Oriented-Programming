
class Child:
    
    def __init__(self, age):
        self.age = age

    def __lt__(self,other):
        if self.age < other.age:
            return True
        else:
            return False
        
    def smallest(self):
        s_years = str(self.age)
        if len(s_years) < 4:
            years = s_years[0:1]
            months = s_years[2:3]
        else:
            years = s_years[0:2]
            months = s_years[2:4]
        print(f"The youngest child is {years} years and {months} months old.")



children_obj = []
cho =  int(input("How many children do you want to add? "))

for i in range(cho):
   children_obj.append(Child(int(input("Enter the age of the Child in the format (age : months): ").replace(":","").replace(" ",""))))


smallest = children_obj[i]
for obj in children_obj:
    if obj < smallest:
        smallest = obj
        
    

smallest.smallest()