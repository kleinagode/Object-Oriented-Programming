
def team_dictionary():

    Stud_mark = {"Klei" :90, 
                 "Lucas" : 91, 
                 "Jonas" : 83,
                 "Joseph" : 75,
                 "Borat" : 31}
    
    name1 = input("Enter the name of student 1 for the team: ")
    name2 = input("Enter the name of student 2 for the team: ")

    final_score = Stud_mark[name1] + Stud_mark[name2]

    print(f"The total score of the team is: {final_score}")

team_dictionary()
