string_input = input("Insert a word: ")
string_vowel = string_input.lower()
vowel_counter = 0
i = 0
for i in range(len(string_vowel)):
    if (
        (string_vowel[i] == "a")
        or(string_vowel[i]== "e")
        or(string_vowel[i]== "i")        
        or(string_vowel[i]== "o")
        or(string_vowel[i]== "u")
    ):
        vowel_counter += 1
print("The number of vowels is: " , vowel_counter)