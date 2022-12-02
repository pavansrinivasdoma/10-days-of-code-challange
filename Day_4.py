# ******* RANDOM FUNCTION *******

# To use random function first we need to import one library, where all the required code is prebuild inside the library
import random
number = random.randint(1,10)  #Prints a random number in 1 to 10 range - integer
print(number)
float_num = random.random()  #Prints a random number in 0 to 1 range - float number
print(float_num)


# ******* RANDOM MODULE *******
# We can create our own library by creating another file and writin code there and importing that code like shown below
import Day_4_randmod
print(Day_4_randmod.name)


# ******* LISTS *******
names = ['tirupati','python','100','89.292','@#$%']  #list

print(len(names))  #prints the length i.e; numberof elements in the list

print(names[0])  #Indexing from first

print(names[-1]) #Indexing from last

names[1] = 'python programing'  #Changing/Modifyint the element in list

names.append('brother')  #adds an element and the end of the list

names.extend(['India', 'Dog']) #adds more number of elements at the end of the list

names.remove('python programing')  #Removes the particular element from the list

Sentence = "Hi, there, My, name, is, pavan"
Sentence.split(", ")  #Splits the string based on the given divider

#Nested Lists
name = ['Andhra Pradesh','Hyderabad','Tirupati']
number = ['123','234','345']
combined = [name,number] #Here can combine lists into a single list
