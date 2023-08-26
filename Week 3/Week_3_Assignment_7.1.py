'''7.1 Write a program that prompts for a file name, 
then opens that file and reads through the file, 
and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt'''

# Answer

file_name = input("Enter file name: ")
file = open(file_name)
for line in file.readlines():
    print (line.upper().strip())


# file_name = words.txt