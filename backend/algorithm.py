import math
import nba_directory
from nba_api.stats.endpoints import teaminfocommon
from nba_api.stats.endpoints import teamestimatedmetrics

def calculate_win_probability(bet_data: dict):
    sign = bet_data["overUnder"] == "Over" and 1 or -1
    value = bet_data["value"]
    
    
    expected_value = 20
    diff = int(bet_data["value"]) - expected_value
    probability = 1 / (1 + 1.5 ** (sign * diff))
    return expected_value, probability

def get_outcome(team1, team2):
    name1, name2 = team1, team2
    id1, id2 = 
    pace = teamestimatedmetrics.TeamEstimatedMetrics(league_id='00', season='2023-24', season_type='Regular Season').team_estimated_metrics.get_dict()
    offPace1, defpace1 = pace['data'][id1][7], pace['data'][id1][8]
    offPace2, defpace2 = pace['data'][id2][7], pace['data'][id2][8]
    
    netDifferenceOff, netDifferenceDef = round(offPace1 - defpace2, 1), round(offPace2 - defpace1, 1)
    out = ""
    
    if abs(netDifferenceOff) <= 2.0 and abs(netDifferenceDef) <= 2.0:
        out += "The " + name1 + " and " + name2 + " are evenly matched"
    if netDifferenceOff > 0 and netDifferenceDef > 0:
        if netDifferenceOff > netDifferenceDef:
            out += (name1 + " beats " + name2)
            if netDifferenceOff - netDifferenceDef >= 5:
                out += ("The " + name1 + " will definitely win")
            else:
                out += ("The " + name1 + " will probably win")
        elif netDifferenceDef > netDifferenceOff:
            out += (name2 + " beats " + name1)
    elif netDifferenceOff < 0 and netDifferenceDef < 0:
        if netDifferenceOff > netDifferenceDef:
            out += (name1 + " beats " + name2)
            if abs(netDifferenceDef) - abs(netDifferenceOff) >= 5:
                out += ("The " + name1 + " will definitely win")
            else:
                out += ("The " + name1 + " will probably win")
        elif netDifferenceDef > netDifferenceOff:
            out += (name2 + " beats " + name1)
    elif netDifferenceOff > 0 and netDifferenceDef < 0:
        out += (name1 + " beats " + name2)
        if netDifferenceOff + abs(netDifferenceDef) >= 5:
            out += ("The " + name1 + " will definitely win")
        else:
            out += ("The " + name1 + " will probably win")
    elif netDifferenceOff < 0 and netDifferenceDef > 0:
        out += (name2 + " beats " + name1)
        if abs(netDifferenceOff) + netDifferenceDef >= 5:
            out += ("The " + name1 + " will definitely win")
        else:
            out += ("The " + name1 + " will probably win")
    return out
    
    
    