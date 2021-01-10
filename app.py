import constants
from constants import PLAYERS
from constants import TEAMS
#use imported player data for calculations



def clean_data(team_name, team_players):
    # 1) read the existing player data from the PLAYERS constants provided
    # in constants.py
    # 2) clean the player data without changing the original data USE .copy
    #Data to be cleaned:

    #team_name = TEAMS.copy()
    #team_players = PLAYERS.copy()
    for player in team_players:
        # Height: This should be saved as an integer
        # looks like: '40 inches'
        num, word = player['height'].split(" ")
        player['height'] = int(num)
        # Experience: This should be saved as a boolean value (True or False)
        # DO NOT MODIFY constants data
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

    return team_name, team_players #TODO NOT sure how to call these returned values for later code
    #team_name1, team_players1 = clean_data()


def balance_teams(team_name, team_players):
    # HINT: To find out how many players should be on each team, divide the length of
    # players by the number of teams.
    num_players_team = len(team_players) / len(team_name)
    # set counter == num_players_team and have it count down to 0 til while statement becomes FALSE and stops recruiting.
    final_teams = []
    for team in team_name:
        final_teams.append({"name": team, "players": []})
    counter = num_players_team
    #Now that the player data has been cleaned, balance the players across the three
    all_heights = [item['height'] for item in team_players]  # [42, 40, 45, ...]

    while counter >= 1:
        for team in final_teams:
            tallest_loc = all_heights.index(max(all_heights))  # returns 3
            all_heights.pop(tallest_loc)
            team["players"].append(team_players.pop(tallest_loc))
        counter -= 1
    return final_teams

    # teams: Panthers, Bandits and Warriors.
    # max(height) popped from the list of players and then appended to team that did draft. .pop eliminated it from player pool


if __name__ == "__main__":
    my_team_names = TEAMS.copy()
    my_players = PLAYERS.copy()

    my_team_names, my_players = clean_data(my_team_names, my_players)
    my_teams = balance_teams(my_team_names, my_players)

    print("Basketball Team Statistics Tool\n\n---- Menu ----")

    while True:
        choice1 = input("Please Select From the Following Menus:\n1) Display Team Stats\n2) Quit\nChoice>  ")
        if choice1 == "1":
            print(my_teams)
            # TODO display team stats
        elif choice1 == "2":
            quit()
        else:
            print("Please enter the number of your choice again please")

