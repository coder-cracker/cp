# make a number guessing game

import random
winning_number = random.randint(1, 100)
guessing_number = int(input("Enter number to guess"))
count = 0
while guessing_number != winning_number:
    if guessing_number > winning_number:
        print("too high")
    elif guessing_number < winning_number:
        print("too low")
    count += 1
    guessing_number = int(input("Enter again"))
print(f"You win : no. of attempts {count+1}")


