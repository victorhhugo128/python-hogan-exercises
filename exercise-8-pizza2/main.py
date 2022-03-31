import math

while True:
  people = input("How many people? ")
  slices = input("How many slices per pizza? ")
  pieces = input("How many pieces each person wants? ")

  if people.isnumeric() and slices.isnumeric() and pieces.isnumeric():
    people = int(people)
    slices = int(slices)
    pieces = int(pieces)
    break

pizzas = math.ceil((people * pieces) / slices)

print("You must get " + str(pizzas) + " pizzas.")

