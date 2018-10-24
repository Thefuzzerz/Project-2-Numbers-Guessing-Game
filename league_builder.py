import csv

PRACTICE_DATES = {"Dragons": "July 10th, 2018",
                  "Sharks": "July 12th, 2018",
                  "Raptors": "July 14th, 2018"}

""" Importing .csv file and allocating players to teams, evenly seperating
    experienced players. Generating informational letters for guardians
    based on name, team, teammates, and practice date. """


def league_build():
    if __name__ == '__main__':
        with open('soccer_players.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            all_players = [(
                            row['Name'],
                            row['Height (inches)'],
                            row['Soccer Experience'],
                            row['Guardian Name(s)']
                            ) for row in reader]

            # sorting teams evenly and assigning team name to player
            def team_split():
                new_players = ([player + ("Dragons",) for player in
                                all_players[0::3] if player[2] == "NO"] +
                               [player + ("Sharks",) for player in
                               all_players[1::3] if player[2] == "NO"] +
                               [player + ("Raptors",) for player in
                               all_players[2::3] if player[2] == "NO"])

                # placing experienced players
                exp_players = ([player + ("Dragons",) for player in
                                all_players[0::3] if player[2] == "YES"] +
                               [player + ("Sharks",) for player in
                               all_players[1::3] if player[2] == "YES"] +
                               [player + ("Raptors",) for player in
                               all_players[2::3] if player[2] == "YES"])
                master_roster = exp_players + new_players
                return master_roster

            master_roster = team_split()

            # create letters for parents
            def guardian_letter(current_player):
                def team_members(current_player):
                    team_members = [(player[0]) for player in master_roster
                                    if player[4] == current_player[4]
                                    and player[0] != current_player[0]]
                    for player in team_members:
                        return player

                practice_date = PRACTICE_DATES.get(current_player[4])
                player_name = (current_player[0].split())
                player_letter = open("{}_{}.txt".format(player_name[0].lower(),
                                     player_name[1].lower()), "w")

                # letter content
                welcome_msg = (f"Dear {current_player[3]},\n\n"
                               f"Your child {player_name[0]} has been "
                               f"selected to play for the {current_player[4]} "
                               f"this season!\n\n{player_name[0]} will be "
                               f"joined by the following members on their "
                               f"team:\n\n***** {current_player[4]} 2018 "
                               "Roster *****\n")

                team_mates = [(f"{player[0]}\n") for player in master_roster
                              if player[4] == current_player[4]
                              and player[0] != current_player[0]]

                group_msg = ("\nWe encourage guardians to carpool to help "
                             "reduce congestion, pollution, and crowding in "
                             "the parking structure.\nThis is also a "
                             "fantastic opportunity for the children to "
                             "socialize with each other.\n\nThe "
                             f"{current_player[4]}' first practice will be "
                             f"held on {practice_date}\n\nWe look forward to "
                             "seeing you there!!!\n\nSincerely,\nTreehouse "
                             "Soccer Management")

                player_letter.writelines(welcome_msg)
                player_letter.writelines(team_mates)
                player_letter.writelines(group_msg)
                player_letter.close()

            # generating full roster based on teams
            def team_letter():
                team_roster = open("teams.txt", "w")

                roster_title = "TREEHOUSE SOCCER LEAGUE TEAMS AND ROSTER"
                roster_header = ("=" * len(roster_title),
                                 f"\n{roster_title}\n",
                                 "=" * len(roster_title), "\n\n")

                sharks_header = ("\n", "*" * 10,
                                 " SHARKS ROSTER", "*" * 10, "\n")
                sharks_members = [f"\n{player[0]} | Experienced Player: "
                                  f"{player[2]} | Parent(s): {player[3]}"
                                  for player in master_roster
                                  if player[4] == "Sharks"]

                dragons_header = ("\n"*3, "*" * 10, " DRAGONS ROSTER",
                                  "*" * 10, "\n")
                dragons_members = [f"\n{player[0]} | Experienced Player: "
                                   f"{player[2]} | Parent(s): {player[3]}"
                                   for player in master_roster
                                   if player[4] == "Dragons"]

                raptors_header = ("\n"*3, "*" * 10, " RAPTORS ROSTER",
                                  "*" * 10, "\n")
                raptors_members = [f"\n{player[0]} | Experienced Player: "
                                   f"{player[2]} | Parent(s): {player[3]}"
                                   for player in master_roster
                                   if player[4] == "Raptors"]

                team_roster.writelines(roster_header)
                team_roster.writelines(sharks_header)
                team_roster.writelines(sharks_members)
                team_roster.writelines(dragons_header)
                team_roster.writelines(dragons_members)
                team_roster.writelines(raptors_header)
                team_roster.writelines(raptors_members)

            for current_player in master_roster:
                guardian_letter(current_player)

            team_letter()


league_build()
