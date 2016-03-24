#Assignment: (Homework #3a) 
# 
#Description: (Computer guessing game) 
# 
#Author: (Robert Crismon) 
#
#Completion Time: (4 hours) 
# 
#In completing this program, I obtained help or worked with the following: 
#(List people and websites here)

from random import * #randint() will NOT work w/out this!!!

print("Let's play a guessing game!")

print("Please think of a number between 0 and 100.")
print("When you have thought of a number, press ENTER to continue")
input() #acts as stop to program, allowing player to "think of a number", then start the main program.

low_bound = 0 #initial lower bound
high_bound = 100 #initial upper bound

player_number = None 
#variable managing when program finishes. If player_number = anything other than None (ie, computer_guess), then program ends

while player_number == None: #first WHILE loop
	computer_guess = randint(low_bound, high_bound)
	print("The computer guesses: ", computer_guess)
	confirmation = input("Is the number too high (h), too low (l), or correct (c)? ")
	confirmation = confirmation.lower() 
	#converts user input to a lowercase string, allowing c, h, and l to work within this code without throwing an error
	if confirmation == 'c':
		player_number = computer_guess
		print("I won!")
		#if this segment of the main WHILE loop executes, the nested WHILE below will not execute, and program will end.
		
	else:
		high_low = None
		#high_low variable allows the WHILE loop below to execute without getting stuck in itself
		while high_low == None: #WHILE loop within main loop
			if confirmation == 'h':
				high_low = computer_guess
				high_bound = high_low
			elif confirmation == 'l':
				high_low = computer_guess
				low_bound = high_low