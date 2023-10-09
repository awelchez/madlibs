import platform
import os

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def start_mad_libs_1():
    name1 = input("Please state a name 1> ")
    name2 = input("Please state a name 2> ")
    movie1 = input("Please state a movie> ")
    adjectives = [input(f"Please state adjective {i}> ") for i in range(1, 7)]
    verbs = [input(f"Please state verb {i}> ") for i in range(1, 4)]
    noun1 = input("Please state a noun> ")
    candy1 = input("Please state a candy> ")
    food1 = input("Please state a food> ")
    
    madlibs1story = f"I went to the movies yesterday with {name1} and {name2}. We saw {movie1}. It was {adjectives[0]}. At one point, I even {verbs[0]} and ran for the {noun1}. During the movie, we ate {candy1} and {food1}. I got mad because the person sitting behind me kept {verbs[1]} during the movie and wouldn't stop {verbs[2]}. He was asked to leave after he {adjectives[1]} across the theatre. It was pretty {adjectives[2]}. Overall, I liked the movie because it was {adjectives[3]} and the main character was super {adjectives[4]}. Hopefully next time the people sitting behind me will be more {adjectives[5]}."
    print(madlibs1story)

def start_mad_libs_2():
    noun1 = input("Please state a noun> ")
    adjective1 = input("Please state an adjective> ")
    numbervalue1 = input("Please state a number value> ")
    bodypart1 = input("Please state a body part> ")
    food1 = input("Please state a food> ")
    verbendingined1 = input("Please state a verb ending in 'ed'> ")
    emotion1 = input("Please state an emotion> ")
    personorthing1 = input("Please state a person or thing> ")
    
    madlibs2story = f"Sat in the office, staring at the {noun1}. He couldn't believe his eyes. There was something so {adjective1} about it. He had been staring at it for {numbervalue1} hours when he finally snapped out of his trance. His {bodypart1} was growling; he knew he had to find some {food1} soon, or else he would starve. As he {verbendingined1} down the hallway, he suddenly felt {emotion1}. He felt his vision fading, but as he looked down the hall, he saw the attacker. It was {personorthing1}."
    print(madlibs2story)

def show_options():
    clear_screen()
    print("Which Mad Libs would you like to do?")
    print("1. A movies Mad Lib")
    print("2. A mystery Mad Lib")
    print("3. Quit")
    choice = input("> ")
    if choice == "1":
        start_mad_libs_1()
    elif choice == "2":
        start_mad_libs_2()
    elif choice == "3":
        quit()
    else:
        show_options()

show_options()
