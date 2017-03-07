# Guessing game in Python2.7 by Eloy Gil
# Email: eloy.gil@est.fib.upc.edu
# The game starts with a random number between 1 and 20.
# The player will guess and receive hints until the guess is correct.

import random, sys

random.seed(a=None)

n = random.getrandbits(5)%21
while (n == 0):
	n = random.getrandbits(5)%21

guess = input("Try to guess the number! ")

while guess != n:
	if (guess * 2 < n):
		print "The number is way bigger than " + str(guess)
	elif (guess < n):
		print "The number is bigger than " + str(guess)
	elif (guess > n * 2):
		print "The number is way smaller than " + str(guess)
	else:
		print "The number is smaller than " + str(guess)
	guess = input("Your new guess: ")

print "That's it! The correct number is " + str(guess)			
