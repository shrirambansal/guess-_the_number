# num = 18
# no. of guesses is 5
# print no. of guesses left
# game over

from nntplib import GroupInfo


print("\t\t***Guess the number***\t")
guesses = 5
print(f"\t***you have only {guesses} Guesses. Play carefully.... ***\t ")
number = 18


for i in range(1,6) :
    guss = int(input("Guess the number : "))
    if guss == number :
        print("Congrates, you win.")
        print(f"Remaining guess : {guesses-i} ")
        break

    elif guss > number :
        print("your guess is big")
        print(f"Remaining guess : {guesses-i} ")
        pass

    else :
        print("your guess is small")
        print(f"Remaining guess : {guesses-i} ")
        pass
    pass

print("you loss")
print(f"Remaining guess : {guesses-i} ")
