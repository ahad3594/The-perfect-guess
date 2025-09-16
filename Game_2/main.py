import random


n= random.randint(1,100)

a=1
guesses=0

while(a!=n):
    guesses += 1
    a=int(input('Guess the number: '))

    if(a>n):
     
     
    
     

     print(f"Guess the lower number than {a}    ⬇️")

    else:
     
     
    
     print(f"Guess the higher number than {a}   ⬆️ ")



print(f'You guessed the number {n} in {guesses} attempts')





