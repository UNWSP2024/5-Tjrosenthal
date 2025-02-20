# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.

#Tanner Rosenthal
#2/20/2025

def distance_converter(m1):
    miles = m1 * 0.6214
    return miles

kilometers = float(input("How many kilometers is the distance you are trying to convert?"))
value = distance_converter(kilometers)
print(kilometers, "kilometers is", round(value, 2), "miles")
