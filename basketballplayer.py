import time
import random
class BasketballTeam:

    def __init__(self, team_points: int, team_rbnds: int, team_ast: int, team_name: str, games_played: int, seeding: int):
        self.team_name = team_name
        self.team_points = team_points
        self.team_rbnds = team_rbnds
        self.team_ast = team_ast
        self.games_played = games_played
        self.seeding = seeding
    
    def team_total_stats(self):
        team_stats = (f'''{self.team_name} 2024-2025 Season Stats 
Total Points: {self.team_points}
Total Rebounds: {self.team_rbnds}
Total Assists: {self.team_ast}
Games Played: {self.games_played}
''')
        print(team_stats)
    
    def team_scoring_update(self):
    #updates the teams statistics per game 
        self.games_played += 1 
        self.team_points += random.randint(100,120)
        self.team_rbnds += random.randint(35,50)
        self.team_ast += random.randint(20,37)
    def team_update_average(self, adjustment_factor = 1.0):
    #Displays the teams averages per stat 
        points_average = (self.team_points/self.games_played) *adjustment_factor
        rbnds_average = (self.team_rbnds/self.games_played)*adjustment_factor
        ast_average = (self.team_ast/self.games_played)*adjustment_factor
        team_avgs = (f'''{self.team_name} 2024-2025 Season Stats 
Average PPG: {round((points_average),1)}
Average REB: {round((rbnds_average),1)}
Average AST: {round((ast_average),1)}
Games Played: {self.games_played}
''')
        print(team_avgs)
    def display_stats(self):
        self.team_total_stats()
        time.sleep(2)
        self.team_update_average()
        time.sleep(2)
        self.team_scoring_update()
        self.team_total_stats()
        time.sleep(2)
        self.team_update_average()

        

    
def main():
    team_one = BasketballTeam(114*69, 108*69, 48*69, 'Warriors', 69, 6)
    team_two = BasketballTeam(119*69, 101*69, 43*69, 'Thunder', 69, 1)
    team_three = BasketballTeam(113*70, 112*70, 43*70, 'Rockets', 70, 2)
    team_four = BasketballTeam(115*68, 106*68, 46*68, 'Lakers', 68, 3)
    team_five= BasketballTeam(120*70, 119*70, 51*70, 'Nuggets', 70, 4)
    team_six = BasketballTeam(122*70, 113*70, 42*70, 'Grizzlies', 70, 5)
    team_seven = BasketballTeam(117*69, 106*69, 49*69, 'Clippers', 69, 7)
    team_eight = BasketballTeam(167*71, 105*71, 37*71, 'Timberwolves', 71, 8)
    team_nine = BasketballTeam(118*68, 102*68, 38*68, 'Kings', 68, 9)
    team_ten = BasketballTeam(110*70, 107*70, 41*70, 'Suns', 70, 10)
    team_eleven = BasketballTeam(119*70, 112*70, 42*70, 'Mavericks', 70, 11)
    team_twelve = BasketballTeam(112*68, 101*68, 38*68, 'Trailblazers', 68, 12)
    team_thirteen = BasketballTeam(105*68, 112*68, 35*68, 'Spurs', 68, 13)
    team_fourteen = BasketballTeam(102*70, 100*70, 43*70, 'Pelicans', 70, 14)
    team_fifteen = BasketballTeam(100*70, 98*70, 44*70, 'Jazz', 70, 15)

    print('_______Western Conference_______')
    print(team_one.display_stats())
    time.sleep(3)
    print(team_two.display_stats())
    time.sleep(3)
    print(team_three.display_stats())
    time.sleep(3)
    print(team_four.display_stats())
    time.sleep(3)
    print(team_five.display_stats())
    time.sleep(3)
    print(team_six.display_stats())
    time.sleep(3)
    print(team_seven.display_stats())
    time.sleep(3)
    print(team_eight.display_stats())
    time.sleep(3)
    print(team_nine.display_stats())
    time.sleep(3)
    print(team_ten.display_stats())
    time.sleep(3)
    print(team_eleven.display_stats())
    time.sleep(3)
    print(team_twelve.display_stats())
    time.sleep(3)
    print(team_thirteen.display_stats())
    time.sleep(3)
    print(team_fourteen.display_stats())
    time.sleep(3)
    print(team_fifteen.display_stats())
    time.sleep(3)
    print(f"""Western Conference Standings
1 Seed: {team_two.team_name}
2 Seed: {team_three.team_name}
3 Seed: {team_four.team_name}
4 Seed: {team_five.team_name}
5 Seed: {team_six.team_name}
6 Seed: {team_one.team_name}
____Playoffs____
7 Seed: {team_seven.team_name}
8 Seed: {team_eight.team_name}
9 Seed: {team_nine.team_name}
10 Seed: {team_ten.team_name}
____Play-In Tournament____
11 Seed: {team_eleven.team_name}
12 Seed: {team_twelve.team_name}
13 Seed: {team_thirteen.team_name}
14 Seed: {team_fourteen.team_name}
15 Seed: {team_fifteen.team_name}

""")
    print('_______Eastern Conference_______')

if __name__ == "__main__":
    main()