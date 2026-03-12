def count_character_frequency(text):
    text = text.lower()  # make everything lowercase
    freq = {}
    for char in text:
        if char.isalpha():  # only count letters
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq

# Example test
print(count_character_frequency("Hello World"))  
# Output: {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
