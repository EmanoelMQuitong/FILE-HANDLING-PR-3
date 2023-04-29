#P-3. (25 points). Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:
#Enter line: Beautiful is better than ugly.
#   Are there more lines y/n? y
#Enter line: Explicit is better than implicit.
#   Are there more lines y/n? y
#Enter line: Simple is better than complex.
#   Are there more lines y/n? n 

#COLOR options and text manipulations:  
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

#Create a program that write multiple line of text contents into a text file mylife.txt.
#Create mylife.txt. first input and response.

#FIRST INPUT
print('\n')
print(DARKCYAN+BOLD+"Enter a line: "+END)
intro = input("     ")

#RESPONSE
print('\n')
print(DARKCYAN+BOLD+"Would you like to write more lines?: "+END)
response = input("      ")
print('\n')

diary = open('mylife.txt', 'a')
diary.write(intro), diary.write('\n')
response.lower()

#while loop for repeated function creating lines to mylife.txt.
while response.lower() == 'y':              #Repeated function as long as response is 'y'

    diary = open('mylife.txt', 'a')         #Opens file mylife.txt. 

    print(DARKCYAN+BOLD+"Enter a line: "+END)   
    message = input("     ")                #Input to enter in mylife.txt, can be repeated as long as response is 'y'.
    diary.write(message), diary.write('\n') #Input that is transferred to mylife.txt.

    print('\n')
    print(DARKCYAN+BOLD+"Would you like to write more lines?: "+END)        #Decides factor to repeat the process. Should only choose from 'y' and 'n'.
    response = input("      ")   
    
    if response == 'n':                     
        diary.close()                       #Shuts down the program after repeated process 
        print(PURPLE+BOLD+"The lines you have been successfully transferred on 'mylife'.txt. The program is closing now."+END)

    else:
         diary.close()                      #Shuts down the program automatically whenever the response entered does not belong to 'y' and 'n'.


if response.lower() == 'n':                 #Shuts down the program without repetition.
    diary.close()
    print(PURPLE+BOLD+"The lines you have been successfully transferred on 'mylife'.txt. The program is closing now."+END)

else:                                       #Shuts down the program automatically whenever the response entered does not belong to 'y' and 'n'.
    diary.close()
    print(RED+BOLD+"Please choose from 'y' or 'n' only if you want to proceed. Thank you! The program is closing now."+END)  

            

            


