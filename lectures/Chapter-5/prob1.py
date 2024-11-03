

Dictionary = {
    "pankha": "fan",
    "dwaar": "door",
    "khidki": "window",
    "kitab": "book",
    "kursi": "chair"
}


word = input("Enter the Hindi word you want to look up: ")


translation = Dictionary.get(word, "Word not found in dictionary")
print(f"The English translation of '{word}' is: {translation}")