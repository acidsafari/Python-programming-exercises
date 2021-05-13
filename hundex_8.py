'''Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them alphabetically.
'''
words = input('Please Enter Words separated by Comma: ')
if len(words) < 1 :
    words = 'without,hello,bag,world'

l = words.split(',')
l.sort()
print(','.join(l))

'''Suppose the following input is supplied to the program: without,hello,bag,world
Then, the output should be: bag,hello,without,world
'''
