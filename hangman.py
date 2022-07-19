# Hangman
import random
list_Of_words = ["camel","deer","lion","tiger","cow"]
chosen_word = random.choice(list_Of_words)
lives = 6

display = []
for letter in range(len(chosen_word)):
    display.append("_")
print(display)

end_of_the_game = False
while not end_of_the_game:
    user_guess = input("Enter a letter: ").lower()

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == user_guess:
            display[i]= letter
    print(display)
    
    if user_guess not in chosen_word:
        lives -= 1
        if lives == 0:
            print("You lose")
            break
        else:
            continue

    if "_" not in display:
        end_of_the_game = True
        print("You Win")
    
print("Your guess was correct " + "".join(display))