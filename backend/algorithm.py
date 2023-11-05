import math
from nba_directory import get_team_id
from nba_api.stats.endpoints import teaminfocommon, playerdashboardbygeneralsplits, teamestimatedmetrics
from nba_api.stats.static import players

def calculate_win_probability(bet_data):
    sign = bet_data["overUnder"] == "Over" and 1 or -1
    value = bet_data["value"]
    playerID = players.find_players_by_full_name(bet_data["selectedPlayer"])[0]["id"]
    playerGeneralInfo = playerdashboardbygeneralsplits.PlayerDashboardByGeneralSplits(season='2023-24',season_type_playoffs='Regular Season', player_id=playerID).overall_player_dashboard.get_dict() 
    playerPTS = playerGeneralInfo['data'][0][26]
    playerREB = playerGeneralInfo['data'][0][18]
    playerSTL = playerGeneralInfo['data'][0][21]
    playerGP = playerGeneralInfo['data'][0][2]
    if bet_data["type"] == "Points":
        expected_value = playerPTS
    elif bet_data["type"] == "Rebounds":
        expected_value = playerREB
    else:
        expected_value = playerSTL
    expected_value = round(expected_value / playerGP)
        
    

    diff = int(bet_data["value"]) - expected_value
    probability = 1 / (1 + 1.5 ** (sign * diff))
    return expected_value, probability

def get_outcome(team1, team2):
    name1, name2 = team1.split()[-1], team2.split()[-1]
    id1, id2 = get_team_id(team1), get_team_id(team2)
    pace = teamestimatedmetrics.TeamEstimatedMetrics(league_id='00', season='2023-24', season_type='Regular Season').team_estimated_metrics.get_dict()
    offPace1, defpace1 = pace['data'][id1][7], pace['data'][id1][8]
    offPace2, defpace2 = pace['data'][id2][7], pace['data'][id2][8]
    
    netDifferenceOff, netDifferenceDef = round(offPace1 - defpace2, 1), round(offPace2 - defpace1, 1)
    out = ""
    
    if abs(netDifferenceOff) <= 2.0 and abs(netDifferenceDef) <= 2.0:
        out += "The " + name1 + " and " + name2 + " are evenly matched"
    else:
        if netDifferenceOff > 0 and netDifferenceDef > 0:
            if netDifferenceOff > netDifferenceDef:
                result = name1 + " beat " + name2
            else:
                result = name2 + " beat " + name1
        elif netDifferenceOff < 0 and netDifferenceDef < 0:
            if netDifferenceOff > netDifferenceDef:
                result = name1 + " beat " + name2
            else:
                result = name2 + " beat " + name1
        elif netDifferenceOff > 0 and netDifferenceDef < 0:
            result = name1 + " beat " + name2
        else:
            result = name2 + " beat " + name1

        if abs(netDifferenceOff) + abs(netDifferenceDef) >= 5:
            out += result + "\nDefinite Win"
        else:
            out += result + "\nProbable Win"

    return out
    
    
    