#Write a program to satisfy the following conditions of the given range: If the number is divisible by 20, it provides an output "twist." If the number is divisible by 15, it will pass (no output) If the number is divisible by 5, it will give an output “fizz.” If the number is divisible by 3, it will give an output "buzz." Otherwise, it will give the output of that number.

a = int(input('Enter a number please: '))

for x in range(a):
    if x%20==0:
        print('twist')
    elif x%15==0:
        pass
    elif x%5==0:
        print('fizz')
    elif x%3==0:
        print('buzz')
    else:
        print(x)