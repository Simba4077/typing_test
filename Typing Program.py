#Typing speed program
#Test your typing skills and see how many wpms you can type!
#3 modes: easy, medium, hard
#Gives user 3 lines of text and then starts timer when user starts typing
#When user hits enter, they have finished the typing test
#WPM is returned

import time
from time import sleep
import sys
from random_word import RandomWords
#import tkinter as tk

# def start_window():
#     window = tk.Tk()
#     greeting = tk.Label(
#         text = "Ready to start you typing test",
#         foreground = "white",
#         background = "black",
#         width = 40,
#         height = 10,
#         )
#     greeting.pack()
#     start = tk.Button(
#         text = "Click here to start!",
#         foreground = "white",
#         background = "red",
#         command = button_click,
#         width = 10,
#         height = 2,
#         )
#     start.pack()
#     window.mainloop()

# def button_click():
#     global start
#     start = time.time()


def generate_word():
    r = RandomWords()
    return r.get_random_word()

def type_effect(text):
    for char in text:
        sleep(0.04)
        sys.stdout.write(char)
        sys.stdout.flush()


    
def init():
    text = ""
    for i in range(31):
        word = generate_word()
        text+=" "
        text+=word
    return text
    
def comparision(text, user):
    score = 0
    if len(text) > len(user):
        for i in range(len(user)):
            if user[i] == text[i]:
                score+=1

    
    else:
        for i in range(len(text)):
            if user[i] == text[i]:
                score+=1

    return score

def accuracy(score):
    return score / 30

def wpm(time):
    return 30 / time


text = init()
# opening = "Are you ready to start your typing test and find out how many WPM you can type?? "
# type_effect(opening)
# sleep(0.1)
# opening = "Let's get started. A 30 word phrase will appear; start typing what you see on the screen and press ENTER when you're finished"
# type_effect(opening)
# print("\n")
type_effect(text)
# print("\n")
# ready = "You ready? Start typing in 3...2...1...GO"

# type_effect(ready)
start = time.time()
print("\n")

user_text = input()
end = time.time()
done = "Let's now calculate your wpm and accuracy"
type_effect(done)

fin_time = end - start
fin_score = comparision(text, user_text)
fin_accuracy = accuracy(fin_score)
fin_wpm = wpm(fin_time)

stats = "Here are your stats:"
type_effect(stats)
print("\n")
print(fin_time)
print(fin_score)
print(fin_accuracy)
print(fin_wpm)






#start_window()
