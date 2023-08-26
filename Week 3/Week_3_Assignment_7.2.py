'''7.2 Write a program that prompts for a file name, 
then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name.'''


# Answer

total=0
count=0
file_name = input("Enter file name: ")
file = open(file_name)
for line in file:
    if not line.startswith("X-DSPAM-Confidence:") : 
    	continue
    count=count+1
    pos=line.find(':')
    value=line[pos+1:]
    total=total+float(value)
    avg=total/count
print("Average spam confidence:",avg)


# file_name = mbox-short.txt