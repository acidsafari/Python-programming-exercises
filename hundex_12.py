'''
Question: Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: In case of input data being supplied to the question,
it should be assumed to be a console input.
'''

ix = input('Input lower limit number >:')
if len(ix) < 1 :
    ix = 0

iy = input('Input upper limit number >:')
if len(iy) < 1 :
    iy = 3000
    ix = 1000

try:
    x=int(ix)
    y=int(iy)
except:
    print('please enter correct values')

r = range(x, y + 1)
values = []
for number in r :
    s = str(number)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)

    
print(",".join(values))
