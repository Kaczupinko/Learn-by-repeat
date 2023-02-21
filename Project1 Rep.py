# Learn by repeat (save/load file, shuffle elements, dictionary that compare key to meaning, repeat bad answers)

import json
import random


def save_dictionary(dictionary, file_name):
    with open(file_name, "w") as file:
        json.dump(dictionary, file)


def load_dictionary(file_name):
    with open(file_name, "r") as file:
        dictionary = json.load(file)
    return dictionary


file_name = "dictionary.json"
dictionary = {}

try:
    dictionary = load_dictionary(file_name)
    print("Dictionary loaded from file", file_name)
except FileNotFoundError:
    print("File", file_name, "not found - creating new dictionary.")
