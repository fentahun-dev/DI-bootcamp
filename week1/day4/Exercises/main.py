

my_fav_numbers = {1,2,3,4}
my_fav_numbers.update(5,6)
my_fav_numbers.remove(6)
friend_fav-numbers = {12,14,7,8 }
our_fav_numbers = my_fav_numbers | friend_fav_numbers

tupel_numbers = (7,8,9)
tupel_numbers.add(6) 
print(tupel_numbers) # not changed tupel is immutable


basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("banana","Blueberries")
basket.insert( 0,"Apples" )
basket.append("Kiwi")
print(basket_counts[Apples])
basket.clear()
print(basket)

numbers = [ 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
numbers = []
mumber = 1.5
while number <= 5:
  numbers.append(number)
  number = number + 0.5
  print(numbers)

for number in range(1,20)
print(number)

numbers = (1,20)
index = 0
for number in numbers:
  print(index,number)
  index += 1



name =input("inter your name:")
while True:
  if len(name) < 3:
    print("name is short")
  elif name.isdigit():
    print("name cannot contain numbers")
  elif not name.isalpha():
    print("Name must contain Letters only")
  else:
    break
    name = input("Enter your name:")
    print("Thank you!")


 fruits = input("Enter your favourite fruits:").splite()
fruit = input("Choose one fruit:")
if fruit in fruits:
  print("You chose one of your favorite fruits! Enjoy!")
else:
  print("You chose a new fruit. I hope you enjoy it!")

pizza_topping = []
while True:
  pizza_topping = input ("Enter a pizza topping:")
  if pizza_topping == "quite":
    break
    pizza_toppings.append(pizza_topping)
    print(f"Adding {pizza_topping} to your pizza")
    
    total = 10 + len(pizza_toppings:) * 2.5
    
    print(f"Your toppings:{pizza_toppings}")
    print(f"total cost: ${total:.2f}")
  
total = 0
for person in range(4):
  age = int(input("Enter age:"))
  if age < 3:
    total += 0
  elif age <= 12:
  total += 10
else:
  total += 15
  print(f"Total cost: ${total:.2f}")

age = []
for person in range(6):
  age =int(input("Enter age:"))
  if 16 <= age <= 21:
    attendees.append(age)
    print(f"Final attendees: {attendees}")

