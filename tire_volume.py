#Import math library because i need to use the math.pi functions
import math
#W02 Excercise, Import datetime for the new file
from datetime import datetime
cdt = datetime.now()
tire_width = float(input("Enter the width of the ire in mm (ex 205)"))
tire_ratio = float(input("Enter the aspect ratio of the (ex 60)"))
tire_diameter = float(input("Enter the diameter of the wheel in inches (ex 15)"))

parentesis =  2540 * tire_diameter + tire_width * tire_ratio
v = math.pi * tire_width**2 * tire_ratio 
Result = parentesis * v / 10000000000
print(f"The aproximate volume of liters of the wheel is: {Result} liters")

#This code print our cdt(time now variable) with the format of year, month and day
#with separations and "f" for the string

#Open our text file named volumes.txt in append mode (modo edición) with "at"
with open("volumes.txt","at") as volumes_file:
    print(f"{cdt:%Y-%m-%d}",tire_width,tire_ratio,tire_diameter,Result,file=volumes_file)