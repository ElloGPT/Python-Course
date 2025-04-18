import time as t
import os

def menu():    #just the menu which is displayed after starting the program
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
    \033[38;2;100;0;0m▓█████  ██▓     ██▓     ▒█████    ▄████  ██▓███  ▄▄▄█████▓\033[0m
    \033[38;2;130;0;0m▓█   ▀ ▓██▒    ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██░  ██▒▓  ██▒ ▓▒\033[0m
    \033[38;2;160;20;20m▒███   ▒██░    ▒██░    ▒██░  ██▒▒██░▄▄▄░▓██░ ██▓▒▒ ▓██░ ▒░\033[0m
    \033[38;2;190;50;50m▒▓█  ▄ ▒██░    ▒██░    ▒██   ██░░▓█  ██▓▒██▄█▓▒ ▒░ ▓██▓ ░\033[0m 
    \033[38;2;220;80;80m░▒████▒░██████▒░██████▒░ ████▓▒░░▒▓███▀▒▒██▒ ░  ░  ▒██▒ ░ \033[0m
    \033[38;2;240;120;120m░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ▒▓▒░ ░  ░  ▒ ░░\033[0m   
    \033[38;2;250;180;180m░ ░  ░░ ░ ▒  ░░ ░ ▒  ░  ░ ▒ ▒░   ░   ░ ░▒ ░         ░\033[0m    
    \033[38;2;255;220;220m░     ░ ░     ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░░         ░\033[0m      
    \033[38;2;255;255;255m░  ░    ░  ░    ░  ░    ░ ░        ░\033[0m
    """)
    
    print("\033[38;2;240;120;120m[1]Start game\033[0m")
    print("\033[38;2;240;120;120m[2]How does it work?\033[0m")
    print("\033[38;2;240;120;120m[3]Exit\033[0m")
    print("")
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def mad_libs_abfrage():

    global name, nomen_a, nomen_b, nomen_c, verb_a, verb_b, verb_c, adjektiv_a, adjektiv_b, adjektiv_c, zahl_a, zahl_b, zahl_c

    name = input("Enter a name: ")
    nomen_a = input("Enter a noun: ")
    nomen_b = input("Enter another noun: ")
    nomen_c = input("Enter one last noun: ")
    verb_a = input("Enter a verb: ")
    verb_b = input("Enter another verb: ")
    verb_c = input("Enter one last verb: ")
    adjektiv_a = input("Enter an adjective: ")
    adjektiv_b = input("Enter another adjective: ")
    adjektiv_c = input("Enter one last adjective: ")
    zahl_a = input("Enter a number: ")
    zahl_b = input("Enter another number: ")
    zahl_c = input("Enter one last number: ")

def mad_libs_erklärung():
    print("What is Madlib?")
    t.sleep(2)
    print("")
    print("Mad Libs is a fun word game where you input various types of words like nouns, verbs, adjectives, or numbers.")
    t.sleep(2)
    print("Once you've entered your words, they will be inserted into a pre-written story.")
    t.sleep(2)
    print("This often leads to very funny or absurd results.")
    t.sleep(2)
    print("")
    print("Have fun playing!")
    t.sleep(2)
    print("")
    input("Press Enter to return to the menu ")

def mad_libs():
    clear()
    print(f"""One morning, {name} woke up and heard a strange noise.
At the door stood a {adjektiv_a} {nomen_a}, trying to {verb_a}.
Without hesitation, {name} grabbed a {nomen_b} and started to {verb_b} in circles {zahl_a} times.
Suddenly, a {adjektiv_b} {nomen_c} appeared and shouted: "{zahl_b} {nomen_a}s are coming!"
But {name} wasn't impressed and started to {verb_c} instead.
After a {adjektiv_c} adventure, they drank {zahl_c} liters of lemonade and laughed out loud.
    """)
    print("")
    input("Press Enter to return to the menu ")

while True:
    menu()
    eingabe = int(input("Option: "))

    if eingabe == 1:
        clear()
        mad_libs_abfrage()
        mad_libs()
    elif eingabe == 2:
        clear()
        mad_libs_erklärung()
    elif eingabe == 3:
        print("Exiting program..")
        t.sleep(2)
        break
    else:
        print("Invalid input!")
        t.sleep(2)
        continue

#Originally, this program was intended to be in German. However, due to the complexity of German grammar, the text made very little sense. Therefore, some parts were rewritten in English.