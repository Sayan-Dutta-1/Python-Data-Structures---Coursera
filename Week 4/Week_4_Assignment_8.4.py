'''8.4 Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using 
the split() method. The program should build a list of words. 
For each word on each line check to see if the word is already 
in the list and if not append it to the list. When the program completes, 
sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt'''

# Answer


#file used is romeo.txt
file_name= input("Enter file name: ")
file = open(file_name)
list = list()
for line in file:
    for i in line.split():
        if not i in list:
            list.append(i)
list.sort()
print(list)


# file_name = romeo.txt