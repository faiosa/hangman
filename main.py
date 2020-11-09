import random
import hangman_words
import hangman_art

stages = hangman_art.stages
end_of_the_game = False
lives = 6
random_word = random.choice(hangman_words.word_list)
word_length = len(random_word)
list_of_blank_underscores = list("_" * word_length)
print(hangman_art.logo)

while "_" in list_of_blank_underscores:
    user_guess = input("\nPlease enter your letter:").lower()
    is_presented_in_the_word = False
    for index, letter in enumerate(random_word):
        if letter == user_guess:
            list_of_blank_underscores[index] = letter
            print(list_of_blank_underscores)
            is_presented_in_the_word = True
    if not is_presented_in_the_word:
        lives -= 1
        print(stages[lives])
        print(f"'{user_guess}' is NOT in the word :(")
        if lives == 0:
            print("\nYou lost :(")
            exit()


print("Congratulation! You won!")
