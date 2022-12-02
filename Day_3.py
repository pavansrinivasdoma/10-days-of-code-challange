# ******* CONDITIONAL STATEMENTS *******
#if-else conditions

# Example - 1
Name = "hi"
if Name =="hi":  #If this condition is true
#NOTE: Remember to keep double equals to sign in condition, because if you keep only one equals to sign it becomes variable and gives error in output
    print(True)  #it will print this statement
else:            #else, else part will print
    print(False)

# Example - 2
age = int(input("enter your age: "))
print(type(age))
if age>=18:
    print("you are eligible for driving licence")
else:
    print("you are not eligible")

# Example - 3
number = int(input("Which number do you want to check? "))
if number%2==0:
    print("This is an even number.")
else:
    print("This is an odd number.")


#Nested if-else conditions
#Note: In if-else condition we can only check 2 conditions. But in nested if-else condition we can check n number of conditions

# Example - 1
age = int(input("enter your age: "))
print(type(age))
if age>=18:  #
    print("you are eligible for driving licence")
    eligibility=input("Are you prepared for LLR test(y/n)")
    if eligibility=="y":  
        print("Eligible for the test drive")  #if this has to print, the above 2 if conditions must be true
    else:
        print("Not eligible")  #if this has to print the first if condition must be true and second if condition should be false
else:
    print("you are not eligible")

# Example - 2
#Find the year is leap year or not
year = int(input("Which year do you want to check? "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


#elif conditions
#NOTE: If there are many if conditions we can make use of elif condition

#Example: Ticket Counter
age = int(input("enter your age: "))
if age<=12:
    print("pay 20rs")
elif age<=18:
    print("pay 40rs")
elif age>18:
    print("pay 60rs")
else:
    print("you cant take a ride")


#MULTIPLE if STATEMENTS
#NOTE: The difference between if-elif and multiple-if-statements is that in multiple-if-statements every condition is checked- 
#      -and if all are satisfied only it print the output. Whereas in if-elif statements any one condition can be true 

#Example - Ticket printer
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride.")


#LOGICAL OPERATORS - {and, or, not}
a=11
if a>10 and a<15:
    print('True')  #It will print only if above 2 conditions are true
else:
    print ('False')

if a>11 or a<12:
    print('True')  #It will print if any one of the above condition is true
else:
    print('False')


# ******* SOME IMPORTANT FUNCTIONS *******
#lower function - This function is used to convert upper case words to lower case
name = "PaVaN"
print(name.lower())

#upper function - This is similar to lower function, as this function converts lower cases to upper cases
print(name.upper())

#count function - This function is used to count the number of elements in a string
print(name.count('a'))
