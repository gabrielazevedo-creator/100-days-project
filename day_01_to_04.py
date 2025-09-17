# rock paper scissors

rock = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

while True:
    r_p_s = [rock, paper, scissors]
    player_choice = input('Choose one: 1- rock, 2- paper, 3- scissors\n').strip()
    computer_choice = random.randint(0,2)
    print('Jo')
    time.sleep(0.5)
    print('Ken')
    time.sleep(0.5)
    print('Po')
    time.sleep(0.5)
    if player_choice == '1':
        if computer_choice == 0:
            print(f"You choose:\n{rock}\nComputer chooses:\n{rock}\nIt's a draw.")
        elif computer_choice == 1:
            print(f"You choose:\n{rock}\nComputer chooses:\n{paper}\nComputer wins! ")
        else:
            print(f"You choose:\n{rock}\nComputer chooses:\n{scissors}\nYou win! ")
    elif player_choice == '2':
        if computer_choice == 0:
            print(f"You choose:\n{paper}\nComputer chooses:\n{rock}\nYou win!")
        elif computer_choice == 1:
            print(f"You choose:\n{paper}\nComputer chooses:\n{paper}\nIt's a draw. ")
        else:
            print(f"You choose:\n{paper}\nComputer chooses:\n{scissors}\nComputer wins! ")
    elif player_choice == '3':
        if computer_choice == 0:
            print(f"You choose:\n{scissors}\nComputer chooses:\n{rock}\nComputer wins!")
        elif computer_choice == 1:
            print(f"You choose:\n{scissors}\nComputer chooses:\n{paper}\nYou win! ")
        else:
            print(f"You choose:\n{scissors}\nComputer chooses:\n{scissors}\nIt's a draw. ")

    else:
        print('Wrong choice, try again!')

        continue
