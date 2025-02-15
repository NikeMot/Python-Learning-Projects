#Input text and chosen letters, make the ext lowercase and check
#how many times the letters appear
input_text = input("Please, input the text\n")
lower_text = input_text.lower()
text = tuple(lower_text)
letter1 = input("Please, select the first letter\n").lower()
letter2 = input("Please, select the second letter\n").lower()
letter3 = input("Please, select the third letter\n").lower()

#Print how many times each chosen letter appears in the text
print("\n")
print("LETTER REPETITIONS")

print(f"'{letter1}' appears {text.count(letter1)} times in the text")
print(f"'{letter2}' appears {text.count(letter2)} times in the text")
print(f"'{letter3}' appears {text.count(letter3)} times in the text")

#Calculate and print how many characters and words are in the text
print("\n")
print("NUMBER OF CHARACTERS AND WORDS")

input_words = input_text.split()
words = tuple(input_words)
print("The total number of characters in the text is", len(text), "and the total number of words is", len(words))

#Print the first and last characters and words in the text
print("\n")
print("FIRST AND LAST CHARACTERS AND WORDS")

print("The first and last characters of the text are", text[0], "and", text[-1])
print("The first and last words of the text are", words[0], "and", words[-1])

#Reverse the text, join it and print it
print("\n")
print("REVERSED TEXT")

reversed_words = " ".join(words[::-1])
print(f"Find below the text reversed:\n> {reversed_words}")

#Find out whether the word "Python" is found in the text
print("\n")
print("CHECK FOR THE WORD PYTHON")

search_number = int(lower_text.find("python"))
search_dict = {-1:"The word 'Python' is NOT found in the text" }
found_dict = search_dict.get(search_number,"The word 'Python' IS found in the text")
print(found_dict)

