import base64
import os
def clear_terminal():
       os.system('cls'if os.name == 'nt' else 'clear')
clear_terminal()
print("                           /$$    /$$                                     /$$")
print("                          /$$/   | $$                                    | $$")
print("  /$$$$$$  /$$$$$$$      /$$//$$$$$$$  /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$$")
print(" /$$__  $$| $$__  $$    /$$//$$__  $$ /$$__  $$ /$$_____/ /$$__  $$ /$$__  $$")
print("| $$$$$$$$| $$  \ $$   /$$/| $$  | $$| $$$$$$$$| $$      | $$  \ $$| $$  | $$")
print("| $$_____/| $$  | $$  /$$/ | $$  | $$| $$_____/| $$      | $$  | $$| $$  | $$")
print("|  $$$$$$$| $$  | $$ /$$/  |  $$$$$$$|  $$$$$$$|  $$$$$$$|  $$$$$$/|  $$$$$$$")
print(" \_______/|__/  |__/|__/    \_______/ \_______/ \_______/ \______/  \_______/")
print("welcome to my base64 encoder/decoder")
while True:
        choice = input("encode, decode or quit e/d/q: ").strip().lower()
        if choice == "e": 
                text = input("what u wanna encode: ")
                try:
                        times = int(input("how many times? "))
                        for i in range(times):
                                text = base64.b64encode(text.encode()).decode()
                        print (text)
                except ValueError:
                        print("wrong number")

        elif choice == "d":
                text = input("what do you want to decode: ")
                try:
                        times = int(input("How many times? "))
                        for i in range(times):
                                text = base64.b64decode(text.encode()).decode()
                        print (text)
                except ValueError:
                      print("wrong number")
            
        elif choice == "q":
                break

        else: 
            print("wrong dumbass")
