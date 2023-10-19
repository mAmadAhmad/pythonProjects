import random
#random module will be used to pick random element from list
rock = ''' _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = ''' _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = '''_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

rock_paper_scissors = [rock, paper, scissors]
computer_choice = (random.choice(rock_paper_scissors))


x = int(input("Type 0 to select rock, 1 for paper and 2 for scissors  "))
if x>2 or x<0:
    print("Invalid choice, you lose")
else:
    if x==0:
        user_choice = rock
    elif x==1:
        user_choice = paper
    elif x==2:
        user_choice = scissors

    print("You choosed: ")
    print(user_choice)
    print("Computer choosed \n",computer_choice)

    if user_choice == computer_choice:
        print("It's a draw")
    elif user_choice == rock and computer_choice == paper:
        print("You lose")
    elif user_choice == scissors and computer_choice == rock:
        print("You lose")
    elif user_choice == paper and computer_choice == scissors:
        print("You lose")
    else:
        print("You Win!")