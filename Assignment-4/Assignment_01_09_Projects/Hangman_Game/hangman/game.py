# import random
# from hangman.words import words

# def get_valid_word(words):
#     word = random.choice(words)
#     while '_' in word or ' ' in word:
#         word = random.choice(words)
#     return word.upper()

# def hangman():
#     word = get_valid_word(words)
#     word_letters = set(word)  # letters to guess
#     alphabet = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     used_letters = set()  # what the user has guessed

#     lives = 6

#     print("🎯 Welcome to Hangman! 🎯")

#     while len(word_letters) > 0 and lives > 0:
#         print(f"\nYou have {lives} lives left. Used letters: {' '.join(used_letters)}")

#         # show the current word status
#         word_list = [letter if letter in used_letters else '-' for letter in word]
#         print("Current word: ", ' '.join(word_list))

#         user_letter = input("\nGuess a letter: ").upper()

#         if user_letter in alphabet - used_letters:
#             used_letters.add(user_letter)
#             if user_letter in word_letters:
#                 word_letters.remove(user_letter)
#                 print("✅ Correct!")
#             else:
#                 lives -= 1
#                 print("❌ Wrong guess.")
#         elif user_letter in used_letters:
#             print("⚠️ You have already used that letter. Try again.")
#         else:
#             print("⚠️ Invalid character. Try again.")

#     if lives == 0:
#         print(f"\n💀 You died, sorry. The word was {word}")
#     else:
#         print(f"\n🎉 Congratulations! You guessed the word: {word}")

import random
from hangman.words import words


def get_valid_word(words):
    word = random.choice(words)
    while '_' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    