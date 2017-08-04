print("what is the width of the wall?")
width= int(input())
print("what is  the height?")
height= int(input())
space= width * height
gallon= 400
print(" how much does a gallon of paint cost?")
cost= int(input())
print(" you will need "+ str(round(space/ gallon) * cost) + " dollars to cover" + str(space)+ "sqaure feet")
