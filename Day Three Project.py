#Input text and chosen letters

input_text = str(input("Please, input the text\n"))
input_letter1 = str(input("Please, select the first letter\n"))
input_letter2 = str(input("Please, select the second letter\n"))
input_letter3 = str(input("Please, select the third letter\n"))

#Make the text and chosen letters lowercase and check how often the letters appear

lower_text = input_text.lower()
letter1 = input_letter1.lower()
letter2 = input_letter2.lower()
letter3 = input_letter3.lower()
text = tuple(lower_text)

#Print how many times each chosen letter appears in the text

print(f"'{letter1}' appears {text.count(letter1)} times in the text")
print(f"'{letter2}' appears {text.count(letter2)} times in the text")
print(f"'{letter3}' appears {text.count(letter3)} times in the text")

#Calculate and print how many characters and words are in the text

input_words = input_text.split()
total_words = tuple(input_words)
print("The total number of characters in the text is", len(text), "and the total number of words is", len(input_words))

#Print the first and last characters and words in the text

print("The first and last characters of the text are", text[0], "and", text[-1])
print("The first and last words of the text are", words[0], "and", words[-1])
