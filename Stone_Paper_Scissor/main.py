import random

li = ["Stone" , "Paper" , "Scissor"]

num = int(input("Enter the number of games do you want to play"))

user_score = 0
computer_score = 0
for i in range(num):
    computer_choice = random.choice(li)
    user_choice = input("Enter your choice in (Stone/Paper/Scissor)")

    if user_choice == "Stone" and computer_choice =="Paper":
        computer_score +=1
        print("Computer Wins this round")
    elif user_choice == "Stone" and computer_choice == "Scissor":
        user_score +=1
        print("User Wins this round")
    elif user_choice == "Paper" and computer_choice == "Scissor":
        computer_score +=1
        print("Computer Wins this round")
    elif user_choice == "Paper" and computer_choice == "Stone":
        user_score+=1
        print("User Wins this round")
    elif user_choice == "Scissor" and computer_choice == "Paper":
        user_score+=1
        print("User Wins this round")
    elif user_choice == "Scissor" and computer_choice == "Stone":
        computer_score +=1
        print("Computer Wins this round")
    else:
        print("This round is draw")

if user_score > computer_score:
    print('User Wins ! Congratulations')
elif user_score < computer_score:
    print('User Wins ! Congratulations')
else:
    print("Match Drawn")