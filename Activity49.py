#Write a program to check alphabet “A” is present in the given string or not. And terminate the loop after finding the alphabet “A.”

a = input('Enter a word please:')

for x in a:
    if x == 'A':
        print('The letter A has been found')
        break
    else:
        print('The letter A has not been identified.')