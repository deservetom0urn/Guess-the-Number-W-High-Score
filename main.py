import random
import os
import time

RandomNumber = random.randint(1, 20)

def menu():
  print("Welcome to the guessing game!")
  data = open('Datas.txt', "r")
  print("High score : ", data.readlines()[1])
  data.close()
  name = input("Input your name: ")
  guess = int(input("Input number here: "))
  GuessLeft = 0
  while guess != RandomNumber:
    # print(RandomNumber)2
    GuessLeft += 1
    if guess > RandomNumber:
      print("The number you guessed is too big from the answer, try again!")
      print("Your guess: ", GuessLeft)
      guess = int(input("Your Guess? "))
    elif guess < RandomNumber:
      print("The number you guessed is too small from the answer, try again!")
      print("Your guess: ", GuessLeft)
      guess = int(input("Your Guess? "))

  if guess == RandomNumber:
    os.system("clear")
    time.sleep(1)
    print("Correct!")
    data = open('Datas.txt', "r")
    score = data.readlines()[1]
    print("Current score = ", score)
    print("Score now = ", GuessLeft)
      
    if GuessLeft < int(score):
      data = open('Datas.txt', 'w')
      data.writelines([str(name), "\n", str(GuessLeft)])
      data.close()
      input("Try again? ")
      menu()
menu()
