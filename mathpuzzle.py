import random
play = 'y'
counter = 0
won = 0
lost = 0
def easy():
    x = random.randint(0,10)
    y = random.randint(0,10)
    return x, y
def medium():
    x = random.randint(-15,15)
    y = random.randint(-15,15)
    return x, y
def hard():
    x = random.randint(-25,25)
    y = random.randint(-25,25)
    return x, y
print("\nWelcome to my puzzle!")
choice = [1,2,3]
while play == 'y':
    try:
        print("\nDo you want to play easy, medium or hard?")
        level = int(input("1 = easy, 2 = medium, 3 = hard. Type 1, 2 or 3 and press enter: "))
    except ValueError:
        print("Type 1, 2 or 3 and press enter") 
        continue
    while level not in choice:
            if level > 3:
                print("\nI know you think you are smart, but this game's difficulty doesn't go higher than 'hard', so starting a hard game\n")
                level = 3
    print("\nFind out what x and y are!")
    if level == 1:
        x, y = easy()
    elif level == 2:
        x, y = medium()
    else:
        x, y = hard()
    counter += 1
    a = x + y
    b = x * y
    print("\nx + y = "+ str(a))
    print("\nx * y = "+ str(b))
    e = int(input("\nx = "))
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
print("\nYou've played "+ str(counter) +" games in total. You gave "+ str(won) + " right answer(s) and gave "+ str(lost) +" wrong anwer(s)!")
print("\nThank you for playing! Have a nice day!")

