from hangman_words import word_list
import hangman_art
import random

print(hangman_art.logo)

end_of_game = True
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"
    
    
lives=6
print()
while end_of_game:
    guess = input("Guess a letter: ").lower()
    t=0
    if guess in display:
            print(f"You've already guessed {guess}")
    for position in range(0,word_length):
        letter = chosen_word[position]
        
        if letter == guess:
          display[position] = letter
          t=1
    if t==0:
      lives-=1
      print(f"Remaining lives - {lives}")
    if lives==0:
      print("\n\nYOU LOSE")
      end_of_game=False
      
            
          
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game=False
        print("\n\nYOU WIN")
    print(hangman_art.stages[lives])
