import math


while True:
  lenght = input("What is the lenght of the room? ")
  width = input("What is the width of the room? ")

  if lenght.isnumeric() and width.isnumeric():
    break
  print("Please enter numbers only.\n")

measure = input("Are you measuring in meters or in feet? ")

if measure.lower() == "feet":
  print("The area is:\n")

  feetArea = int(lenght) * int(width)
  metersArea = math.sqrt(feetArea**2 * 0.09290304)
  print(str(feetArea) + " square feet." )
  print(str(metersArea) + " square meters.")
elif measure.lower() == "meters":
  print("The area is:\n")
  
  metersArea = int(lenght) * int(width)
  feetArea = math.sqrt(metersArea**2 * 0.09290304)
  
  print(str(feetArea) + " square feet." )
  print(str(metersArea) + " square meters.")