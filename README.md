# Multiple  line of Text

<b>Write a method in python to write multiple line of text contents into a text file mylife.txt. See sample output:</b>
```sample
    Enter line: Beautiful is better than ugly.
    Are there more lines y/n? y  
    Enter line: Explicit is better than implicit.
    Are there more lines y/n? y
    Enter line: Simple is better than complex.
    Are there more lines y/n? n
```
*** 
# Program Sequence
<body>
  
  + The program opens "mylife.txt" file. If it doesn't exist, it will be generated automatically.
  
  + It will ask the user to "Enter a line: " which whenever it is entered, it will be transferred immediately to 
  ```
  "mylife.txt"
  ```
  + After the input, it will ask the user to "Would you like to enter another line?". This will be answerable by 
  ```
    'y' or 'n'
  ```
  + If any text is not 'y' or 'n' entered, the program will immediately finish.
  + This response will guide to the while loop where you will be able to write multiple lines of text.
  + To continue writing multiple lines of text, enter 'y' to prompt for another line of text.
  + Enter 'n' to stop the loop and finish the program.
  + Close the file.  
</body>

###
# Guide
+ Open a create any txt file that where the lines of the user enters will be transfered. In my case:
```
'mylife.txt'
```
+ Create input for line text.
```
message = input("Enter line: ")
```
+ Create input for user's response.
```
response = input("Are there more lines y/n?")
```
+ Open the file in append format.
```
diary = open('mylife.txt', 'a')
```
+ Write the line entered to the 'mylife.txt', Make sure to write 'diary.write('\n')' so whenever you enter a text, The next loop will start from a new line of text
  ```
  diary.write(message), diary.write('\n')
  ```
+ Create a while loop that repeats the process as long as the user enters 'y' as a response
  ```
  while response == 'y'
    open('mylife.txt', 'a')
    message = input("Enter line: ")
    diary.write(message), diary.write('\n')
    response = input("Are there more lines y/n?")
  ```
+ Shut down the program if the user enters 'n' as a response
  ```
  if response == 'n':
    diary.close()
  ```
 
