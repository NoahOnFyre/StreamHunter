#!/usr/bin/python
# Encoding=utf-8
# Autor github.com/Eltotiz

import os
from colorama import Fore, init
import requests
import time
import random
import string

init(convert=True)


def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")


clear()
print()
print("""                                                       
     _____ _                     _____         _           
    |   __| |_ ___ ___ ___ _____|  |  |_ _ ___| |_ ___ ___ 
    |__   |  _|  _| -_| .'|     |     | | |   |  _| -_|  _|
    |_____|_| |_| |___|__,|_|_|_|__|__|___|_|_|_| |___|_|  

                Erstellt von github.com/Eltotiz
              Übersetzt von github.com/NoahOnFyre
                """)
input(" [+] Drücke Enter um zu beginnen!")
print()
print(" [+] Suche Videos...")
print()
print()

while True:
    text = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    minus = text.lower()
    time.sleep(1)
    src = requests.get(f"https://streamable.com/{minus}")
    try:
        if src.status_code != 404:
            print(Fore.GREEN + f" [+] https://streamable.com/{minus} - Gültiger Link")
                
    except Exception as e:
        print()
        print(" [?] Ein Fehler ist bei dem Verbindungsaufbau zu streamable.com aufgetreten.")
        print(f" [?] Fehlerbeschreibung: {e}")
        input(" [?] Drücke Enter zum verlassen.")
