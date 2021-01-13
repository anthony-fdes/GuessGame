from random import randint

name = input("whats your name ?")

# num = [1, 2, 3, 4, 5]

computer = randint(1, 5)
#print(computer)

player = False
chances = 0

while chances < 4:
    player = int(input("Okay!, Hie " + name + " You would need to guess a number betweeen 1 to 5?"))
    chances += 1

    if player > computer:
        print("The number that you have entered is greater than the expected number")

    if player < computer:
        print("The number that you have entered is less than expected")

    if player == computer:
        print("Both the numbers now match, you win!")
        break

if player == computer:
    print("you guesssed the number in " + str(chances) + " tries")  ##un-commenting this

else:
    print("you did not guess the number, the number was " + str(computer))  ##un-commenting this
