#Assignment: (Homework #3b) 
# 
#Description: (Player guessing game) 
# 
#Author: (Robert Crismon) 
#
#Completion Time: (4 hours) 
# 
#In completing this program, I obtained help or worked with the following: 
#(List people and websites here)

from random import * #randint() will NOT work w/out this!!!

print("Let's play a guessing game!")

print("I will think of a number between 0 and 100.")
print("When you are ready, press ENTER to continue")
input()

low_bound = 0
high_bound = 100

player_guess = 0 #variable for player guessing computer's number
computer_number = randint(low_bound, high_bound) #low_bound, high_bound defined for later additions, alterations

while player_guess != computer_number: #!= means while [var/object] is NOT [var/object]
	#print(computer_number) 
	# ^ DEBUG
	player_guess = input("Guess my number: ")
	player_guess = int(player_guess) #converts player_guess to integer
	if player_guess == computer_number:
		print("You won!")
	
	else:
		#no WHILE loop needed
		if player_guess >= computer_number:
			print("Too high!")
			#human player automatically makes a 'too high' guess the new upper bound in mind
		elif player_guess <= computer_number:
			print("Too low!")
			#human player automatically makes a 'too low' guess the new lower bound in mind