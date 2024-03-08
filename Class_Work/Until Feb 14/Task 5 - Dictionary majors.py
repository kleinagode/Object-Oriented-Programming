#Create a dictionary with students and their details: name, major, minor, emphasis, andgrade
#Klei Nagode

students = {1: ["Klei", "CS", "EE", "Robotics", "B+"], 
            2: ["Lucas", "EE", "CS", "Game design", "A-"],
            3: ["Juan", "CS", "ART", "AI", "A"],
            4: ["Ahmet", "ME", "CS", "AI", "C"]
            }


#a) - ALL CS Majors
i = 1
print("ALL CS Majors")
for index in students:
    if students[i][1] == "CS":
        print(students[i])
    i+=1

print("\n\n")

#b) - CS minors with an EE or ME major
i = 1
print("CS minors with an EE or ME major")
for index in students:
    if students[i][2] == "CS" and students[i][1] == "EE" or students[i][1] == "ME":
        print(students[i])
    i+=1
    
print("\n\n")
    
#c) - All CS majors with an emphasis on Robotics/Game Design/Cyber
i = 1 
print("All CS majors with an emphasis on Robotics/Game Design/Cyber")
for index in students:
    if students[i][1] == "CS" and students[i][3] == "Robotics" or students[i][3] == "Game design" or students[i][3] == "Cyber":
        print(students[i])
    i+=1
  
print("\n\n")
    
#c) - All students who have grades A- or A
i = 1 
print("All students who have grades A- or A")
for index in students:
    if students[i][4] == "A-" or students[i][4] == "A":
        print(students[i])
    i+=1