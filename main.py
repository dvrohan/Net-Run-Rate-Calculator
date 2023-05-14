# 12 172 16.2 171 120

no_of_matches = int(input('Enter number of matches played '))

runs_scored  = []
overs_played = []

runs_conceded = []
overs_bowled = []

def print_nrr():
    own_rr = sum(runs_scored)/(sum(overs_played)/6)
    opp_rr = sum(runs_conceded)/(sum(overs_bowled)/6)
    print('NRR:', own_rr-opp_rr)

for index in range(no_of_matches):
    runs_scored.append((int(input('Enter runs scored in match {} '.format(index+1)))))
    played_overs = input('Enter overs played in match {} '.format(index+1))
    played_overs = played_overs.split('.')
    if(len(played_overs) == 2):
        played_overs = int(played_overs[0])*6 + int(played_overs[1])
    else:
        played_overs = int(played_overs[0])*6
    overs_played.append(played_overs)
    runs_conceded.append((int(input('Enter runs conceded in match {} '.format(index+1)))))
    bowled_overs = input('Enter overs bowled in match {} '.format(index+1))
    bowled_overs = bowled_overs.split('.')
    if(len(bowled_overs) == 2):
        bowled_overs = int(bowled_overs[0])*6 + int(bowled_overs[1])
    else:
        bowled_overs = int(bowled_overs[0])*6
    overs_bowled.append(bowled_overs)
    print_nrr()
print(runs_scored, overs_played, runs_conceded, overs_bowled)