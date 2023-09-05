#what if the player get the full word before 6 guesses?
import random

#read file and store words as list
with open ("dictionary.txt", 'r') as file:
  content = file.readlines()
  words = []
  for line in content:
    word = line.strip()
    word = word.lower()
    words.append(word)
  #print(words)

    
#randomly select one word form the list
choice = random.choice(words)


#main game loop

letters_of_choice = list(choice)
correct_guesses = []
counter = 0

def display(all_letters, correct_guesses):
  in_reply = []
  for letter in all_letters:
    if letter in correct_guesses:
      in_reply.append(letter)
    else:
      in_reply.append('_')
      
  outcome = ''.join(in_reply)
  return outcome
    
  

while counter < 6:
  if display(letters_of_choice, correct_guesses) != choice:
      guess = input("guess a letter in my word: ")
      if guess in choice:
        correct_guesses.append(guess)
        show = display(letters_of_choice, correct_guesses)
        print(show)
      else:
        print("your letter is not in my word")
        counter += 1
  else: 
    print("You win!!")
    counter = 7

if counter == 6:
  print("you have exceeded your chances")