import random
import time as t
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Willkommen zu SSP! Bist du bereit, gegen ElloGPT anzutreten???!!!")

spielzüge = {"schere": "✂️","stein": "🪨","papier": "📃"}
erlaubte_spielzüge = list(spielzüge.keys())
spielerpunkte = 0
ellogpt_punkte = 0

while True:
    t.sleep(3)
    clear()
    print("")
    print(f"""!Spielstand!
------------------  
Du: {spielerpunkte}
ElloGPT: {ellogpt_punkte}
------------------
""")
    spielzug = input("Schere, Stein oder Papier? ").lower()

    if spielzug == "beenden":
        print("Danke fürs Spielen!")
        t.sleep(2)
        break
    elif spielzug not in erlaubte_spielzüge:
        print("Spielzug nicht erkannt..")
        t.sleep(1.5)
        continue

    ellogpt = random.choice(erlaubte_spielzüge)

    print("--------------")
    print(f"Spieler: {spielzüge[spielzug]}")
    print(f"ElloGPT: {spielzüge[ellogpt]}")
    print("")

    if spielzug == ellogpt:
        print("Es ist ein Unentschieden!")
    elif spielzug == "stein" and ellogpt == "schere":
        spielerpunkte += 1
        print("Du gewinnst!")
    elif spielzug == "papier" and ellogpt == "stein":
        spielerpunkte += 1
        print("Du gewinnst!")
    elif spielzug == "schere" and ellogpt == "papier":
        spielerpunkte += 1
        print("Du gewinnst!")
    else:
        ellogpt_punkte += 1
        print("ElloGPT hat gewonnen!")
    