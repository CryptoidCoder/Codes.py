# This is a word game
import random


def print_scaffold(errors, wd): # prints the scaffold
                if (errors == 0):
				print ("_________")
				print ("|	 |")
				print ("|")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (errors == 1):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|")
				print ("|")
				print ("|")
				print ("|________")
		elif (errors == 2):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	 |")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (errors == 3):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (errors == 4):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|")
				print ("|________")
		elif (errors == 5):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ ")
				print ("|________")
		elif (errors == 6):
				print ("_________")
				print ("|	 |")
				print ("|	 O")
				print ("|	\|/")
				print ("|	 |")
				print ("|	/ \ ")
				print ("|________")
				print ("\n")
				print ("The word was %s.") %wd
				print ("\n")
				print ("\nYOU LOSE! TRY AGAIN!")
				print ("\nWould you like to play again, type y for yes or n for no?")
				again = str(raw_input(("> "))
				again = again.lower()
				if again == ("y"):
                                    hangMan()
				return

def selectWord():
	file = open('C:\Users\Joshua\OneDrive - The Holy Trinity Church of England Secondary School\school\coding stuff\hangman\words.py')
	words = file.readlines() 
	myword = 'a'
	while len(myword) < 4: # makes sure word is at least 4 letters long
	  myword = random.choice(words)
  	myword = str(myword).strip('[]')
  	myword = str(myword).strip("''")
  	myword = str(myword).strip("\n")
  	myword = str(myword).strip("\r")
	myword = myword.lower()
	return myword


def hangMan():
  errors = 0					
  word = selectWord()				
  word_list = list(word)	
  blanks = ("_")*len(word)	
  blanks_list = list(blanks) 
  new_blanks_list = list(blanks)
  guess_list = []
  
  print ("Let's play hangman!\n")
  print_scaffold(errors, word)
  print ("\n")
  print ("(" + ' '.join(blanks_list)
  print ("\n")
  print ("Guess a letter.\n")
  
  while errors < 6:
  
  		guess = str(raw_input(("> "))
  		guess = guess.lower()
  		
  		if len(guess) > 1:
  				print ("Stop cheating! Enter one letter at time.")
  		elif guess == (""):
  				print ("Don't you want to play? Enter one letter at a time.")
  		elif guess in guess_list:
  				print ("You already guessed that letter! Here is what you've guessed:")
  				print ' '.join(guess_list)
  		else:
  				guess_list.append(guess)
  				i = 0
  				while i < len(word):
  						if guess == word[i]:
  								new_blanks_list[i] = word_list[i]
  						i = i+1
  
  				if new_blanks_list == blanks_list:
  						print ("Your letter isn't here.")
  						errors = errors + 1
  						print_scaffold(errors, word)
  						
  						if errors < 6:
  								print ("Guess again.")
  								print ' '.join(blanks_list)
  						
  				elif word_list != blanks_list:
  						
  						blanks_list = new_blanks_list[:]
  						print ' '.join(blanks_list)
  						
  						if word_list == blanks_list:
  						  print ("\nYOU WIN! Here is your prize:")
  						  print ("\n")
  						  print ("Would you like to play again?")
  						  print ("Type 1 for yes or 2 for no.")
  						  again = str(raw_input(("> "))
  						  if again == ("1"):
  						    hangMan()
  						  quit()
  						
  						else:
  								print ("Great guess! Guess another!")
												
hangMan()



	






