import random
def guess(n,k):
    l = [i for i in str(k)]
    j = [i for i in n]
    c = 0
    if l == j:
        print("You got it\n")
        return 1
    else:
        for i in range(3):
            if l[i] == j[i]:
                print("fermi")
                c = 1
            elif j[i] in l[i:]:
                print("pico")
                c = 1
        if c == 0: 
            print("bagels")
def game():
    print("I have thought up a number. You have 10 guesses to get it.\n")
    k = random.randint(100,999)
    for i in range(10):
        a = guess(input("Enter the guess - "),k)
        if i == 9:
            print("\nYou ran out of guesses")
            print("The answer was : ",k)
        if a:
            return
    
        
print("""I am thinking of a 3-digit number. Try to guess, here are some clues: 
When I say:     That means:
Pico            One digit is correct but in the wrong position. 
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.\n""")
while(1):
    game()
    print("Do you want to play again - (yes/no)")
    c = input()
    if not c.lower() == "yes":
        print("Thanks for playing!")
        break