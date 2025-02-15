#Input text and chosen letters
input_text = str(input("Please, input the text\n"))
input_letter1 = str(input("Please, select the first letter\n"))
input_letter2 = str(input("Please, select the second letter\n"))
input_letter3 = str(input("Please, select the third letter\n"))

#Make the text and chosen letters lowercase and check how many times the letters appear
lower_text = input_text.lower()
letter1 = input_letter1.lower()
letter2 = input_letter2.lower()
letter3 = input_letter3.lower()
text = tuple(lower_text)

#Print how many times each chosen letter appers in the text
print(f"'{letter1}' appears {text.count(letter1)} times in the text")
print(f"'{letter2}' appears {text.count(letter2)} times in the text")
print(f"'{letter3}' appears {text.count(letter3)} times in the text")
