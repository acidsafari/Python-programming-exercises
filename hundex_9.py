# Write a program that accepts sequence of lines as input
# and prints the lines after making all characters in the sentence capitalized.

lines = []
while True :
    l = input('Please Enter Lines: ') # if you start with this, there is no exit
    if l :  #to the while loop
        lines.append(l.upper())
    else: break

for line in lines :
    print(lines)

# Suppose the following input is supplied to the program: Hello world Practice makes perfect
