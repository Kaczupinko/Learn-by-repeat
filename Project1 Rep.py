# Learn by repeat (save/load file, shuffle elements, dictionary that compare key to meaning, repeat bad answers)

import json
import random


def save_dictionary(dictionary, file_name):
    with open(file_name, "w") as file:
        json.dump(dictionary, file)


def load_dictionary(file_name):
    with open(file_name, "r") as f:
        dictionary = json.load(f)
    return dictionary


def quiz(dictionary):
    words = list(dictionary.keys())
    random.shuffle(words)
    correct_answers = 0
    for word in words:
        print("What is the translation of the word: ", word)
        answer = input("Your answer! ")
        if answer.lower() == dictionary[word].lower():
            print("Correct answer!")
            correct_answers += 1
        else:
            print("Incorrect answer. The correct answer is:", dictionary[word])
    print("End of quiz. Your score is:", correct_answers, "out of", len(words))


def review(dictionary):
    incorrect_words = []
    for word in dictionary:
        print("What is the translation of the word: ", word)
        answer = input("Your answer: ")
        if answer.lower() != dictionary[word].lower():
            incorrect_words.append(word)
    if len(incorrect_words) == 0:
        print("Congratulations! You have no words to review")
    else:
        print("Words to review:", ",".join(incorrect_words))


file_name = "dictionary.json"
dictionary = {}

try:
    dictionary = load_dictionary(file_name)
    print("Dictionary loaded from file", file_name)
except FileNotFoundError:
    print("File", file_name, "not found - creating new dictionary.")

while True:
    print("Choose an option:")
    print("1 - Test")
    print("2 - Review")
    print("3 - Add a new word")
    print("4 - Save the dictionary")
    print("5 - Exit")
    choice = input("Your choice: ")
    if choice == "1":
        quiz(dictionary)
    elif choice == "2":
        review(dictionary)
    elif choice == "3":
        word = input("Enter a new word: ")
        meaning = input("Enter the meaning of " + word + ": ")
        dictionary[word] = meaning
        print("Word added to the dictionary.")
    elif choice == "4":
        save_dictionary(dictionary, file_name)
        print("Dictionary saved to file", file_name)
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
