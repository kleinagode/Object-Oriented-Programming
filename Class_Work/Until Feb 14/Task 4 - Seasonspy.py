
def main():

    month = input()
    day = int(input())
   
    months = ["january", "february", "march", "april", "may", "june", "july", "august",
              "september", "october", "november", "december"]
    
    def season_finder(month, day):

        if (month == "march" and day >= 20) or (month == "april" and day <= 19):
            print("Spring")
        elif (month == "april" and day >= 20) or (month == "may") or (month == "june" and day <= 20):
            print("Summer")
        elif (month == "june" and day >= 21) or (month == "july") or (month == "august" and day <= 21):
            print("Summer")
        elif (month == "august" and day >= 22) or (month == "september") or (month == "october" and day <= 21):
            print("Autumn")
        elif (month == "october" and day >= 22) or (month == "november") or (month == "december" and day <= 20):
            print("Autumn")
        elif (month == "december" and day >= 21) or (month == "january") or (month == "february" and day <= 19):
            print("Winter")
        elif (month == "february" and day >= 20) or (month == "march" and day <= 19):
            print("Winter")


    if not month.lower() in months or day > 31 or day < 1:
        print("Invalid")
    else:
        season_finder(month,day)


    

main()
