
def inputs():
    
    name_raw = input("Enter in your full name: ")
    name_split = name_raw.split()
    formated_name = [item[0].upper() + "." for item in name_split]

    
    if len(formated_name) < 3:
        print(f"Hello {name_split[1].capitalize()}, {formated_name[0]} !")
    else:
        print(f"Hello {name_split[2].capitalize()}, {formated_name[0] + formated_name[1]} !")

inputs()