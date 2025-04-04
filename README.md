# 16 Day Python Learning Challenge
## Learning Python via small projects

The projects are taken from the *Total Python: You Can Master Python Programming in 16 Days* course on Udemy.

## Day One 

You're going to create Python code that asks your friend to answer two questions that
require a single word each and then displays those combined words on the screen to
form a creative brand.


## Day Two 

The situation is this: You work in a company where salespeople receive 13%
commissions on their total sales, and your boss wants you to help the salespeople
calculate their commissions by creating a program that asks them their name and
how much they've sold this month.
Your program will answer them with a sentence that includes their name and the
amount of commissions they are entitled to



## Day Three 


The task is as follows:
You are going to create a program that first asks the user to
enter text. It can be any text, an entire article, a paragraph, a sentence, a poem,
whatever you want. Then the program will ask the user to enter three random letters.
From that moment on, our code is going to process that information and result in five
different types of analysis:

*1. How many times each of those letters they have chosen appears.*

*2. How many words are in the whole text?*

*3. What are the first and last letters of the text?*

*4. The system will show us how the text would look like if we inverted the order of the words.*

*5. The system will tell us if the word “Python”*


## Day Four 


The task is this: 

The program will ask for the user's name and then it will say something like: 
“Well John, I've thought of a number between 1 and 100 and you have only eight tries to guess it. What number do you think it is?” 
On each try, the player will say a number and the program can answer for different things.

*1. If the number the user said is less than 1 or greater than 100, it will tell them that he/she has chosen a number that is out of play.*

*2. If the number the user chose is less than the number the program thought of, it will tell them that the answer is wrong, and that he/she chose a lower number than the secret number.*

*3. If the user chose a number greater than the secret number, it will let them know that it was greater.*

*4. And if the user got the secret number right, they will be informed that they have won, and how many tries that has taken them*

*5. If the user has not guessed correctly in their first attempt, they will be asked again to choose another number and so on until they win or until their eight attempts are done*

## Day Five


Today you are going to program the hangman game.

It's simple, popular, but if you don't know it, let me explain it really quickly: The program will choose a secret word and we'll show the player only a series of dashes that represent the number of letters in the word. 

In each turn, the player must choose a letter: 

if that letter is in the hidden word, the system will show where it is located, but if the player chooses a letter that is not in the hidden word, they lose a life.

In the real hangman game, each time we lose a life, the drawing of the hangman is completed limb by limb, but in our case, as we still do not have the graphic elements, we will simply tell the user that they have six lives, and we will deduct them one by one for each time the player chooses an incorrect letter.*

## Day Six

Today you are going to create a recipe manager. 

It’s a program by which a user can read, create and delete recipes from a database. Before you start, you need to create a folder directory in the base folder of your computer: it is a folder called Recipes, which contains four subfolders and each of them contains two text files. 

Inside the files, you can write whatever you want. It's not important what it says in each in each text file for this exercise. If you prefer, you can download and unzip the file that we've attached to this lecture and place it in the root directory, if you don't feel like building out that structure yourself. 
Once you have done that, here comes your task:

Your code will first welcome the user, tell them the path to the directory where our Recipes folder is located, tell them how many recipes there are inside the folder, and then ask them to choose one of these options:

*1. Option 1 will ask the user “Which category do you choose?” Meats, salads, desserts… whatever categories you want. And once the user chooses a category, it will ask them “Which recipe do you want to read?” And then it will show the content of that recipe.*

*2. Option 2 is getting the user to create a new recipe in a specific category: it will also ask the user to choose a category, but then it will ask the user to write the name and content of a new recipe, and it will create that file in the correct place.*

*3. Option 3 will ask for the name of the category the user wants to create and will generate a brand new folder, a new category with that name*

*4. Option 4 will delete recipes: it’ll do the same as option one, but instead of reading the recipe, it will delete it.*

## Day Seven

It's time to program with object-oriented programming principles in mind. I'm going to ask you to create a code that allows a person to perform operations on their bank account.
Don't be scared, the instructions will be well defined so that you can do it quickly:

*1. First, you are going to create a class called Person, and the person is going to have only two attributes: first name and last name. That's it.

*2. Then, you are going to create a second class called Customer. This class will inherit from Person because customers are persons, but it will also have its own attributes such as account number and balance. For example, the bank account balance.*

*3. But that's not all: the Customer will also have three methods:*
   
    a. The first one is going to be one of the special methods, and it is going to be the one that allows us to print our client. When the code asks to print the client, this method will allow their data to be displayed,         including their account balance.
    b. Then, a method called deposit, which allows the user to decide how much money they want to add to their account.
    c. And finally, a method called withdraw, which allows the user to take money and deduct it from their account.
    d. Once you have created these two classes, you have to create the code for your program to run, asking the user to choose whether they want to make a deposit or withdrawal.
   
*The user can make as many transactions as they want until they decide to exit the program. Therefore, our code has to keep track of how much money is in the balance,
and you must make sure that the customer never withdraws more money than they have.*

*5. Option 5 will let the user delete a category, asking “Which category do you want to delete?”*

*6. Option 6 will end the execution of the code (just end the program).*

## Day Eght

Now it's time to put it all into action in a new program. Today's challenge is for you to create a software that works like a ticket vending machine in a drugstore. 
What's a ticket vending machine? 
It's a machine you can find at the entrance of many stores or banks. 
This machine asks you what procedure you've come to perform, and assigns you a turn number according to the area you want to go.

In our case, you are going to create it for a drugstore where there are three areas of attention:perfumes, medicine and cosmetics. 
Your program will ask the customer which of the areas they want to go, and it’ll give them a shift number depending on which area they go to.
For example, if I choose cosmetics, it will give me the letter C (as in cosmetics), - (dash) 54.
After this, it will ask us if we want to take another number to simulate that a new client is
coming, and it will repeat the whole process.
Some things to keep in mind:

*1. Different customers will be taking different numbers for different areas (perfumes,
medicine, cosmetics) in a different order, so the system must keep track of how many
numbers it has given for each of those areas and produce the next number for each area
as they ask for it. You probably already understand that we need to take advantage of
generators and their efficiency to do this.*

*2. The message where we tell the customer they're waiting number should have some
additional text before and after the number. For example: “Your number is…” then the
number itself with the letter at the beginning, and something like “Wait and someone
will be with you shortly”. In order for our code not to repeat itself, instead of putting this
text in each of the functions that calculate the numbers, we can take advantage of the
decorators flexibility to create that additional text only once and then wrap any of our
functions with that unique text.*

*3. Finally, you should take advantage of the fact that you now know how to split your
program into different modules and separate the code into two parts: on the one hand,
a module that can be called numbers.py, where you write all the generators and the
decorator, then a second module which we can call main.py, where you write the
functions that manage the operation of the program (for example, instructions to choose
an area and to decide if it will continue taking new clients or end the program).*

## Day Nine

Your job is to create a Serial Number Finder. What is that? It's a program that will search for serial numbers that match a certain format, within a tree of folders.

Your program will go through all the folders, subfolders and files in a root directory (in this case, the folder you just unzipped), and look for any string that matches the description. We know that there can't be more than one serial number per file.

To achieve this you are going to use 2 things: the OS module to open and iterate through the directory, and regular expressions to find the correct serial number format.

For the purposes of this exercise, these are the format conditions that the findings must meet:
- [N] + [three text characters] + [-] + [5 numbers].

For example: Nryu-112365

The on-screen presentation of the findings should be a list in table format, respecting the following example format:

----------------------------------------------------
Search date: [today's date]

FILE		SERIAL NO.
----		----------
text1.txt 	Nter-15496
text25.txt 	Ngba-85235

Numbers found: 2
Search duration: 1 seconds
----------------------------------------------------

IMPORTANT

*The 'Search duration' must be rounded up.*

*Don't forget that the best way to traverse a folder tree is probably with the walk() method of OS.*

*Note that the search date must be the date of the day you run the code, so you need to use the datetime module.*

*We encourage you to find a way to display today's date in the format dd/mm/yy.*

*To report the duration of the search at the end of your presentation, you will need the time module.*

*Remember that in order to print everything in table format you can use the special characters to tabulate.*

## Day Ten

Create a space invaders clone

