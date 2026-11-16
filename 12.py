# Lab 12 - Document Analysis System

# 1. Take input from the user
sentence = input("Enter a sentence: ")

# 2. Analyze the sentence and count
total_characters = len(sentence)

# Split by whitespace to count words
words_list = sentence.split()
total_words = len(words_list)

vowels = "aeiouAEIOU"
total_vowels = 0
total_consonants = 0
total_digits = 0
total_spaces = 0
total_special = 0

for char in sentence:
    if char.isalpha():
        if char in vowels:
            total_vowels += 1
        else:
            total_consonants += 1
    elif char.isdigit():
        total_digits += 1
    elif char.isspace():
        total_spaces += 1
    else:
        total_special += 1

total_letters = total_vowels + total_consonants
vowel_percentage = (total_vowels / total_letters * 100) if total_letters > 0 else 0.0

# 3. Display all results in a clean, formatted report
print("\n" + "=" * 55)
print("                    DOCUMENT ANALYSIS REPORT")
print("=" * 55)
print(f"Sentence: {sentence}")
print(f"Total characters: {total_characters}")

print("\n--- Character Breakdown ---")
print(f"Words              : {total_words}")
print(f"Vowels             : {total_vowels}")
print(f"Consonants         : {total_consonants}")
print(f"Digits             : {total_digits}")
print(f"Spaces             : {total_spaces}")
print(f"Special characters : {total_special}")

print("\n--- Summary ---")
print(f"Total letters      : {total_letters}")
print(f"Vowel percentage   : {vowel_percentage:.1f}%")

print("\n" + "=" * 55)
print("Analysis Complete!")
print("=" * 55)