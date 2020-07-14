# Game Rules
# At a time, only one thing can do : Sanke/Water/Gun
# If first person did Snake and Second person did Water,first person -Sanke will be winner
# If first person did Gun and second person did water,second person - water will be winner
# If First person did snake and second person did Gun,Second person - Gun will be winner

# write a program using random.choice : choose any varibale Snake,water ,gun but do not print.
# Take input from user
# compare random and input user who will be winner and play for 10 times.

import random
lst=["s","g","w"]

chance=10
no_of_chance=0
computer_points=0
human_points=0

print("\t\t Snake Water Game STARTS \t\t")
print("s for snake \n w for water \n g for gun")

while no_of_chance < chance:
    _input=input('Snake,water,Gun')
    _random=random.choice(lst)

    if(_input==_random):
        print("Tie both 0 point to each\n")
    #if user enter s it will compare with g and w
    elif _input == "s" and _random == "g":
        computer_points=computer_points+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"your point is {human_points} and computer point is {computer_points}")
    elif _input == "s" and _random == "w":
        human_points=human_points+1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you wins 1 point \n")
        print(f"your point is {human_points} and computer point is {computer_points}")
    # if user enter w it will compare with g and s
    elif _input == "w" and _random == "s":
        computer_points = computer_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"your point is {human_points} and computer point is {computer_points}")
    elif _input == "w" and _random == "g":
        human_points = human_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you wins 1 point \n")
        print(f"your point is {human_points} and computer point is {computer_points}")
    # if user enter g  it will compare with s and w
    elif _input == "g" and _random == "w":
        computer_points = computer_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("computer wins 1 point \n")
        print(f"your point is {human_points} and computer point is {computer_points}")
    elif _input == "g" and _random == "s":
        human_points = human_points + 1
        print(f"your guess is {_input} and computer guess is {_random}")
        print("you wins 1 point \n")
        print(f"your point is {human_points} and computer point is {computer_points}")
    else:
        print("you have input wrong")

    no_of_chance = no_of_chance+1
    print(f"{chance-no_of_chance} is left out of {chance}\n")

print("Game Over")

if computer_points==human_points:
    print("Tie")
elif computer_points>human_points:
    print("computer wins and you loose")
else:
    print("you win and computer loose")

print(f"your point is {human_points} and computer points is {computer_points}")


