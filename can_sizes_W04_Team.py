#Problem Statement
"""
In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can. Some sizes of cans require a lot of steel to store a small amount of food. Other sizes of cans require less steel and store more food. A can size with a large storage efficiency is considered more friendly to the environment than a can size with a small storage efficiency.

The storage efficiency of a steel can is computed by dividing the volume of a can by its surface area.

storage_efficiency = volume/surface_area
In other words, the storage efficiency of a can is the space inside the can divided by the amount of steel required to make the can. The formulas for the volume and surface area of a cylinder are:

volume = π radius^2*height
surface_area = 2π*radius*(radius + height)
π is the constant PI, the ratio of the circumference of a circle divided by its diameter (use math.pi)
radius is the radius of the cylinder
height is the height of the cylinder
"""
#Assignment
"""
Work as a team to write a Python program named can_sizes.py that computes and prints the storage efficiency for each of the following 12 steel can sizes.
Then visually examine the output and answer this question, “Which can size has the highest storage efficiency?”

Name	    Radius	Height	Cost per Can
            (cm)    (cm)    (U.S. dollars)
#1 Picnic	6.83	10.16	$0.28
#1 Tall	    7.78	11.91	$0.43
#2	        8.73	11.59	$0.45
#2.5	    10.32	11.91	$0.61
#3 Cylinder	10.79	17.78	$0.86
#5	        13.02	14.29	$0.83
#6Z	        5.40	8.89	$0.22
#8Z short	6.83	7.62	$0.26
#10	        15.72	17.78	$1.53
#211	    6.83	12.38	$0.34
#300	    7.62	11.27	$0.38
#303	    8.10	11.11	$0.42
If you separate your program into functions, this problem will be much easier to solve than if you don't separate it into functions.
You are free to write any functions that you choose in your program, but we strongly suggest that your program include at least these three functions:

main
compute_volume
compute_surface_area
"""
#Core Requirements
"""
Your program must compute the volume of all 12 can sizes.
Your program must compute the surface area of all 12 can sizes.
Your program must compute and print the storage efficiency of all 12 can sizes.
"""
#Stretch Challenges
"""
If your team finishes the core requirements in less than an hour, complete one or more of these stretch challenges. Note that the stretch challenges are optional.

Add another function named compute_storage_efficiency to your program. This function should call the compute_volume and compute_surface_area functions and then compute and return the storage efficiency of a steel can size. Replace code in the main function with a call to the compute_storage_efficiency function as appropriate. Did adding and calling the compute_storage_efficiency function reduce the number of lines of code in your program?
The table of can sizes that appears in the Assignment section above includes a column that contains the cost per can of each steel can size. Add another function to your program named compute_cost_efficiency that computes and returns the volume of a steel can divided by its cost. Write code to call the compute_cost_efficiency function and print the cost efficiency for each can size. Then visually examine the output and answer this question, “Which can size has the highest cost efficiency?”
If you remember how to use lists and a for loop from CSE 110, rewrite your main function so that it uses a list or lists that contain the can size names and dimensions. Then write a loop that processes the values in the list.
Add if statements inside the loop to automatically determine which can size has the best storage efficiency and which can size has the best cost efficiency.
"""

# Import the functions from the math library
# so that they can be used in this program.
import math

# Define functions
def main():
    Name = 	'#1 Picnic'
    Radius = 6.83
    Height = 10.16
    Cost_per_Can = .28
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#1 Tall'
    Radius = 7.78
    Height = 11.91
    Cost_per_Can = .43
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#2'
    Radius = 8.73
    Height = 11.59
    Cost_per_Can = .45
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#2.5'
    Radius = 10.32
    Height = 11.91
    Cost_per_Can = .61
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#3 Cylinder'
    Radius = 10.79
    Height = 17.78
    Cost_per_Can = .86
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#5'
    Radius = 13.02
    Height = 14.29
    Cost_per_Can = .83
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#6Z'
    Radius = 5.40
    Height = 8.89
    Cost_per_Can = .22
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#8Z short'
    Radius = 6.83
    Height = 7.62
    Cost_per_Can = .26
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#10'
    Radius = 15.72
    Height = 17.78
    Cost_per_Can = 1.53
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#211'
    Radius = 6.83
    Height = 12.38
    Cost_per_Can = .34
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#300'
    Radius = 7.62
    Height = 11.27
    Cost_per_Can = .38
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

    Name = 	'#303'
    Radius = 8.10
    Height = 11.11
    Cost_per_Can = .42
    print(f"{Name} {compute_storage_efficiency(Radius,Height):.2f} {compute_cost_efficiency(Radius,Height,Cost_per_Can):.0f}")

def compute_volume(radius,height):
    return math.pi*(radius*radius)*height
def compute_surface_area(radius,height):
    return 2*math.pi*radius*(radius + height)
def compute_storage_efficiency(radius,height):
    return(compute_volume(radius,height)/compute_surface_area(radius,height))
def compute_cost_efficiency(radius,height,cost):
    return compute_volume(radius,height)/cost

# Call the main function so that
# this program will start executing.
main()