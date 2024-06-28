import random

words = ["blender", "houdini", "maya", "unreal", "unity", "painter", "designer"]
chosen_word = random.choice(words)
word_display = [' _ ' for _ in chosen_word]


def play_game():
    print("Welcome to the Hangman! Are you ready to die?")
    print("(1). Yea, for I am already dead.\n(2). No, get me outta here!")
    choice = input("What do you choose? ")
    print("----------------------------------------------------------------")
    if choice == "1":
        print("Loading Nooses, murderers, rapists, thiefs, lunatics...\n")
        print("A crowd begins to gather, they cant wait to see some real justice.")
        print("There's just one thing, you aren't a real criminal.")
        print("No, no. You're the wrong time, wrong place type.")
        print("You may think you're dead, but it's not like that at all.")
        print("Yes, yes. You've got a chance to live.")
        print("All you've gotta do is guess the right words and you can live to see another day.")
        print("But don't get so happy yet.")
        print("If you make 8 wrong guess, YOU'RE TOAST! VAMANOS!!!\n")
        core_game(words)
    elif choice == "2":
        print("You are safe...for now")
    else:
        print("Pardon me, What did you say?")
        play_game()

def core_game(words):
    attemps = 8
    letters_used = ""
    while attemps > 0 and ' _ ' in word_display:
        print("----------------------------------------------------------------")
        print("Letters used: " + letters_used)
        print("\n" + ' '.join(word_display) + "\n")
        guess = input("Enter a letter: ").lower()
        print("----------------------------------------------------------------")
        if guess in chosen_word and guess not in letters_used:
            print("It turns out, your guess was RIGHT!")
            letters_used += guess + ","
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    word_display[index] = guess
            if attemps > 0 and ' _ ' not in word_display:
                print("----------------------------------------------------------------\n")
                print("You WON and live another day, but not for long.")
                print("----------------------------------------------------------------\n")
        elif guess in chosen_word and guess in letters_used:
            print("You already guessed that bruh")
        elif attemps > 1 and ' _ ' not in word_display:
            print("You Won and live another day, but not for long.")
        else:
            attemps -= 1
            letters_used += guess + ","
            if attemps == 7:
                print("_______       ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("============    ")
                print("\nNot up to a good start, Right?")
            elif attemps == 6:
                print("_______       ")
                print(" |    |       ")
                print(" |            ")
                print(" |            ")
                print(" |            ")
                print("============    ")
                print("\nThat's the wrong letter, You wanna be out here all day?")
            elif attemps == 5:
                print("_______       ")
                print(" |    |       ")
                print(" |    O       ")
                print(" |            ")
                print(" |            ")
                print("============    ")
                print("\nyou have a pretty neck!")
            elif attemps == 4:
                print("_______       ")
                print(" |    |       ")
                print(" |    O       ")
                print(" |   /        ")
                print(" |            ")
                print("============    ")
                print("\nTry Again.")
            elif attemps == 3:
                print("_______       ")
                print(" |    |       ")
                print(" |    O       ")
                print(" |   /|       ")
                print(" |            ")
                print("============    ")
                print("\nThings aren't looking so good, that guess was WRONG!")
            elif attemps == 2:
                print("_______       ")
                print(" |    |       ")
                print(" |    O       ")
                print(" |   /|\\     ")
                print(" |            ")
                print("============   ")
                print("\nWrong Guess Idiot!")
            elif attemps == 1:
                print("_______       ")
                print(" |    |       ")
                print(" |    O       ")
                print(" |   /|\\     ")
                print(" |   /        ")
                print("============  ")
                print("\nOh man, that crowd is gettin happy, I thought you wanted to make them mad?")
            else:
                print("_______       ")
                print(" |    |       ")
                print(" |    O       ")
                print(" |   /|\\     ")
                print(" |   / \\     ")
                print("============  ")
                print("\nThe noose tightens around your neck, and you feel the sudden urge to watch Boku no Pico.")
                print("Game Over!!!")

play_game()
