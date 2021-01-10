import constants
from constants import PLAYERS
from constants import TEAMS
#use imported player data for calculations

if __name__ == "__main__":
    #code function

    def clean_data():
    # 1) read the existing player data from the PLAYERS constants provided
    # in constants.py
    # 2) clean the player data without changing the original data USE .copy
    #Data to be cleaned:
    #Height: This should be saved as an integer
        team_name = TEAMS.copy()
        team_players = PLAYERS.copy()
        for player in team_players:
            player['height'] = int('height')

    # Experience: This should be saved as a boolean value (True or False)
    # DO NOT MODIFY constants data
        for player1 in team_players:
            if player1['experience'] == 'YES':
                player1['experience'] = True
            else:
                player1['experience'] = False
        return team_name, team_players #TODO NOT sure how to call these returned values for later code
    #team_name1, team_players1 = clean_data()
    #def balance_teams():
    def balance_teams():
    # HINT: To find out how many players should be on each team, divide the length of
    # players by the number of teams.
        num_players_team = len(PLAYERS) / len(TEAMS) #TODO this could potentially give a float so round down.
    # set counter == num_players_team and have it count down to 0 til while statement becomes FALSE and stops recruiting.
        counter = num_players_team
    #Now that the player data has been cleaned, balance the players across the three
        while counter > 1:
            for team in team_name1:
                for player in team_players1:
                    team_name1.append(player.pop(max['height']))
                    counter -= 1 # this will countdown to <1 and turn off the while loop
    # teams: Panthers, Bandits and Warriors.
    # max(height) popped from the list of players and then appended to team that did draft. .pop eliminated it from player pool



print("Basketball Team Statistics Tool\n\n---- Menu ----")
choice1 = input("Please Select From the Following Menus:\n1) Display Team Stats\n2) Quit\nChoice>  ")
while True:
    if choice1 == "1":
        print(TEAMS)
        pass #TODO display team stats
    elif choice1 == "2":
        quit
    else:
        print("Please enter the number of your choice again please") #should I try exceptions?
        choice1 = input("Please Select From the Following Menus:\n1) Display Team Stats\n2) Quit\nChoice>  ")
            #This code is not running properly, the print() never gets run despite a non 1-2 choice.
