#P-3. (25 points). Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
#Enter line: Beautiful is better than ugly.
#   Are there more lines y/n? y
#Enter line: Explicit is better than implicit.
#   Are there more lines y/n? y
#Enter line: Simple is better than complex.
#   Are there more lines y/n? n 

#Create a program that write multiple line of text contents into a text file mylife.txt.
#Create mylife.txt. If it
intro = input("Enter a line: ")
response = input("Would you like to write more lines?: ")
diary = open('mylife.txt', 'a')
diary.write(intro), diary.write('\n')

while response == 'y' and response != 'n':

    diary = open('mylife.txt', 'a')
    message = input("Enter a line: ")
    diary.write(message), diary.write('\n')

    response = input("Would you like to write more lines?: ")

    if response == 'n':
        diary.close()

if response == 'n':
    diary.close()

            


