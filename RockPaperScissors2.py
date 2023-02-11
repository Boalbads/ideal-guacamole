import random
import time
import winsound

time.sleep(0.5)
print("$$$$$$$\                      $$\  ")     
print("$$  __$$\                     $$ |      ")
print("$$ |  $$ | $$$$$$\   $$$$$$$\ $$ |  $$\ ")
print("$$$$$$$  |$$  __$$\ $$  _____|$$ | $$  |")
print("$$  __$$< $$ /  $$ |$$ /      $$$$$$  / ")
print("$$ |  $$ |$$ |  $$ |$$ |      $$  _$$<  ")
print("$$ |  $$ |\$$$$$$  |\$$$$$$$\ $$ | \$$\ ")
print("\__|  \__| \______/  \_______|\__|  \__|\n")
time.sleep(1)
print("$$$$$$$\                                         ")
print("$$  __$$\                                        ")
print("$$ |  $$ |$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\  ")
print("$$$$$$$  |\____$$\ $$  __$$\ $$  __$$\ $$  __$$\ ")
print("$$  ____/ $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \__|")
print("$$ |     $$  __$$ |$$ |  $$ |$$   ____|$$ |      ")
print("$$ |     \$$$$$$$ |$$$$$$$  |\$$$$$$$\ $$ |      ")
print("\__|      \_______|$$  ____/  \_______|\__|      ")
print("                   $$ |                          ")
print("                   $$ |                          ")
print("                   \__|                          \n")
time.sleep(1)
print(" $$$$$$\            $$\                                                   $$\ ")
print("$$  __$$\           \__|                                                  $$ |")
print("$$ /  \__| $$$$$$$\ $$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$\ $$ |")
print("\$$$$$$\  $$  _____|$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$ |")
print(" \____$$\ $$ /      $$ |\$$$$$$\  \$$$$$$\  $$ /  $$ |$$ |  \__|\$$$$$$\  \__|")
print("$$\   $$ |$$ |      $$ | \____$$\  \____$$\ $$ |  $$ |$$ |       \____$$\     ")
print("\$$$$$$  |\$$$$$$$\ $$ |$$$$$$$  |$$$$$$$  |\$$$$$$  |$$ |      $$$$$$$  |$$\ ")
print(" \______/  \_______|\__|\_______/ \_______/  \______/ \__|      \_______/ \__|\n")
print("By Boa!\n")
time.sleep(1)
winsound.Beep(2000, 250)
input("Press enter to play!\n")

computer = random.randint(1,3)
print("The computer has chosen.\n")

print("1 - Rock\n2 - Paper\n3 - Scissors\n")

userinput = int(input("What is your choice?\n"))

def win():
    
    print("You win!")
    winsound.Beep(2500, 500)
    winsound.Beep(3000, 500)
    winsound.Beep(3500, 500)
    winsound.Beep(2500, 500)

def lose(user,comp):
    whydidyoulose_question = ""
    if comp == 1 and user == 3:
        whydidyoulose_question = "(Rock vs Scissors)"
    elif comp == 2 and user == 1:
        whydidyoulose_question = "(Paper vs Rock)"
    elif comp == 3 and user == 2:
        whydidyoulose_question = "(Scissors vs Paper)"
    elif comp == 0 and user == 0:
        whydidyoulose_question = "I'm sorry dave, I cannot do that for you."
    print("You lose, computer wins, good luck next time "+whydidyoulose_question)
    
    winsound.Beep(3000, 500)
    winsound.Beep(2500, 500)
    winsound.Beep(2000, 500)
    winsound.Beep(1500, 750)
    winsound.Beep(1250, 1000)

def tie():

    print("Tie.")
    winsound.Beep(2000, 500)

time.sleep(0.5)
print("Rock")
time.sleep(0.5)
print("    Paper")
time.sleep(0.5)
print("         Scissors")
time.sleep(0.5)
print("                 Shoot!")
winsound.Beep(2000, 250)

if userinput >= 4:
    exit("Invalid Character")
elif userinput <= -1:
    exit("Invalid Character")

if computer == userinput:
    tie()
elif computer == 1 and userinput == 3:
    lose(3,1)
elif computer == 2 and userinput == 1:
    lose(1,2)
elif computer == 3 and userinput == 2:
    lose(2,3)
elif userinput == 0:
    print("haxxor - i test code with this")
    winlosetie = int(input("W/L/T"))
    if winlosetie == 1:
        win()
    elif winlosetie == 3:
        tie()
    else:
        lose(0,0)
else:
    win()