# ******* LOOPS *******
#Loop allow us to run same line of code multiple times
NAMES = ['helo', 'apple', 'girraffe']
for name in NAMES:  #Every time it runs it assigns the element/value to name variable
    print(name)
    print(name+' bro')

#Range function
# for number in range(a,b,z) **here, a is first number, b is last number and z in the range limit
for number in range(1,10,2): #range function sets the respective variable in between the range of 1 and 10(excluding 10) 
    print(number)
#Print sum of first 100 natural numbers
total=0
for number in range(1,101):
    total+=number
print(total) 

#Print the greatest number using loops
numbers = input("Input a list of numberss ").split()
for n in range(0, len(numbers)):
  numbers[n] = int(numbers[n])
print(numbers)

highest_num = 0
for num in numbers:
    if num>highest_num:
        highest_num=num
print(f"The highest number in the list is: {highest_num}")



