#
#   Python:          3.9.2
#
#   Author:           Paul D. Fairbanks         
#
#   Purpose:        The Tech Academy - Python Course, creating my first program.
#                           Demonstraiting how to pass variables from function to function
#                           while producing a functional game.
#
#                           function_name(variable) _means that we pass in the variable.
#                           return variable _means that we are returning the variable back
#                           to the calling function.







def start(nice=0,mean=0,name="") : # sets default values in parameters
  # get user's name
  name = describe_game(name)
  nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name) :
  """
          Check if this is a new game or not.
          If is new, get the users name.
          If it is not a new game, thank the player for
          playing again and continue with the game.
  """
  # meaning, if we do not already have this users name,
  # then they are a new player and we need to get their name.
  if name != "":
    print("\nThank you for playing again, {}!".format(name))
  else:
    stop = True
    while stop:
      if name == "":
        name = input("\nWhat is your name? \n>>> ").capitalize()
        if name != "":
          print("\nWelcome, {}!".format(name))
          print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
          print("but at the end of the game your fate \nwill be sealed by your actions.")
          stop = False

  return name


def nice_mean(nice,mean,name):
  stop = True
  while stop:
    show_score(nice,mean,name)
    pick = input("\nA elderly woman approaches you asking for directions. \nWill you be nice \nor mean? (N/M) \n>>>: ").lower()
    if pick == "n":
        print("\nThe elderly woman walks away smiling...")
        nice = (nice + 1)
        stop = False
    if pick == "m":
        print ("\nThe elderly woamn glares at you \nmenacingly and storms off...")
        mean = (mean + 1)
        stop = False
  score(nice,mean,name) # pass the 3 variables to the score ()


def show_score(nice,mean,name):
  print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
  # score function is being passed the values stoted within the 3 variables
  if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
    win(nice,mean,name)
  if mean > 2: # if conditionis valid, call lose function passing in the variables so it can use them
    lose(nice,mean,name)
  else:           # else, call nice_mean function passding in the variables so it can use them
    nice_mean(nice,mean,name)


def win(nice,mean,name):
  # substitute the {} wildcards with our variable values
  print("\nNice job {}, you win! \nEveryone loves you and you've made lots of friends along the way!".format(name))
  again(nice,mean,name)


def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over! \n{}, your a heartless person, who deserves \nto be in a van by the river, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
  stop = True
  while stop:
    choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
    if choice == "y":
      stop = False
      reset(nice,mean,name)
    if choice =="n":
      print("\nOh, so sad, sorry to see you go!")
      stop = False
      quit()
    else:
      print("\nEnter ( Y ) for 'YES', ( N ) for 'NO' :\n>>> ")


def reset(nice,mean,name):
  nice = 0
  mean = 0
  # Notice, I do not reset the name variable as that same user has elected to play again
  start(nice,mean,name)


if __name__ == "__main__":
  start()

