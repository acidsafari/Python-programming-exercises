'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers
as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example: 0100,0011,1010,1001
Then the output should be: 1010
Notes: Assume the data is input by console.

Hints: In case of input data being supplied to the question,
it should be assumed to be a console input.
'''
try:
    seq = input('Input Comma Separated Binary >:')
    if len(seq) < 1 :
        seq = '0100,0011,1010,1001'
except:
    print('please enter correct values')

l = seq.split(',')
l2 = []
for i in l :
    n = int(i)
    if n%5 == 0 :
        s = i
        l2.append(s)

print(l2)
t = ''
for b in l2 :
    if len(t) == 0 :
        t = b
    else :
        tt = t + ',' + b

print(tt)
