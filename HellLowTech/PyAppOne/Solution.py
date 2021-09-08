from Problems import *

while True:

    problemHolder.PrintAll()

    problemNum = int(input("Put in the number of the program you want to run: "))

    for problem in listOfProblems:
        if problem.num == problemNum:
            problem.func()

    while True:
        play_again = input("Start over? (yes/no): ")
        if play_again.lower() != "yes" and play_again.lower() != "y" and play_again.lower() != "1" and play_again.lower() != "+":
            if play_again.lower() == "no" or play_again.lower() == "n" or play_again.lower() == "0" or play_again.lower() == "-":
                print("Ok. Come back later")
                break

            else:
                    print("I don't think i get that. Please repeat")
        else:
            break
    if play_again.lower() == "no" or play_again.lower() == "n" or play_again.lower() == "0" or play_again.lower() == "-":
        break
