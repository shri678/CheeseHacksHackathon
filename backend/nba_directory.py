from nba_api.stats.endpoints import playercareerstats, commonteamroster, teaminfocommon, teamestimatedmetrics

from nba_api.stats.static import players, teams
import pandas as pd


nba_teams = {
    'ATL': 'Atlanta Hawks',
    'BOS': 'Boston Celtics',
    'BKN': 'Brooklyn Nets',
    'CHA': 'Charlotte Hornets',
    'CHI': 'Chicago Bulls',
    'CLE': 'Cleveland Cavaliers',
    'DAL': 'Dallas Mavericks',
    'DEN': 'Denver Nuggets',
    'DET': 'Detroit Pistons',
    'GSW': 'Golden State Warriors',
    'HOU': 'Houston Rockets',
    'IND': 'Indiana Pacers',
    'LAC': 'Los Angeles Clippers',
    'LAL': 'Los Angeles Lakers',
    'MEM': 'Memphis Grizzlies',
    'MIA': 'Miami Heat',
    'MIL': 'Milwaukee Bucks',
    'MIN': 'Minnesota Timberwolves',
    'NOP': 'New Orleans Pelicans',
    'NYK': 'New York Knicks',
    'OKC': 'Oklahoma City Thunder',
    'ORL': 'Orlando Magic',
    'PHI': 'Philadelphia 76ers',
    'PHX': 'Phoenix Suns',
    'POR': 'Portland Trail Blazers',
    'SAC': 'Sacramento Kings',
    'SAS': 'San Antonio Spurs',
    'TOR': 'Toronto Raptors',
    'UTA': 'Utah Jazz',
    'WAS': 'Washington Wizards'
}

#Receive player data provided the player ID
def get_players_data(id):
    career_player = playercareerstats.PlayerCareerStats(player_id=id) 
    career_player.get_data_frames()[0]
    career_player.get_json()
    return career_player.get_dict()['resultSets'][0]['rowSet'][::-1][:2]

def return_data_team(team_name):
    team = teams.find_teams_by_full_name(regex_pattern=team_name)
    team = team[0]
    
    play = commonteamroster.CommonTeamRoster(team_id=team['id'])
    
    play.get_data_frames()[0]
    play.get_json()

    team_info = play.get_dict()['resultSets'][0]['rowSet']

    player_name_and_id = []
    for player in team_info:
        player_name_and_id.append({"name": player[3], "id":player[14]})

    return player_name_and_id


info1 = teaminfocommon.TeamInfoCommon(team_id='1610612743')
info2 = teamestimatedmetrics.TeamEstimatedMetrics(league_id='00',season='2023-24',season_type='Regular Season')
avg = info1.team_season_ranks.get_dict()
pace = info2.team_estimated_metrics.get_dict()

for i in range(0,30):
    print(i, "is index for", pace['data'][i][0], pace['data'][i][7], pace['data'][i][8])

