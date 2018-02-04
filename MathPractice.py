import Tkinter as Tk
import random
from random import randint


def mathProblem():
    """Randomly generate two numbers between 0 and 20 to be added together"""
    global realAnswer, x, y
    problem = operation.get()
    userMessage["text"] = "Give it a try!"
    if problem == 1:
        operationLabel["text"] = "+"
        x = randint(0, 20)
        y = randint(0, 20)
        realAnswer = x + y
        print'Real answer is: {}'.format(realAnswer)
    elif problem == 2:
        operationLabel["text"] = "-"
        x = randint(0, 20)
        y = randint(0, x)
        realAnswer = x - y
        print'Real answer is: {}'.format(realAnswer)
    elif problem == 3:
        operationLabel["text"] = "x"
        x = randint(0, 10)
        y = randint(0, 10)
        realAnswer = x * y
        print'Real answer is: {}'.format(realAnswer)
    elif problem == 4:
        operationLabel["text"] = "/"
        x = randint(0, 50)
        xFactors = []
        for i in range(1, x + 1):
            if x % i == 0:
                xFactors.append(i)
        print'Factors of the numerator: {}'.format(xFactors)
        y = random.choice(xFactors)
        realAnswer = x / y
        print'Real answer is: {}'.format(realAnswer)
    else:
        print("something went wrong!")

    xLabel["text"] = x
    yLabel["text"] = y
    answerEntry.delete(0, 5)


def checkProblem(event):        # Not sure why squiggly under input, its needed to make the 'Enter' button work
    """Check answer to the problem generated"""
    guess = int(userAnswer.get())
    real = realAnswer
    if guess == real:
        userMessage["text"] = "You are correct!"
        newProblem["text"] = "Next Problem"
    elif guess != real:
        userMessage["text"] = "Sorry, wrong answer.  Try again..."
        answerEntry.delete(0, 5)
    else:
        print("something went wrong!")


# Create and configure root window
root = Tk.Tk()
root.title("Math Program")
root.geometry("500x400")
root.configure(bg="white")

# Establish variables
operation = Tk.IntVar()
operation.set(1)
userAnswer = Tk.StringVar()

# Create Title label
titleFrame = Tk.Frame(root, pady=20, padx=10, bg="white")
titleFrame.pack()
titleLabel = Tk.Label(titleFrame, text="Math Practice!", bg="white", font="Verdana 20 bold")
titleLabel.pack()

# Create Labels where the math problem with be
problemFrame = Tk.Frame(root, pady=20, padx=10, bg="white")
problemFrame.pack()

xLabel = Tk.Label(problemFrame, text="?", width=3, bg="white", font="Verdana 16 bold")
xLabel.pack(side="left")

operationLabel = Tk.Label(problemFrame, text="+", width=3, bg="white", font="Verdana 16 bold")
operationLabel.pack(side="left")

yLabel = Tk.Label(problemFrame, text="?", width=3, bg="white", font="Verdana 16 bold")
yLabel.pack(side="left")

equalLabel = Tk.Label(problemFrame, text="=", width=3, bg="white", font="Verdana 16 bold")
equalLabel.pack(side="left")

answerEntry = Tk.Entry(problemFrame, width=5, bg="light gray", font="Verdana 16 bold", justify="center",
                       textvariable=userAnswer)
# Bind "Enter" key on keyboard to also checkProblem
answerEntry.bind('<Return>', checkProblem)
answerEntry.pack(side="left")

# Create radio buttons to choose between Addition or Subtraction problem
radioButtonFrame = Tk.Frame(root, pady=20, padx=10, bg="white")
radioButtonFrame.pack()
addButton = Tk.Radiobutton(radioButtonFrame, text="Addition", bg="white", variable=operation, value=1)
addButton.pack(side="left")
subtractButton = Tk.Radiobutton(radioButtonFrame, text="Subtraction", bg="white", variable=operation, value=2)
subtractButton.pack(side="left")
multiplyButton = Tk.Radiobutton(radioButtonFrame, text="Multiplication", bg="white", variable=operation, value=3)
multiplyButton.pack(side="left")
divideButton = Tk.Radiobutton(radioButtonFrame, text="Division", bg="white", variable=operation, value=4)
divideButton.pack(side="left")

# Create a message label
messageFrame = Tk.Frame(root, pady=20, padx=10, bg="white")
messageFrame.pack()
userMessage = Tk.Label(messageFrame, text="Ready to try?", bg="white", font="Verdana 16 bold")
userMessage.pack(fill="x")

# Create a button that will generate the numbers for the math problem.
buttonFrame = Tk.Frame(root, pady=20, padx=10, bg="white")
buttonFrame.pack()
newProblem = Tk.Button(buttonFrame, text="Start", bg="green", command=mathProblem)
newProblem.pack(side="left")

root.mainloop()
