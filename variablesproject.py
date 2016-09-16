#Nikolei Advani, 9/16/2016
#This program will draw two lines and calculate the angle between them.
print("draw two lines and calculate the angle between them.")

#user will input their first X and Y coordinates.
first_x_coordinate = float(input("What is the first X coordinate?:"))
first_y_coordinate = float(input("What is the first Y coordinate?:"))

#user will input their second X and Y coordinates.
second_x_coordinate = float(input("What is the second X coordinate?:"))
second_y_coordinate= float(input("What is the seocond Y coordinate?:"))

#equations to calculate m1 and m2.
first_slope = first_y_coordinate - 0 / first_x_coordinate - 0
second_slope = second_y_coordinate - first_y_coordinate / second_x_coordinate - first_x_coordinate

#turtle will draw the two lines.
import turtle
turtle.goto(first_x_coordinate , first_y_coordinate)
turtle.goto(second_x_coordinate, second_y_coordinate)

#'theda' will calculate the angle and 'degrees' will convert it from radians to degrees.
import math
theda = math.atan(second_slope - first_slope / 1 + first_slope * second_slope)
degrees = theda * 180 / math.pi

#turtle will print the number and the program will terminate.
turtle.write(degrees)
turtle.done()