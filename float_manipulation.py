# created a program that uses built in fuctions to get various outputs 

# added that import math function as stated 
import math 
import statistics
# created a list that will store the numbers enterd by the user 
Numbers = []

# user_input will ask for the user to enter a decimal number using float
# the for loop loops through user_ input 10 times 
user_input = [float(input("Enter any decimal number:")) for i in range(10)]

# added the numbers a list using append and printed it out    
Numbers.append(user_input)

print(Numbers)

# line 19 - 23 built in functions are used to dispaly the various outputs 
print("The total numbers is :", sum(user_input),"\n")
print("The largest number is:",max(user_input),"\n")
print("The smallest number is:",min(user_input),"\n")
print("The average of the numbers is:",round(sum(user_input) / len(user_input), 2), "\n" )
print("The median of the numbers is:", statistics.median(user_input))
