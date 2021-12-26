import random
print("Roll the dice thrice. If you get a total greater than 10, you win.")
numberofrolls = 0
sumofrolls = 0
while numberofrolls != 3:
 input("Press Enter to roll ")
 r = random.randint(1,6)
 print("You rolled a ", r)
 sumofrolls = sumofrolls + r
 numberofrolls = numberofrolls + 1
 
print("You scored ", sumofrolls)
if sumofrolls > 10:
 print("You won!")
else:
 print("You lost!")


