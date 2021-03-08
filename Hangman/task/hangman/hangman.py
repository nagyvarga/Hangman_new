# Write your code here
import random

print("H A N G M A N")

list_of_words = ["python", "java", "kotlin", "javascript"]

english_letters = set("abcdefghijklmnopqrstuvwxyz")

while True:

    print('Type "play" to play the game, "exit" to quit: > ')
    menu_input = input()

    if menu_input == "exit":
        break
    elif menu_input != "play":
        continue

    word = random.choice(list_of_words)
    unique_letters = set(word)
    puffer = "-" * (len(word))
    puffer_gaps = list(puffer)

    writed_letters = set()

    length_of_word = len(word)
    number_of_life = 8

    while number_of_life > 0:
        print('\n' + puffer)
        print("Input a letter: > ")
        guess_letter = input()

        if len(guess_letter) > 1:
            print("You should input a single letter")
            continue

        if guess_letter not in english_letters:
            print("Please enter a lowercase English letter")
            continue

        if guess_letter in writed_letters:
            print("You've already guessed this letter")
            continue

        repeat = False
        if guess_letter in unique_letters:
            index = 0
            if guess_letter in puffer_gaps:
                repeat = True
            puffer = ""
            for character in word:
                if character == guess_letter:
                    puffer_gaps[index] = guess_letter
                    if not repeat:
                        length_of_word -= 1
                puffer += puffer_gaps[index]
                index += 1
            # print(puffer_gaps)
        else:
            print("That letter doesn't appear in the word")
            number_of_life -= 1
        if length_of_word == 0:
            print("You guessed the word!\nYou survived!")
            number_of_life = 0

        writed_letters.add(guess_letter)

    if length_of_word > 0:
        print("You lost!")
