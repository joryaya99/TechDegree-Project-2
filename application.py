import constants
from copy import deepcopy

players_data = deepcopy(constants.PLAYERS)
teams_data = deepcopy(constants.TEAMS)

def clean_data():
  for player in players_data:
    if player["experience"] == "YES":
      player["experience"] = True
    else:
      player["experience"] = False
    player["height"] = int(player["height"][:2])


def balance_teams():
  Panthers = []
  Bandits = []
  Warriors = []
  teams = [Panthers, Bandits, Warriors]
  num_players_team = int(len(players_data) / len(teams))
  for player in range(len(players_data)):
    teams[player % len(teams)].append(players_data[player])
  return Panthers, Bandits, Warriors

def experience_counter(x):
  count = 0
  for players in x:
    if players['experience'] == True:
      count += 1
  print ("Players With Experience: ", count)

def players_names(x):
  roster = []
  for players in x:
    roster.append(players['name'])
  updated_roster = ", ".join(roster)
  print ("Players On The Team: " "\n", updated_roster)

def guardians(x):
  parents = []
  for players in x:
    parents.append(players['guardians'])
  updated_parents = ", ".join(parents)
  print ("The crowd tonight consists of these proud parents: " "\n", updated_parents)

def team_selection(x):
  print("\nTotal Roster Size: " , len(x))
  experience_counter(x)
  players_names(x)
  guardians(x)
  welcome_screen()

def welcome_screen():
  print ('\n'"{}, welcome to the Basketball Team Stats Tool !!!"'\n'
         "\n--- MENU ---" '\n'  
         "\nPlease pick one of the two options:" 
         "\nA.) Display Team Stats" 
         "\nB.) Quit Application"
         "\n"
         .format(user_name)
        )
  option_one()

def option_one():
  while True:
    try:
      user_option_one = input("What can we do for your today{} ? ".format(user_name)).lower()
    except ValueError as err:
      print("Please use a proper response, {}".format(user_name))
    else:
      if user_option_one == 'a':
        print ("A.) Panthers Team Stats" "\nB.) Bandits Team Stats" "\nC.) Warriors Team Stats")
        option_two()
        break
      elif user_option_one == 'b':
        print ("Thank you for stopping by today {} !".format(user_name))
        break
      else:
        print ("Please pick one of the two options")
  
def option_two():
  while True:
    try:
      user_option_two = input("\n{}, what team would you like to see the stats for ? ".format(user_name)).lower()
    except ValueError as err:
      print("Please use a proper response, {}".format(user_name))
    else:
      if user_option_two == 'a':
        print("\nTeam: Panther Stats"
              "\n-----------------")
        team_selection(Panthers)
        break
      elif user_option_two == 'b':
        print("\nTeam: Bandits Stats"
              "\n-----------------")
        team_selection(Bandits)
        break
      elif user_option_two == 'c':
        print("\nTeam: Warriors Stats"
              "\n-----------------")
        team_selection(Warriors)
        break
      else:
        print ("Please pick one of the three options")
        
if __name__ == "__main__":
  user_name = input("What is your name ?" )
  clean_data()
  balance_teams()
  Panthers, Bandits, Warriors = balance_teams()
  welcome_screen()
