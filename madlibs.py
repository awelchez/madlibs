import platform
import os
import sys

systemplatform = platform.system()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def startMadLibs1():
    print("Please state a name 1: ")
    name1 = str(input("> "))
    print("Please state a name 2: ")
    name2 = str(input("> "))
    print("Please state a movie: ")
    movie1 = str(input("1> "))
    print("Please state adjective 1: ")
    adjective1 = str(input("> "))
    print("Please state adjective 2: ")
    adjective2 = str(input("> "))
    print("Please state adjective 3: ")
    adjective3 = str(input("> "))
    print("Please state adjective 4: ")
    adjective4 = str(input("> "))
    print("Please state adjective 5: ")
    adjective5 = str(input("> "))
    print("Please state adjective 6: ")
    adjective6 = str(input("> "))
    print("Please state verb 1: ")
    verb1 = str(input("> "))
    print("Please state verb 2: ")
    verb2 = str(input("> "))
    print("Please state verb 3: ")
    verb3 = str(input("> "))
    print("Please state a noun: ")
    noun1 = str(input("> "))
    print("Please state a candy: ")
    candy1 = str(input("> "))
    print("Please state a food: ")
    food1 = str(input("> "))
    madlibs1story = f"I went to the movies yesterday with {name1} and {name2}. We saw {movie1}. It was {adjective1}. At one part, I even {verb1} and ran for the {noun1}. During the move we ate {candy1} and {food1}. I got mad because the person sitting behind me kept {verb2} during the movie and wouldn't stop {verb3}. He was asked to leave after he {adjective2} across the theatre. It was pretty {adjective3}. Overall, I liked the movie because it was {adjective4} and the main character was super {adjective5}. Hopefully next time t he people sitting behind me will be more {adjective6}."
    print(madlibs1story)

def startMadLibs2():
    print("Please state a noun: ")
    noun1 = str(input("> "))
    print("Please state an adjective: ")
    adjective1 = str(input("> "))
    print("Please state a number value: ")
    numbervalue1 = str(input("> "))
    print("Please state a body part: ")
    bodypart1 = str(input("> "))
    print("Please state a food: ")
    food1 = str(input("> "))
    print("Please state a verb ending in 'ed': ")
    verbendingined1 = str(input("> "))
    print("Please state an emotion: ")
    emotion1 = str(input("> "))
    print("Please state a person or thing: ")
    personorthing1 = str(input("> "))
    madlibs2story = f"Sat in the office, staring at the {noun1}. He couldn't believe his eyes. There was something so {adjective1} about it. He had been staring out it for {numbervalue1} hours, when he finally snapped out of his trance. His {bodypart1} was growling, he knew he had to find some {food1} soon, or else he would starve. As he {verbendingined1} down the hallway, he suddenly felt {emotion1}. He felt his vision fading, but as he looked down the hall, he saw the attacker. It was {personorthing1}"
    print(madlibs2story)

def showOptions():
    if systemplatform == "Linux":
        os.system("clear")
    elif systemplatform == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    print("Which Mad Libs would you like to do?")
    print("1. A movies Mad Lib")
    print("2. A mystery Mad Lib")
    print("3. Quit")
    choice = str(input("> "))
    if choice == "1":
        startMadLibs1()
    elif choice == "2":
        startMadLibs2()
    elif choice == "3":
        quit()
    else:
        showOptions()

showOptions()
