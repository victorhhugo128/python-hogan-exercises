while True:
  people = input("How many people? ")
  pizzas = input("How many pizzas? ")
  slices = input("How many slices per pizza? ")

  if people.isnumeric() and pizzas.isnumeric() and slices.isnumeric():
    people = int(people)
    pizzas = int(pizzas)
    slices = int(slices)
    break

slices = slices * pizzas
slicesperperson = int(slices / people)

print("Each person gets " + str(slicesperperson), end= " ")

if(slicesperperson > 1):
  print("pieces of pizza.")

else: 
  print("piece of pizza.")

print("There are " + str(slices % people) + " leftover pieces.")