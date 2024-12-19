## BEFORE YOU RUN, MAKE SURE YOU HAVE "background.gif" DOWNLOADED AND IN THE SAME FOLDER AS THIS FILE ##



import random
import turtle

turtle.setup(2000, 1000)
screen = turtle.Screen()
screen.register_shape("background.gif")
screen.title("Hollow Knight: Silksong")
my_turtle = turtle.Turtle()
my_turtle.shape("background.gif")
turtle.hideturtle()
turtle.penup()

def rock(): # "rock" drawing
    turtle.speed(100)
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
def paper(): #Paper drawing
    turtle.speed(100)
    turtle.fillcolor('gray')
    turtle.begin_fill()
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.forward(160)
    turtle.left(90)
    turtle.forward(240)
    turtle.left(90)
    turtle.end_fill()    
def scissor(): #scissor drawing
    turtle.speed(1000000000000)
    turtle.fillcolor('red')
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.fillcolor('black')
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.left(90)
    turtle.fillcolor('gray')
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    turtle.right(90)
    turtle.forward(10)
    for i in range(0,2):
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,5):
        turtle.forward(10)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(10)
    turtle.begin_fill()
    for i in range(0,4):
        turtle.forward(10)
        turtle.left(90)
    turtle.end_fill()
    
def death():
    turtle.speed(100000)

    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(100)
    turtle.end_fill()
    turtle.fillcolor('#f9f57f')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    

def RPS(x):
    difficulty = x
    turtle.goto(0,200)
    user_life = 3
    com_life = 3
    while (user_life > 0 and com_life > 0): #continues to run until someone loses
        turtle.penup()
        turtle.goto(0,250)
        turtle.clear()
        turtle.write("Your Lives: {}  						Hornet's Lives: {}".format(user_life, com_life), align="center", font=("Courier", 24, "normal"))
        print("Your lives:", user_life, "\t Opponent's lives", com_life)
        action = int(input("Rock (1) \nPaper (2) \nScissors (3) \n\t")) #your decission input
        print()
        print()
        if difficulty == "easy":
            comp_action = 1 #computer decission input is always rock
        elif difficulty == "regular":
            comp_action = random.randint(1, 3) #computer decission input
        else: #computer will always beat you
            if action == 1:
                comp_action = 2
            elif action == 2:
                comp_action = 3
            else:
                comp_action = 1
        
        if comp_action == 1: 
            print("Hornet picked Rock")
            turtle.goto(250,0)
            turtle.pendown()
            rock()
            turtle.penup()
        if comp_action == 2:
            print("Hornet picked Paper")
            turtle.goto(100,0)
            turtle.pendown()
            paper()
            turtle.penup()
        if comp_action == 3:
            print("Hornet picked Scissors")
            turtle.goto(250,0)
            turtle.pendown()
            scissor()
            turtle.penup()
            
            
        if action == comp_action:
            if action == 1:
                turtle.goto(-250,0)
                turtle.pendown()
                rock()
                turtle.penup()
            if action == 2:
                turtle.goto(-250,0)
                turtle.pendown()
                paper()
                turtle.penup()
            if action == 3:
                turtle.goto(-250,0)
                turtle.pendown()
                scissors()
                turtle.penup()
                
                
            print("Tie")
            print()
            print()
            
            
        elif action == 1: #if you picked rock
            turtle.goto(-250,0)
            turtle.pendown()
            rock()
            turtle.penup()
            if comp_action == 2:
                print("Rock loses to Paper :(")
                print()
                print()
                user_life -= 1
                
            elif comp_action == 3:
                print("Rock beats Scissors!")
                print()
                print()
                com_life -= 1
                
        elif action == 2: #if you picks paper
            turtle.goto(-250,0)
            turtle.pendown()
            paper()
            turtle.penup()
            if comp_action == 3:
                print("Paper loses to Scissors :(")
                print()
                print()
                user_life -= 1
                
            elif comp_action == 1:
                print("Paper beats Rock!")
                print()
                print()
                com_life -= 1
                
        elif action == 3:#if you picks scissors
            turtle.goto(-250,0)
            turtle.pendown()
            scissor()
            turtle.penup()
            if comp_action == 1:
                print("Scissors loses to Rock :(")
                print()
                print()
                user_life -= 1
                
            elif comp_action == 2:
                print("Scissors beats Paper!")
                print()
                print()
                com_life -= 1
                
        else: #if you misinput a higher number (doesn't work if inputs characters)
            print("Incorrect input, try again!")
            print()
            print()
    turtle.goto(0,200)
    turtle.clear()
    turtle.write("Your Lives: {}  						Hornet's Lives: {}".format(user_life, com_life), align="center", font=("Courier", 24, "normal"))
                
    if user_life > com_life: #checks if you still have lives left
        print("User wins!")
        turtle.goto(0,0)
        turtle.write("You Win!", align="center", font=("Courier", 50, "normal"))
        turtle.goto(450,-150)
        death()
            
    else: #checks if Hornet still has lives left
        print("You Lost ඞ")
        turtle.goto(0,0)
        turtle.write("You Lost ඞ", align="center", font=("Courier", 50, "normal"))
        turtle.goto(-450,-150)
        death()
    
    pp = int(input("Play again? \n1: Yes \n2: No \n\t"))
    
    if pp == 1:
        main()
    else:
        print("good bye!")
    

def main():
    
    mode = int(input("Welcome to rock, paper, scissors! Please enter a difficutly: \n1: easy \n2: medium \n3: impossible \n\t"))    
    if mode == 1:
        RPS("easy")
        
    elif mode == 2:
        RPS("regular")
        
    elif mode == 3:
        RPS("impossible")
        
        
    else:
        print("Incorrect input, try again.")
        
    
    
main()
