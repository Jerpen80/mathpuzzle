import random
play = 'y'
counter = 0
won = 0
lost = 0
def getallen():
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    return x, y

print("\nWelcome to my puzzle!\n")
print("Find out what x and y are!")

while play == 'y':
    x, y = getallen()
    counter += 1
    a = x + y
    b = x * y
    print("\nx + y = "+ str(a))
    print("\nx * y = "+ str(b))
    print()
    
    e = int(input("x = "))
    f = int(input("y = "))
    c = e + f
    d = e * f
    if a == c:
        if b == d:
            won += 1
            print("\nWell done!")

        else:
            lost +=1
            print("\nWrong answer.. You can do better than that! Solution: x was "+ str(x) + " and y was "+ str(y))
    else:
        lost +=1
        print("\nWrong answer.. You can do better than that! Solution: x was "+ str(x) + " and y was "+ str(y))   
    play = input("\nWant to try again? Type y and press enter to play again: ")

print("\nYou've played "+ str(counter) +" games in total. You've won "+ str(won) + " game(s) and lost "+ str(lost) +" game(s)!")
print("\nThank you for playing! Have a nice day!")

    


