import random
import os
import time
import winsound
from pygame import mixer

def single_player():
    game = ['Rock', 'Paper', 'Scissors']
    R = "Rock"
    P = "Paper"
    S = "Scissors"
    i = 0
    user_points = 0
    comp_points = 0
    print("Plz! Tell us how much attempt you need: ")
    turns = int(input("Enter: "))
    winsound.Beep(500,1000)
    os.system('cls')
    while(i<turns):
        Comp = random.choice(game)
        print("*********************")
        Input = int(input("Press 1 for Rock\nPress 2 for Paper\nPress 3 for Scissors\n*********************\nEnter: "))
        print("")
        print("Computer choose ",Comp,": and You choose ",Input," ,So:")
        print("")
        if(Input==1):
            if(R==Comp):
                mixer.music.load('failure-drum-sound-effect-2-7184.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Wao! The ",i+1," attemp is draw")
            elif(Comp == P):
                mixer.music.load('negative_beeps-6008.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Ooo!You lose the ",i+1," attempt")
                comp_points = comp_points+1
            elif(Comp == S):
                mixer.music.load('success-1-6297.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Yes!You won the ",i+1," attempt")
                user_points = user_points +1
            i = i + 1
        elif(Input==2):
            if(P==Comp):
                mixer.music.load('failure-drum-sound-effect-2-7184.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Wao! The ",i+1," attemp is draw")
            elif (Comp == R):
                mixer.music.load('success-1-6297.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Yes!You won the ",i+1," attempt")
                user_points = user_points +1
            elif (Comp == S):
                mixer.music.load('negative_beeps-6008.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Ooo!You lose the ",i+1," attempt")
                comp_points = comp_points+1
            i = i + 1
        elif(Input==3):
            if(S==Comp):
                mixer.music.load('failure-drum-sound-effect-2-7184.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Wao! The ",i+1," attemp is draw")
            elif (Comp == R):
                mixer.music.load('negative_beeps-6008.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Ooo!You lose the ",i+1," attempt")
                comp_points = comp_points+1
            elif (Comp == P):
                mixer.music.load('success-1-6297.mp3')
                mixer.music.set_volume(0.2)
                mixer.music.play()
                print("Yes!You won the ",i+1," attempt")
                user_points = user_points +1
            i = i+1
        else:
            print("Invalid Option! Plz Re-enter correct choice")
        time.sleep(2)
        os.system('cls')
    print("Game Points:\nCalculating..... ")
    time.sleep(3)
    print("___________________________________")
    print(f"Total points of User is {user_points}")
    print(f"Total points of Computer is {comp_points}")
    print("___________________________________")
    print("")
    time.sleep(2)
    print("<><><><><><><><><><><><><><><><><><><><>")
    if(user_points > comp_points):
        mixer.music.load('wingrandpiano-96338.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()
        print("Congrats! King You win the game")
    elif(user_points<comp_points):
        mixer.music.load('game_over_sound.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()
        print("Ooops! You lose better luck next time")
    else:
        mixer.music.load('draw_sound2.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()
        print("Game is draw between You and Computer")
    print("<><><><><><><><><><><><><><><><><><><><>")
    time.sleep(6)
def Multi_player():
    us1 = 0
    us2 = 0
    print("!!!!!!!!!!!!!!!!!!!")
    print("Enter user 1 name: ")
    user1 = input()
    winsound.Beep(350,1000)
    print("Enter user 2 name: ")
    user2 = input()
    winsound.Beep(350,1000)
    print("!!!!!!!!!!!!!!!!!!!")
    time.sleep(3)
    os.system('cls')
    time.sleep(1)
    print(f"{user1} and {user2} you both have only 3 attempts: ")
    print("Plz! Wait for your own attempt ")
    time.sleep(3)
    print("----{Game is starting,plz! wait}----")
    time.sleep(2)
    print("Go,Play and Enjoy! Game has been start")
    time.sleep(2)
    os.system('cls')
    i = 0
    while i<3:
        print(f">>>>>>>>>>>>>\nIt is {i+1} attempt\n>>>>>>>>>>>>>")
        print("@@@@@@@@@@@@@@@@@")
        print(f"{user1} Plz select:\n1) for Rock\n2) for Paper\n3) for Scissors\n@@@@@@@@@@@@@@@@@")
        u1 = int(input("Enter: "))
        winsound.Beep(200,700)
        os.system('cls')
        print(f"{user2} Plz select:\n1) for Rock\n2) for Paper\n3) for Scissors\n@@@@@@@@@@@@@@@@@")
        u2 = int(input("Enter: "))
        winsound.Beep(200,700)
        print("")
        if u1==u2:
            print("Wao! it's draw")
            i = i+1
            time.sleep(3)
        elif ((u1 == 1) & (u2 == 2)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user2} won {i+1} attempt ")
            i = i+1
            us2 = us2+1
            time.sleep(3)
        elif ((u1 == 1) & (u2 == 3)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user1} won {i+1} attempt ")
            i = i+1
            us1 = us1 + 1
            time.sleep(3)
        elif ((u1 == 2) & (u2 == 1)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user1} won {i+1} attempt ")
            i = i+1
            us1 = us1 + 1
            time.sleep(3)
        elif ((u1 == 2) & (u2 == 3)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user2} won {i+1} attempt ")
            i = i+1
            us2 = us2+1
            time.sleep(3)
        elif ((u1 == 3) & (u2 == 1)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user2} won {i+1} attempt ")
            i = i+1
            us2 = us2+1
            time.sleep(3)
        elif ((u1 == 3) & (u2 == 2)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user1} won {i+1} attempt ")
            i = i+1
            us1 = us1 + 1
            time.sleep(3)
        elif ((u2 == 1) & (u1 == 2)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user1} won {i+1} attempt ")
            i = i+1
            us1 = us1 + 1
            time.sleep(3)
        elif ((u2 == 1) & (u1 == 3)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user2} won {i+1} attempt ")
            i = i+1
            us2 = us2+1
            time.sleep(3)
        elif ((u2 == 2) & (u1 == 1)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user2} won {i+1} attempt ")
            i = i+1
            us2 = us2+1
            time.sleep(3)
        elif ((u2 == 2) & (u1 == 3)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user1} won {i+1} attempt ")
            i = i+1
            us1 = us1 + 1
            time.sleep(3)
        elif ((u2 == 3) & (u1 == 1)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user1} won {i+1} attempt ")
            i = i+1
            us1 = us1 + 1
            time.sleep(3)
        elif ((u2 == 3) & (u1 == 2)):
            mixer.music.load('success-1-6297.mp3')
            mixer.music.set_volume(0.2)
            mixer.music.play()
            print(f" {user2} won {i+1} attempt ")
            i = i+1
            us2 = us2+1
            time.sleep(3)
        else:
            print("Invalid option! select correct option")
            time.sleep(2)
        os.system('cls')

    print("Game Points:\nCalculating..... ")
    time.sleep(3)
    print("___________________________________")
    print(f"Total points of {user1} is {us1}")
    print(f"Total points of {user2} is {us2}")
    print("___________________________________")
    time.sleep(2.5)
    if(us1 > us2):
        mixer.music.load('wingrandpiano-96338.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print(f"Congrats! Stronger {user1} You win the game")
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
    elif(us1<us2):
        mixer.music.load('wingrandpiano-96338.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
        print(f"Congrats! Stronger {user1} You win the game")
        print("<><><><><><><><><><><><><><><><><><><><><><><>")
    else:
        mixer.music.load('draw_sound2.mp3')
        mixer.music.set_volume(0.3)
        mixer.music.play()
        print("<><><><><><><><><><><><><><><><><><><><><>")
        print(f"Game is draw between {user1} and {user2}")
        print("<><><><><><><><><><><><><><><><><><><><><>")
    time.sleep(6)
mixer.init()
mixer.music.load('game_start2.mp3')
mixer.music.set_volume(0.2)
mixer.music.play()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("Welcome!\'Rock,Paper and Scissors\',Game")
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
time.sleep(2.5)
while True:
    print("__________________________")
    print("Select mode of Game:\nPress 1 for Single Player\nPress 2 for Multi Player\n__________________________")
    mode = int(input("Enter: "))
    winsound.Beep(500,1000)
    if (mode!=1 and mode!=2):
        print("Invalid option! Re-select mode\n")
        continue
    else:
        break
print("Game will start soon! we hope you will enjoy the game!")
time.sleep(2)
if(mode==1):
    single_player()
elif(mode == 2):
    Multi_player()

