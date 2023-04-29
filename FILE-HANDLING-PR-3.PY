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
diary.write(intro)

while response == 'y':
    message = input("Enter a line: ")
    diary = open('mylife.txt', 'a')
    diary.write(message)
    response = input("Would you like to write more lines?: ")

else:
    diary.close()

            


