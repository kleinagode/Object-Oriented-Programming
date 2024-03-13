
height = float(input())

try:
    10/height
except ZeroDivisionError:
    print("Can not devide by zero")

except (ValueError, TypeError):
    print("Invalid input")

if height < 0:
    raise ValueError("Invalind height, the height can not be negative")
    
        




