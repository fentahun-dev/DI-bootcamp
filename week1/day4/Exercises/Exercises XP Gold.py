# exercise one concatenate lists 
a = [ 1,2,3,4]
b = [5,6,7,8]
c = [*a,*b]

# exercise 2 range of numbers 
for i in range(1500,2501):
  if i % 5 == 0 and i % 7 == 0:
    print(i)

# exercise check the index 
# Exercise 3 
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
name =input("Enter your name: ")
if name in names:
  index = name.index(name)
  print("The name is at index:",index)
else:
  print("Name not found")

# Exercise 4 Greatest Number 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
num3 = int(input("Enter first number: "))
greatest = num1
if num2 > greatest:
  greatest = num2
if num3 > greatest:
  greatest = num3
print ("The greatest number is:", greatest)  

Exercise 5: The Alphabet
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
for letter in alphabet:
        if letter in vowels:
                print(letter, "is a vowels")
        else:
                print(letter,"is aconsonant")
                

Exercise 6: Words and letters






