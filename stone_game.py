from random import randint
# How computer decides what to take 
def botake():
    if total_stones == 1:
        return 1
    if total_stones % 4 == 1:
        return randint (1, 3)
    else:
        return (total_stones - 1) % 4
        
# The actual game
z = "You"
print ("There are a total of 22 stones we can each take. (1-3) stones every time. Last one to take a stone loses!")

total_stones = 22

while total_stones > 0:
    stones_taken = int(input("Amount of stone(s) to take: "))
    while stones_taken > 3 or stones_taken < 1 or total_stones < stones_taken:
        stones_taken =int(input("invalid entry. Try again: "))
    total_stones = total_stones - stones_taken
    if total_stones == 0:
        z = "Computer"
        break
    take = botake()
    total_stones = total_stones - take
    print ("The bot took " + str(take) + " stones, there are " + str(total_stones) + " left.")
    
print (z+ " won!")