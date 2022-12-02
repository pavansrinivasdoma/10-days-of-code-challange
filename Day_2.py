# ******* DATA TYPES *******
#STRINGS 
s="Hey there, How are you???"
print("HELLO"[0]) #INDEXING
print('123'+'456')
#INTEGER
i=123456
print(123+456)
print(123_456_789) # HERE _ IS LIKE COMMA{AS COMPUTERS CAN INTERPRET THIS SIGN}
#FLOAT
f=8.164
print(8.9195)
#BOOLEAN
t=True  
f=False
#CHECKING TYPE
print(type(s))
print(type(i))
print(type(f))
print(type(i))


# As we discussed in prev. day's file, integer and string couldn't be concatinated we have one technique that converts integer to string
num=input("Enter a number: ")
new_num=str(num)
print(new_num+" is the number that user gave")
#Like wise string can also be converted into integer
a="3"
print(type(a))
x=int(a)
print(type(x))


# ******* MATHEMATICAL OPERATIONS *******
3+4  #ADDITION
2-1  #SUBTRACTION
2*4  #MULTILPICATION
9/3  #DIVISION - Prints float value
9//3 #DIVISION - Prints integer value
2**3 #POWER
10%2 #REMAINDER 
#NOTE: Python follows "PEMDAS RULE" in solving mathematical operations {priority order from top to bottom}
                  #    Paranthesis - ()
                  #    Exponants - **
                  #    Multiplication - *
                  #    Division - /
                  #    Addition/Subtraction - +/-
#ROUND FUNCTION
print(round(3.14567893219876,2)) # Roundoff the long decimal value to two decimal value
print(round(3.14567893219876,3)) # Roundoff the long decimal value to three decimal value
#Like wise we can round off the the value to required number of decimals
#NUMBER MANIPULATION
school=10
school+=5  #Manipulates the previous values and assign it to same variable


# ******* f-STRING *******
#We know that, to print the different data types string, integer in a single print statement gives error[without converting]
#So we use f-string to convert all at a time
numb=10
charac="ten"
bool=True
print(f"number is {numb}, word is {charac}, value is {bool}")
