import pygame
import os
import random
import datetime
import math
import numpy as np
import tkinter

class Problem:
    def __init__(self, func, name, num):
        self.func = func
        self.name = name
        self.num = num

class ProblemHolder:
    def __init__(self, listOfProblems):
        self.listOfProblems = listOfProblems

    def PrintAll(self):
        for problem in self.listOfProblems:
            print(str(problem.num) + ".", problem.name)


def RealSqrt(a):
    if a == -1:
        i = "i"
        print(i)
    else:
        realSqrt1 = math.sqrt(a)
        realSqrt2 = -(math.sqrt(a))
        if realSqrt1 == int(realSqrt1):
            if realSqrt2 == int(realSqrt2):
                return int(realSqrt1), int(realSqrt2)
            else:
                return int(realSqrt1), realSqrt2
        elif realSqrt2 == int(realSqrt2):
            return realSqrt1, int(realSqrt2)
        else:
            return realSqrt1, realSqrt2

def NthRoot(a, b):
    return pow(a, (1 / b))

def problem1():
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

    else:
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

def problem2():
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

def problem3():
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

def problem4():
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

def problem5():

        score = 0
        start = input("Would you like to start? Yes/No ")
        Yes = "Cool lets begin"
        correct = "Correct"
        incorrect = "Incorrect"
        if start.lower() == "yes":
            print(Yes)
            q1 = input("1. What is my name? ")
            if q1.lower() == "anton":
                score += 1
                print(correct)
            else:
                print(incorrect)
            q2 = input("2. What is my favorite color ")
            if q2.lower() == "green":
                score += 1
                print(correct)
            elif q2.lower() == "black":
                score += 1
                print(correct)
            else:
                print(incorrect)
            q3 = input("3. What is my favorite subject in school? ")
            if q3.lower() == "math":
                score += 1
                print(correct)
            elif q3.lower() == "maths":
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
        if mark == int(mark):
            print("Mark:", int(mark), "%")
        else:
            print("Mark:", mark, "%")

def problem6():
        while True:
            q = input("Would you like to roll the dice? (yes/no) ")
            a = random.randint(1, 6)
            if q.lower() == "yes":
                print("You rolled a", a)
            else:
                break

def problem7():
        AllChars = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        length = int(input("Password length? - "))
        numOfP = int(input("Number of passwords? - "))
        NOP = 0
        while NOP < numOfP:
            num = 0
            password = []
            realPassword = ""
            while num < length:
                password.append(random.choice(AllChars))
                num += 1
            for e in password:
                realPassword += str(e)
            print(realPassword)
            NOP += 1

def problem8():
        while True:
            def odd(n): 
                return n & 1 

            def color(a): 
                return 'green' if odd(a) else 'blue' 

            class Map: 

                def __init__(self, master, rows = 15, columns = 15): 
                    self.master = master 
                    self.row = random.problemNumrange(rows) 
                    self.col = random.problemNumrange(columns) 
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


            main()
            play_again = input("Play again? (y/n): ")
            if play_again.lower() != "y":
                break

def problem9():

        while True:
            playerchoice = input("Choose rock paper or scissors ")
            compoptions = ["rock", "paper", "scissors"]
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

def problem10():

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

def problem11():

    def Add(a, b):
        return a + b
    def Subtract(a, b):
        return a - b
    def Mult(a, b):
        return a * b
    def Divide(a, b):
        return a / b
    def Mod(a):
        return int(math.sqrt(a ** 2))
    def Factorial(a):
        return math.factorial(a)
    def OneOverA(a):
        return 1 / a
    def Squared(a):
        return a ** 2
    def Power(a, b):
        return a ** b
    def TenPowerA(a):
        return 10 ** a
    def TwoPowerA(a):
        return 2 ** a
    def NaturalLog(a):
        return math.log(a)
    def Log(a, b):
        return math.log(a, b)

    def Op1(c, p):
        if c == 1:
            x = int(input("Input number "))
            y = int(input("Input number "))
            print(x, "+", y, "=", Add(x, y))
            previous = Add(x, y)
        else:
            if prev == 1:
                x = previous
                y = int(input("Input number "))
                print(x, "+", y, "=", Add(x, y))
                previous = Add(x, y)
    def Op2():
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "-", y, "=", Subtract(x, y))

    def Op3():
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "*", y, "=", Mult(x, y))

    def Op4():
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "/", y, "=", Divide(x, y))

    def Op5():
        x = int(input("Input number "))
        print("|" + str(x) + "|", "=", Mod(x))

    def Op6():
        x = int(input("Input number "))
        print(str(x) + "!", "=", Factorial(x))

    def Op7():
        x = int(input("Input number "))
        print(1, "/", x, "=", OneOverA(x))

    def Op8():
        x = int(input("Input number "))
        print(x, "^", 2, "=", Squared(x))

    def Op9():
        x = int(input("Input number "))
        print(x, "^", 3, "=", Power(x, 3))

    def Op10():
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "^", y, "=", Power(x, y))

    def Op11():
        x = int(input("Input number "))
        print(10, "^", x, "=", TenPowerA(x))

    def Op12():
        x = int(input("Input number "))
        print(2, "^", x, "=", TwoPowerA(x))

    def Op13():
        x = int(input("Input number "))
        print("log(" + str(x) + ")", "=", NaturalLog(x))

    def Op14():
        x = int(input("Input number "))
        y = int(input("Input number "))
        print("log(" + str(y) + ")", str(x), "=", Log(x, y))

    def Op15():
        x = int(input("Input number "))
        print("sqrt(" + str(x) + ")", "=", RealSqrt(x))

    def Op16():
        x = int(input("Input number "))
        K = pow(x, (1/3))
        if K == int(K):
            print("(3)rt" + "(" + str(x) + ")", "=", int(K))
        else:
            print("(3)rt" + "(" + str(x) + ")", "=", K)

    def Op17():
        x = int(input("Input number "))
        y = int(input("Input number "))
        K = pow(x, (1/y))
        if K == int(K):
            print("(" + str(y) + ")" + "rt" + "(" + str(x) + ")", "=", int(pow(x, (1/ y))))
        else:
            print("(" + str(y) + ")" + "rt" + "(" + str(x) + ")", "=", pow(x, (1/ y)))

    def Op18():
        x = int(input("Input number "))
        print(x, "* e =", math.e * x)

    def Op19():
        x = int(input("Input number "))
        print(x, "* pi =", math.pi * x)

    def Op20():
        x = int(input("Input number "))
        print("e ^", x, "=", math.e ** x)

    def Op21():
        x = int(input("Input number "))
        print("sin(" + str(x) + ")", "=", math.sin(x))

    def Op22():
        x = int(input("Input number "))
        print("cos(" + str(x) + ") =", math.cos(x))

    def Op23():
        x = int(input("Input number "))
        print("tan(" + str(x) + ") =", math.tan(x))


    print("Clear")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. /")
    print("5. |x|")
    print("6. !")
    print("7. 1/x")
    print("8. x ^ 2")
    print("9. x ^ 3")
    print("10. x ^ y")
    print("11. 10 ^ x")
    print("12. 2 ^ x")
    print("13. ln")
    print("14. Log")
    print("15. sqrt")
    print("16. Cube Root")
    print("17. N-th Root")
    print("18. *e")
    print("19. *pi")
    print("20. e ^ x")
    print("21. Sin")
    print("22. Cos")
    print("23. Tan")
    previous = 0
    clear = input("C? y/n ")
    opperation = int(input("What opperation do you want to do? "))
    if opperation == 1:
        if clear == "y":
            x = int(input("Input number "))
            y = int(input("Input number "))
            print(x, "+", y, "=", Add(x, y))
            previous = Add(x, y)
        else:
            prev = int(input("1, 2?"))
            if prev == 1:
                x = previous
                y = int(input("Input number "))
                print(x, "+", y, "=", Add(x, y))
                previous = Add(x, y)
            else:
                x = int(input("Input number "))
                y = int(input("Input number "))
                print(x, "+", y, "=", Add(x, y))
                previous = Add(x, y)

    elif opperation == 2:
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "-", y, "=", Subtract(x, y))
    elif opperation == 3:
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "*", y, "=", Mult(x, y))
    elif opperation == 4:
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "/", y, "=", Divide(x, y))
    elif opperation == 5:
        x = int(input("Input number "))
        print("|" + str(x) + "|", "=", Mod(x))
    elif opperation == 6:
        x = int(input("Input number "))
        print(str(x) + "!", "=", Factorial(x))
    elif opperation == 7:
        x = int(input("Input number "))
        print(1, "/", x, "=", OneOverA(x))
    elif opperation == 8:
        x = int(input("Input number "))
        print(x, "^", 2, "=", Squared(x))
    elif opperation == 9:
        x = int(input("Input number "))
        print(x, "^", 3, "=", Power(x, 3))
    elif opperation == 10:
        x = int(input("Input number "))
        y = int(input("Input number "))
        print(x, "^", y, "=", Power(x, y))
    elif opperation == 11:
        x = int(input("Input number "))
        print(10, "^", x, "=", TenPowerA(x))
    elif opperation == 12:
        x = int(input("Input number "))
        print(2, "^", x, "=", TwoPowerA(x))
    elif opperation == 13:
        x = int(input("Input number "))
        print("log(" + str(x) + ")", "=", NaturalLog(x))
    elif opperation == 14:
        x = int(input("Input number "))
        y = int(input("Input number "))
        print("log(" + str(y) + ")", str(x), "=", Log(x, y))
    elif opperation == 15:
        x = int(input("Input number "))
        print("sqrt(" + str(x) + ")", "=", RealSqrt(x))
    elif opperation == 16:
        x = int(input("Input number "))
        K = pow(x, (1/3))
        if K == int(K):
            print("(3)rt" + "(" + str(x) + ")", "=", int(K))
        else:
            print("(3)rt" + "(" + str(x) + ")", "=", K)
    elif opperation == 17:
        x = int(input("Input number "))
        y = int(input("Input number "))
        K = pow(x, (1/y))
        if K == int(K):
            print("(" + str(y) + ")" + "rt" + "(" + str(x) + ")", "=", int(pow(x, (1/ y))))
        else:
            print("(" + str(y) + ")" + "rt" + "(" + str(x) + ")", "=", pow(x, (1/ y)))
    elif opperation == 18:
        x = int(input("Input number "))
        print(x, "* e =", math.e * x)
    elif opperation == 19:
        x = int(input("Input number "))
        print(x, "* pi =", math.pi * x)
    elif opperation == 20:
        x = int(input("Input number "))
        print("e ^", x, "=", math.e ** x)
    elif opperation == 21:
        x = int(input("Input number "))
        print("sin(" + str(x) + ")", "=", math.sin(x))
    elif opperation == 22:
        x = int(input("Input number "))
        print("cos(" + str(x) + ") =", math.cos(x))
    elif opperation == 23:
        x = int(input("Input number "))
        print("tan(" + str(x) + ") =", math.tan(x))

    else:
        print("Not Valid")

def problem12():

        name = input("What is your name? ")
        print("Hello, " + name, "Time to play hangman!")
        time.sleep(1)
        print("You may now guess")
        words = open("words.txt")
        lines = words. readlines()
        word = random.choice(lines)
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

def problem13():

        question = input("Ask a random yes or no question ")
        L = ["It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        choice = random.choice(L)
        print(choice)

def problem14():
    print("??? Coming Soon")
    filler = "filler"

def problem15():

        if random.randint(1, 2) == 1:
            names = open("boyNames.txt")
        else:
            names = open("girlNames.txt")
        name = names.readlines()
        surnames = open("surnames.txt")
        surname = surnames.readlines()
        emails = open("emails.txt")
        email = emails.readlines()
        countries = open("Countries.txt")
        country = countries.readlines()
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        streets = ["first Ave", "second Ave", "third Ave", "fourth Ave", "fifth Ave", "Main Street", "Park Street"]
        number = random.randint(0, 81)
        year = 1940 + number
        month = random.choice(months)
        street = random.choice(streets)
        house = random.randint(1, 200)
        if month == "feb":
            date = random.randint(1, 28)
        else:
            date = random.randint(1, 30)
        print("- Name:", random.choice(name))
        print("- Surname:", random.choice(surname))
        print("- Date of birth:", month, date, ",", year)
        print("")
        print("- Email:", random.choice(email))
        print("- Address:", house, street, random.choice(country))

def problem16():

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

def problem17():

        n = int(input("Input length "))
        m = int(input("Input height "))
        k = int(input("Input number of bricks "))
        d = 4 * (m + n) * (m + n) - 16 * k
        w = int(((2 * (m + n)) - (math.sqrt(d))) / 8)
        print(w)

def problem18():

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

def problem19():

        t = int(input("Input the time when you came "))
        a = int(input("Input the time of the 1st swimmer "))
        b = int(input("Input the time of the 2nd swimmer "))
        c = int(input("Input the time of the 3rd swimmer "))
        if int(t / a) > 1 or int(t / b) > 1 or int(t / c) > 1:
            L = [t % a, t % b, t % c]
            print("The nearest swimmer will come in", min(L), "minutes")
        elif int(t / a) == 0 or int(t / b) == 0 or int(t / c) == 0:
            print("The nearest swimmer will come in", min(a, b, c) - t, "minutes")
        elif t == a or t == b or t == c:
            print("The nearest swimmer will come in", 0, "minutes")
        else:
            k = 2 * min(a, b, c) - t
            print("The nearest swimmer will come in", k, "minutes")

def problem20():

        h = int(input("Input the time in zone A (0 - 23) "))
        a = int(input("Input the time difference from UTC+0 (-11 - 12) "))
        b = int(input("Input the time difference from UTC+0 (-11 - 12) "))
        if -11 > a > 12 or -11 > b > 12 or 0 > h > 23:
            print("Not valid")
        else:
            answer = h - a + b
            answerStr = str(answer)
            if answer >= 12:
                print("It's " + str(answer) + "pm in zone B")
            else:
                print("It's " + str(answer) + "am in zone B")

def problem21():

        A = int(input("Input first number "))
        B = int(input("Input second number "))
        def sum_even(a, b):
            return sum(i for i in range(a, b + 1) if i % 2 == 0)
        def sum_odd(a, b):
            return sum(i for i in range(a, b + 1) if i % 2 == 1)
        print("The difference of the sum of all even numbers between them and all odd numbers between them is" ,sum_even(A, B) - sum_odd(A, B))

def problem22():

        a = int(input("Input the first number "))
        b = int(input("Input the second number "))
        if a >= b:
            ans = 1
            while ans % b != b - 1:
                ans += a
        else:
            ans = b - 1
            while ans % a != 1:
                ans += b
        print("The answer is", ans)

def problem23():

        task1 = input("Input task ")
        if task1.lower() == "done":
            print("You have nothing in your list")
        else:
            task2 = input("Input task ")
            if task2.lower() == "done":
                print("Would you like to hear the list?")
                ans = input("yes/no ")
                if ans.lower() == "yes":
                    print(task1)
                    sys.stdout = open("ToDoList.txt", "w")
                    print(task1)
                    sys.stdout.close()
                else:
                    print("ok. Discard")
            else:
                task3 = input("Input task ")
                if task3.lower() == "done":
                    print("Would you like to hear the list?")
                    ans = input("yes/no ")
                    if ans.lower() == "yes":
                        print(task1)
                        print(task2)
                        sys.stdout = open("ToDoList.txt", "w")
                        print(task1)
                        print(task2)
                        sys.stdout.close()
                    else:
                        print("ok. Discard")
                else:
                    task4 = input("Input task ")
                    if task4.lower() == "done":
                        print("Would you like to hear the list?")
                        ans = input("yes/no ")
                        if ans.lower() == "yes":
                            print(task1)
                            print(task2)
                            print(task3)
                            sys.stdout = open("ToDoList.txt", "w")
                            print(task1)
                            print(task2)
                            print(task3)
                            sys.stdout.close()
                        else:
                            print("ok. Discard")
                    else:
                        task5 = input("Input task ")
                        if task5.lower() == "done":
                            print("Would you like to hear the list?")
                            ans = input("yes/no ")
                            if ans.lower() == "yes":
                                print(task1)
                                print(task2)
                                print(task3)
                                print(task4)
                                sys.stdout = open("ToDoList.txt", "w")
                                print(task1)
                                print(task2)
                                print(task3)
                                print(task4)
                                sys.stdout.close()
                            else:
                                print("ok. Discard")
                        else:
                            print("Would you like to hear the list?")
                            ans = input("yes/no ")
                            if ans.lower() == "yes":
                                print(task1)
                                print(task2)
                                print(task3)
                                print(task4)
                                print(task5)
                                sys.stdout = open("ToDoList.txt", "w")
                                print(task1)
                                print(task2)
                                print(task3)
                                print(task4)
                                print(task5)
                            else:
                                print("ok. Discard")

def problem24():

        year = int(input("Input the year "))
        month = int(input("Input the months "))
        day = int(input("Input the day "))
        yearToDays = (int((year - 1) / 4) + 1) * 366 + (year - (int((year - 1)/ 4) + 1)) * 365
        if year % 4 == 0:
            if month == 1:
                monthToDays = 0
            elif month == 2:
                monthToDays = 31
            elif month == 3:
                monthToDays = 31 + 29
            elif month == 4:
                monthToDays = 31 + 29 + 31
            elif month == 5:
                monthToDays = 31 + 29 + 31 + 30
            elif month == 6:
                monthToDays = 31 + 29 + 31 + 30 + 31
            elif month == 7:
                monthToDays = 31 + 29 + 31 + 30 + 31 + 30
            elif month == 8:
                monthToDays = 31 + 29 + 31 + 30 + 31 + 30 + 31
            elif month == 9:
                monthToDays = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31
            elif month == 10:
                monthToDays = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30
            elif month == 11:
                monthToDays = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            elif month == 12:
                monthToDays = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        else:
            if month == 1:
                monthToDays = 0
            elif month == 2:
                monthToDays = 31
            elif month == 3:
                monthToDays = 31 + 28
            elif month == 4:
                monthToDays = 31 + 28 + 31
            elif month == 5:
                monthToDays = 31 + 28 + 31 + 30
            elif month == 6:
                monthToDays = 31 + 28 + 31 + 30 + 31
            elif month == 7:
                monthToDays = 31 + 28 + 31 + 30 + 31 + 30
            elif month == 8:
                monthToDays = 31 + 28 + 31 + 30 + 31 + 30 + 31
            elif month == 9:
                monthToDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
            elif month == 10:
                monthToDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
            elif month == 11:
                monthToDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
            elif month == 12:
                monthToDays = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
        Days = yearToDays + monthToDays + day + 1
        if Days % 7 == 0:
            print("Wednesday")
        elif Days % 7 == 1:
            print("Thursday")
        elif Days % 7 == 2:
            print("Friday")
        elif Days % 7 == 3:
            print("Saturday")
        elif Days % 7 == 4:
            print("Sunday")
        elif Days % 7 == 5:
            print("Monday")
        elif Days % 7 == 6:
            print("Tuesday")

def problem25():
    print("DON'T START IT. IT CAN'T STOP. DON'T DO IT.")
    K = int(input("How old are you? "))
    t = 2523200000 - (K * 365 * 24 * 60 * 60)
    while t > 0:
        time.sleep(1)
        t -= 1
        print(t)

def problem26():
    def calculate(k, n):
        p = int(n / k)
        q = p + 1

        ans = min(q*k-n, abs(p*k-n))
        return ans

    k = np.int64(input())
    n = np.int64(input())
    print(calculate(k, n))

def problem27():
    def calculate(listOfBacteria):
        resultList = []
        listOfBacteria.sort()
        for bacteria in listOfBacteria:
            realList = listOfBacteria.copy()
            bacteriaPower = bacteria
            realList.remove(bacteria)
            for bac in listOfBacteria:
                if bacteriaPower > bac:
                    bacteriaPower += bac
            if bacteriaPower > max(listOfBacteria):
                resultList.append(1)

            else:
                resultList.append(0)

        return resultList

    numOfInputs = int(input())
    bacList = []

    for e in range(numOfInputs):
        Input = int(input())
        bacList.append(Input)

    for ans in calculate(bacList):
        print(ans)

def problem28():
    def calculate(a, b):
        if (a + b) % 3 != 0:
            return [-1]
        difference = a - b
        numOfBoxes = (a + b) / 3
        bBoxes = (numOfBoxes - difference) / 2
        aBoxes = bBoxes + difference

        if aBoxes < 0 or bBoxes < 0 or (aBoxes < 0 and bBoxes < 0):
            return [-1]

        return (aBoxes, bBoxes)

    a = int(input())
    b = int(input())

    for ans in calculate(a, b):
        print(ans)

def problem29():
    class Tower:
        def __init__(self, x, y, n):
            self.x = x
            self.y = y

            self.n = n

        def Rotate90Deg(self):
            newX, newY = self.n - self.y + 1, self.x
            self.x, self.y = newX, newY


    def calculate(listOfTowers):
        listOfTupleTowers = []

        for tower in listOfTowers:
            tower.Rotate90Deg()
            listOfTupleTowers.append((tower.x, tower.y))

        sorted_list = sorted(listOfTupleTowers, key=lambda tow : tow[1])
        for e in sorted_list:
            print(e[0])

    listOfTowers = []

    n = int(input())
    y = 1

    for e in range(n):
        Input = int(input())
        listOfTowers.append(Tower(Input, y, n))
        y += 1

    calculate(listOfTowers)

def problem30():

    def calculate(n):
        num = 0
        listOfNums = []
        while num < 10000:
            num += 1
            squareNum = num * num
            listOfNums.append(squareNum)
        listOfNums.append(n)
        listOfNums.sort()
        index = listOfNums.index(n)
        if listOfNums[index+1] == n:
            if n % 2 == 1:
                return (1, int(math.sqrt(n)))

            else:
                return (int(math.sqrt(n)), 1)

        else:
            upperSquare = listOfNums[index+1]
            line = math.sqrt(upperSquare)


            distance = upperSquare - n

            oppDistance = 2 * line - 2 - distance

            if line % 2 == 1:
                if distance == oppDistance:
                    return (line, line)

                elif distance > oppDistance:
                    return (line, oppDistance+1)

                else:
                    return (distance+1, line)
            else:
                if distance == oppDistance:
                    return (line, line)

                elif distance > oppDistance:
                    return (oppDistance+1, line)

                else:
                    return (line, distance+1)

    n = int(input())

    for ans in calculate(n):
        print(ans)

def problem31():
    def calculate(n):
        def calculateForAnyTri(startN):
            ans = 0
            N = startN
            while N - 3 >= 0:
                ans += (N * 3 - 3)
                N -= 3

            return int((ans * 3 + 3 ** N) / 3) * 3

        # I dunno why I wrote func inside fund it just happened by itself
        return calculateForAnyTri(n)

    n = int(input())
    print(calculate(n))

def problem32():
    def calculate(word):
        Word = []
        for letter in word:
            Word.append(letter.lower())

        copyWord = Word.copy()
        Word.reverse()

        if Word == copyWord:
            return "yes"

        else:
            return "no"


    word = input()

    print(calculate(word))

def Helper():
    def PrintAll():
        num = 1
        L = []

        while num <= 20212021:
            num *= 4
            L.append(num)
        return L

    for Num in PrintAll():

        print(Num)






listOfProblems = [
    Problem(problem1, "Quadratic Equation Solver", 1),
    Problem(problem2, "Text Writer", 2),
    Problem(problem3, "Intercept Finder (For lines)", 3),
    Problem(problem4, "Intercept Finder (For parabolas)", 4),
    Problem(problem5, "Anton Quiz", 5),
    Problem(problem6, "Dice Roller", 6),
    Problem(problem7, "Password Maker", 7),
    Problem(problem8, "Video Game", 8),
    Problem(problem9, "Rock Paper Scissers", 9),
    Problem(problem10, "Subtracting Squares", 10),
    Problem(problem11, "Calculator", 11),
    Problem(problem12, "Hangman", 12),
    Problem(problem13, "Magic 8 Ball", 13),
    Problem(problem14, "??? Coming Soon", 14),
    Problem(problem15, "Fake ID generator", 15),
    Problem(problem16, "Number Guessing Game", 16),
    Problem(problem17, "Square", 17),
    Problem(problem18, "Pythagorean Theorem", 18),
    Problem(problem19, "Three Swimmers", 19),
    Problem(problem20, "Time Belts", 20),
    Problem(problem21, "Even - Odd", 21),
    Problem(problem22, "Ducks?", 22),
    Problem(problem23, "To Do List", 23),
    Problem(problem24, "Day of the Week Calculator", 24),
    Problem(problem25, "Time Till Death", 25),
    Problem(problem26, "Bus Stops", 26),
    Problem(problem27, "Agar.io", 27),
    Problem(problem28, "Boxes With Cakes", 28),
    Problem(problem29, "Peaceful Towers", 29),
    Problem(problem30, "Table", 30),
    Problem(problem31, "Triangles", 31),
    Problem(problem32, "Palindromes", 32),
    Problem(Helper, "f", 33),
]

problemHolder = ProblemHolder(listOfProblems)

