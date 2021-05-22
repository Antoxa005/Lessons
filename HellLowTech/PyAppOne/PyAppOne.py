import math
import pygame
import random
import tkinter
import time
import sys
import re
import string
import numpy as np

while True:
    print("1. Quadratic Equation Solver")
    print("2. Text Writer")
    print("3. Intercept Finder (For lines)")
    print("4. Intercept Finder (For parabolas)")
    print("5. Anton Quiz")
    print("6. Dice Roller")
    print("7. Password Maker")
    print("8. Video Game")
    print("9. Rock Paper Scissers")
    print("10. Subtracting Squares")
    print("11. Calculator")
    print("12. Hangman")
    print("13. Magic 8 Ball")
    print("14. Odd or Even")
    print("15. Fake ID generator")
    print("16. Number Guessing Game")
    print("17. Square")
    print("18. Pythagorean Theorem")
    print("19. ")
    listofall = input("Put in the number of the program you want to run: ")
    if listofall == "1":
        print("Hello. Anna speaking. I am a bot that solves quadratic equations for you. All you have to do is input 3 numbers (a, b, and c) and I will find the answers for you.")
        a = int(input("A = "))
        b = int(input("B = "))
        c = int(input("C = "))
        B = b ** 2
        forAC = 4 * a * c
        A = 2 * a
        d = B - forAC
        if d < 0:
            print("D =", d, "< 0 => No solution exists")

        q = math.sqrt(d)
        x1 = (-b + q) / (A)
        x2 = (-b - q) / (A)
        if d > 0:
            if x1 == int(x1):
                if x2 == int(x2):
                    print("D =", B, "-", forAC, "=", d, "=> x1 = (", -b, "+", q, ")", "/", A, "=", int(x1), "=> x2 =(", -b, "+", q, ")", "/", A, "=", int(x2))
                else:
                    print("D =", B, "-", forAC, "=", d, "=> x1 = (", -b, "+", q, ")", "/", A, "=", int(x1), "=> x2 =(", -b, "+", q, ")", "/", A, "=", x2)
            else:
                if x2 == int(x2):
                    print("D =", B, "-", forAC, "=", d, "=> x1 = (", -b, "+", q, ")", "/", A, "=", x1, "=> x2 =(", -b, "+", q, ")", "/", A, "=", int(x2))
                else:
                    print("D =", B, "-", forAC, "=", d, "=> x1 = (", -b, "+", q, ")", "/", A, "=", x1, "=> x2 =(", -b, "+", q, ")", "/", A, "=", x2)
        else:
            if x1 == int(x1):
                print("D =", B, "-", forAC, "=", d, "=> x1 = (", -b, "+", q, ")", "/", A, "=", int(x1))
            else:
                print("D =", B, "-", forAC, "=", d, "=> x1 = (", -b, "+", q, ")", "/", A, "=", x1)
    elif listofall == "2":
        print("Hello. George here. I am a bot that writes a text when given 7 parameters. 3 nouns, 1 plural noun, 1 adjective, 1 place, and 1 number and you've got yourself a perfect text.")
        loop = 1
        while (loop < 2):
            noun = input("Choose a noun: ")
            p_noun = input("Choose a plural noun: ")
            number = int(input("Choose a number: "))
            noun2 = input("Choose a noun: ")
            place = input("Name a place (Don't pu (MY) before the place): ")
            adjective = input("Choose an adjective (Describing word): ")
            noun3 = input("Choose a noun: ")
            print ("------------------------------------------")
            print ("Be devoted to your",noun,"How many", p_noun, "do you have?")
            print ("Let me guess it's", number, "Ok, ok now tell me do you love your", noun2,",")
            print ("Please don't break my",p_noun,"in my",place)
            print ("Where the weather is always",adjective,".")
            print ()
            print ("You may think that is this the",noun3,",")
            print ("Well it is.")
            print ("------------------------------------------")
            loop += 1
    elif listofall == "3":
        k1 = int(input("Choose coefficient for the first line "))
        b1 = int(input("Choose intercept for the first line "))
        k2 = int(input("Choose coefficient for the second line "))
        b2 = int(input("Choose intercept for the second line "))
        if k1 == k2:
            if b1 == b2:
                print("They are the same line")
            else:
                print("They are parallel")
        x = (b2 - b1) / (k1 - k2)
        y = k1 * x + b1
        x = int((b2 - b1) / (k1 - k2))
        y = int(k1 * x + b1)
        if k1 > k2:
            print("Their intercept is", x, y)
        else:
            print("Their intercept is", x, y)
    elif listofall == "4":
        k11 = int(input("Choose coefficient for the first line "))
        k12 = int(input("Choose another coefficient for the first line "))
        b1 = int(input("Choose intercept for the first line "))
        k21 = int(input("Choose coefficient for the second line "))
        k22 = int(input("Choose another coefficient for the second line "))
        b2 = int(input("Choose intercept for the second line "))
        a = k11 - k21
        b = k12 - k22
        c = b1- b2
        d = b ** 2 - 4 * a * c
        if d < 0:
            print("d < 0 => no solution")
        if a == 0:
            if b == 0:
                if c == 0:
                    print("They are the same graph")
                else:
                    print("They are parallel")
            else:
                x1 = (-c) / b
                y1 = k11 * x1 + b1
                x1 = int((-c) / b)
                y1 = int(k11 * x1 + b1)
                print("Their intercept is", x1, ",", y1)
        else:
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            x1 = int((-b + math.sqrt(d)) / (2 * a))
            x2 = int((-b - math.sqrt(d)) / (2 * a))
            y1 = k11 * (x1 ** 2) + k21 * x1 + b1
            y2 = k11 * (x2 ** 2) + k21 * x2 + b1
            y1 = int(k11 * (x1 ** 2) + k21 * x1 + b1)
            y2 = int(k11 * (x2 ** 2) + k21 * x2 + b1)
            if x1 == x1:
                print("Their intercepts are", x1, ",", y1, "and", x2, ",", y2)
    elif listofall == "5":
        while True:
            score = 0
            start = input("Would you like to start? Yes/No ")
            Yes = "Cool lets begin"
            correct = "Correct"
            incorrect = "Incorrect"
            if start.lower() == "yes":
                print(Yes)
                start = input("1. What is my name? ")
                if start.lower() == "anton":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("2. What is my favorite color ")
                if start.lower() == "green":
                    score += 1
                    print(correct)
                elif start.lower() == "black":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("3. What is my favorite subject in school? ")
                if start.lower() == "math":
                    score += 1
                    print(correct)
                elif start.lower() == "maths":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("4. What is my favorite sport? ") 
                if start.lower() == "volleyball":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("5. What is my favorite food? ")
                if start.lower() == "pasta":
                    score += 1
                    print(correct)
                elif start.lower() == "chicken curry":
                    score += 1
                    print(correct)
                elif start.lower() == "steak":
                    score += 1
                    print(correct)
                elif start.lower() == "chicken with curry":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("6. What is my date of birth (mm.dd.yyyy)? ")
                if start.lower() == "02.13.2009":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("7. What is my favorite music band? ")
                if start.lower() == "panic at the disco":
                    score += 1
                    print(correct)
                elif start.lower() == "panic! at the disco":
                    score += 1
                    print(correct)
                elif start.lower() == "patd":
                    score += 1
                    print(correct)
                elif start.lower() == "p!atd":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("8. How old was I when I got my first tablet? ")
                if start.lower() == "7":
                    score += 1
                    print(correct)
                elif start.lower() == "7 years old":
                    score += 1
                    print(correct)
                elif start.lower() == "seven":
                    score += 1
                    print(correct)
                elif start.lower() == "seven years old":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("9. What was my first phone called? ")
                if start.lower() == "mi a3":
                    score += 1
                    print(correct)
                elif start.lower() == "xiaomi mi a3":
                    score += 1
                    print(correct)
                elif start.lower() == "xiaomi a3":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
                start = input("10. What are my favorite two numbers (put them as numbers) (the order doesn't matter)? ")
                if start.lower() == "4 8":
                    score += 1
                    print(correct)
                elif start.lower() == "4, 8":
                    score += 1
                    print(correct)
                elif start.lower() == "4 and 8":
                    score += 1
                    print(correct)
                elif start.lower() == "4 & 8":
                    score += 1
                    print(correct)
                elif start.lower() == "8 4":
                    score += 1
                    print(correct)
                elif start.lower() == "8, 4":
                    score += 1
                    print(correct)
                elif start.lower() == "8 and 4":
                    score += 1
                    print(correct)
                elif start.lower() == "8 & 4":
                    score += 1
                    print(correct)
                else:
                    print(incorrect)
            elif start.lower() == "no":
                print("Ok. Come back when ever you want")
            print("Thank you for playing, you got", score, "questions correct")
            mark = (score / 10) * 100
            print("Mark:", str(mark), "%")
            play_again = input("Play again? (yes/no): ")
            if play_again.lower() != "yes":
                break
    elif listofall == "6":
        while True:
            q = input("Would you like to roll the dice? (yes/no) ")
            a = random.randint(1, 6)
            if q.lower() == "yes":
                print("You rolled a", a)
            else:
                break
    elif listofall == "7":
        chars = "abcdefghijklmnopqrstuvwxyz123456789012345678901234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        number = int(input("Number of passwords? - "))
        length = int(input("Password length? - "))
        for p in range(number):
            password = ""
            for c in range(length):
                password += random.choice(chars)
            print(password)
    elif listofall == "8":
        while True:
            def odd(n): 
                return n & 1 

            def color(a): 
                return 'green' if odd(a) else 'blue' 

            class Map: 

                def __init__(self, master, rows = 15, columns = 15): 
                    self.master = master 
                    self.row = random.randrange(rows) 
                    self.col = random.randrange(columns) 
                    self.cost = 0 
                    self.found = False 
                    Button = tkinter.Button 
                    self.buttons = [] 
                    options = dict(text = '??', font = 'Courier 14') 
                    for r in range(rows): 
                        br = []                 # row of buttons 
                        self.buttons.append(br) 
                        for c in range(columns): 
                            b = Button( 
                                master, 
                                command = lambda r=r, c=c: self(r, c), 
                                fg = color(r+c), 
                                **options 
                                ) 
                            b.grid(row = r, column = c) 
                            br.append(b) 
                    master.mainloop() 

                def __bool__(self): 
                    return self.found 

                def __call__(self, row, col): 
                    if self: 
                        self.master.quit() 
                    distance = int(round(math.hypot(row-self.row, col-self.col))) 
                    self.buttons[row][col].configure(text = '{}'.format(distance), bg = 'yellow', fg = 'red') 
                    self.cost += 1 
                    if not distance: 
                        print('You win!  At the cost of {} sonar devices.'.format(self.cost)) 
                        self.found = True 

            def main(): 
                root = tkinter.Tk() 
                map = Map(root) 
                root.destroy() 

            if __name__ == '__main__': 
                main() 
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
    elif listofall == "9":
        while True:
            playerchoice = input("Choose rock paper or scissers ")
            compoptions = ["rock", "paper", "scissers"]
            compchoice = random.choice(compoptions)
            if compchoice == "rock":
                if playerchoice == "rock":
                    print("Its a tie")
                elif playerchoice == "paper":
                    print("You won")
                else:
                    print("You lost")
            elif compchoice == "paper":
                if playerchoice == "rock":
                    print("You lost")
                elif playerchoice == "paper":
                    print("Its a tie")
                else:
                    print("You won")
            else:
                if playerchoice == "rock":
                    print("You won")
                elif playerchoice == "paper":
                    print("You lost")
                else:
                    print("Its a tie")
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break
    elif listofall == "10":
        n = int(input("Choose a number "))
        if n % 4 == 0:
            k = int(n / 4)
            x = int(k + 1)
            y = int(k - 1)
            print("This number can be expressed through the difference of squares of", x, "and", y)
        elif n % 2 == 1:
            k = int((n - 1) / 2)
            x = int(k + 1)
            y = int(k)
            print("This number can be expressed through the difference of squares of", x, "and", y)
        else:
            print("This number can't be expressed through the difference of squares")
    elif listofall == "11":
        a = int(input("Do you want to input 1 or 2 numbers? "))
        if a == 2:
            x = int(input("Input a number "))
            y = int(input("Input a number "))
            operation = input("What operation do you want to do? (-, +, *, /) ")
            if operation == "-":
                a = x - y
                print(x, "-", y, "=", a)
            elif operation == "+":
                a = x + y
                print(x, "+", y, "=", a)
            elif operation == "*":
                a = x * y
                print(x, "*", y, "=", a)
            elif operation == "/":
                a = x / y
                print(x, "/", y, "=", a)
            else:
                print("Not valid")
        elif a == 1:
            x = int(input("Input a number "))
            operation = input("What operation do you want to do? (sqrt, *pi, *e, ^2, factorial) ")
            if operation == "sqrt":
                if x < 0:
                    print("Invalid input")
                else:
                    sqrt = math.sqrt(x)
                    if sqrt == int(sqrt):
                        print("The square root of", x, "=", int(sqrt))
                    else:
                        print("The square root of", x, "=", sqrt)
            elif operation == "*pi":
                pi = x * math.pi
                print(x, "*", math.pi, "=", pi)
            elif operation == "*e":
                e = x * math.e
                print(x, "*", math.e, "=", e)
            elif operation == "^2":
                xSquared = x ** 2
                print(x, "^", 2, "=", xSquared)
            elif operation == "factorial":
                xFactorial = math.factorial(x)
                print(x, "!", "=", xFactorial)
        else:
            print("Not an option")
    elif listofall == "12":
        name = input("What is your name? ")
        print("Hello, " + name, "Time to play hangman!")
        time.sleep(1)
        print("You may now guess")
        words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
        word = random.choice(words)
        guesses = ""
        turns = 10
        while turns > 0:
            failed = 0
            for char in word:
                if char in guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1
            if failed == 0:
                print("You won. The word was", word)
                break
            guess = input("guess a character:") 
            guesses += guess 
            if guess not in word:
                turns -= 1
                print("Wrong")
                print("You have", turns, "more guesses")
                if turns == 0:
                    print("You lose. The word was", word)
    elif listofall == "13":
        question = input("Ask a random yes or no question ")
        L = ["It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        choice = random.choice(L)
        print(choice)
    elif listofall == "14":
        while True:
            x = int(input("Input a number "))
            if x % 2 == 0:
                print("Your number is even")
            elif x % 2 == 1:
                print("Your number is odd")
            else:
                print("Thats not a whole number")
            startover = input("Start over? (yes/no) ")
            if startover != "yes":
                print("Ok. Come back later")
                break
    elif listofall == "15":
        names = ["Liam", "Noah", "Oliver", "William", "Elijah", "James", "Benjamin", "Lucas", "Olivia", "Emma", "Eva", "Charlotte", "Sophia", "Amelia", "Isabella", "Mia"]
        surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        streets = ["first Ave", "second Ave", "third Ave", "fourth Ave", "fifth Ave", "Main Street", "Park Street"]
        cities = ["NY", "Beijing", "Moscow", "Toronto", "Nice", "Berlin", "Cairo", "Stockholm"]
        number = random.randint(0, 81)
        year = 1940 + number
        month = random.choice(months)
        name = random.choice(names)
        surname = random.choice(surnames)
        street = random.choice(streets)
        house = random.randint(1, 200)
        city = random.choice(cities)
        if month == "feb":
            date = random.randint(1, 28)
        else:
            date = random.randint(1, 30)
        print("- Name:", name, surname)
        print("- Date of birth:", month, date, ",", year)
        print("- Address:", house, street, city)
    elif listofall == "16":
        attempts = 0
        number = random.randint(1, 99)
        while attempts > -1:
            attempt = int(input("Enter a number from 1 to 99 "))
            attempts += 1
            print("This is your", attempts, "guess")
            if attempt < number:
                print("Your guess is too low")
            elif attempt > number:
                print("Your guess is too high")
            else:
                print("Great you guessed the number. It was", number)
                break
        if attempts == number:
            print("You guessed in ", attempts, "attempts")
        if attempt != number:
            print("The secret number was", number)
    elif listofall == "17":
        n = int(input("Input length "))
        m = int(input("Input height "))
        k = int(input("Input number of bricks "))
        d = 4 * (m + n) * (m + n) - 16 * k
        w = int(((2 * (m + n)) - (math.sqrt(d))) / 8)
        print(w)
    elif listofall == "18":
        a = int(input("Input the length of the first leg "))
        b = int(input("Input the length of the second leg "))
        c = math.sqrt(a ** 2 + b ** 2)
        if c == int(c):
            print("The hypotenuse is equal to", int(c))
        else:
            print("The hypotenuse is equal to the square root of", a ** 2 + b ** 2)
        answer = input("Do you want to see the approximate answer? (yes/no): ")
        if answer == "yes":
            print("The hypotenuse is equal to", c)
    elif listofall == "19":
        pass
    else:
        print("Thats not valid")
    play_again = input("Start over? (yes/no): ")
    if play_again.lower() != "yes":
        if play_again.lower() == "no":
            print("Ok. Come back later")
            break
        else:
            print("I will count that as a NO")
            break
