
with open("numbers.txt","r") as file:
    for num in file:
        numbers = num.split(",")

        
    float_numbers = [float(number) for number in numbers]
    number_sum = sum(float_numbers)

print(number_sum)