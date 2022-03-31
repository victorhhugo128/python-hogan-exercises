import math

shape = input("What is the shape of the room (round, square, L)? ")

while True:
  if shape.lower() == 'round':
    m1 = input("Enter with the radius of the room? ")
    if m1.isnumeric():
      m1 = int(m1)
      break
  elif shape.lower() == 'l':
    m1 = input("Enter with the first measurement (a) of the room: ")
    m2 = input("Enter with the second measurement (b) of the room: ")
    m3 = input("Enter with the third measurement (c) of the room: ")
    m4 = input("Enter with the fourth measurement (d) of the room: ")
    if m1.isnumeric() and m2.isnumeric() and m3.isnumeric() and m4.isnumeric():
      m1 = int(m1)
      m2 = int(m2)
      m3 = int(m3)
      m4 = int(m4)
      break
  elif shape.lower() == 'square':
    m1 = input("Enter the lenght of the room: ")
    m2 = input("Enter the width of the room: ")
    if m1.isnumeric() and m2.isnumeric():
      m1 = int(m1)
      m2 = int(m2)
      break

  print("Please enter only numbers: ")


if shape.lower() == 'round':
  pi = 3.141592653589793
  area = m1**2 * pi
  gallons = math.ceil(area / 250)

  print("You will need to purchase " + str(gallons) + " gallons of paint to cover " + str(area) + " square feet.")

elif shape.lower() == 'l':
  area = m1*m2 + m3*m4 - m4*m1
  gallons = math.ceil(area / 250)

  print("You will need to purchase " + str(gallons) + " gallons of paint to cover " + str(area) + " square feet.")

elif shape.lower() == 'square':
  area = m1*m2
  gallons = math.ceil(area / 250)

  print("You will need to purchase " + str(gallons) + " gallons of paint to cover " + str(area) + " square feet.")