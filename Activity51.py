#Write a program to display 1 to 10 numbers in reverse order and skip the number 5.

num1 = 10
while num1>0:
    num1 = num1-1
    if num1 == 5:
        continue
    print('\n The current value of the value is:',num1)
print('\n Goodbye! See you soon!')