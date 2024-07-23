def play():
    comp_points=0
    player_points=0
    print('lets play rock , paper, scissors')
    choice=input('type down your choise : ')
    options=['rock','paper','scissors']
    if choice.lower() in options:
        import random
        computer=random.choice(options)
        print('you chose {:^15} and computer chose {:^15}'.format(choice,computer))
        if choice.lower()=='rock':
            if computer.lower()=='paper':
                print('oh ho! , you lost')
                comp_points=comp_points+1
            elif choice.lower()==computer.lower():
            	print('woooops! its a tie')
            else:
            	print('you won')
            	player_points=player_points+1
        if choice.lower()=='paper':
            if computer.lower()=='scissors':
                print('oh ho! , you lost')
                comp_points+=1
            elif computer.lower()=='paper':
                print('woooops! its a tie')
            else:
                print('you won')
                player_points+=1
        if choice.lower()=='scissors':
            if computer.lower()=='rock':
                print('oh ho! , you lost')
                comp_points+=1
            elif choice.lower()==computer.lower():
             	 print('woooops! its a tie')
            else:
             	print('you won')
             	player_points+=1
    else:
        print('check you spelling , get some help from here ', options)
    print('your points are %d and computers points are %d'%(player_points,comp_points))
    again=input('wanna play one more round? just type yes or no : ')
    if again.lower()=='yes':
                play()
    if again.lower()=='no':
        print('game over')
        if player_points>comp_points:
            print(f'DANG! your won the game6 \n your points are {player_points} and \n computers points are {comp_points}')
        elif player_points<comp_points:
            print(f'NGL\nyou are cooked\nyour lost the game\nyour points are {player_points}\nand computers points are {comp_points}\nSHAME ON YOU')
        else:
            print(f'you cant wear a game but the game is tie\nyour points are {player_points}\nand computers points are {comp_points}')
        exit
play()
