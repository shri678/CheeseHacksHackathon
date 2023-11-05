from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from algorithm import calculate_win_probability
from nba_directory import get_players_data
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Returns the player names and ids for a given team
@app.get("/teams/{team_name}")
async def get_team(team_name: str):
    team = teams.find_teams_by_full_name(regex_pattern=team_name)
    team = team[0]

    play = commonteamroster.CommonTeamRoster(team_id=team['id'])

    play.get_data_frames()[0]

    # json
    play.get_json()

    # dictionary
    team_info = play.get_dict()['resultSets'][0]['rowSet']

    player_name_and_id = []
    for player in team_info:
        player_name_and_id.append({"name": player[3], "id":player[14]})

    return player_name_and_id

#Returns the estimated win probability for a given bet
@app.post("/bets/")
async def calculate_bet(bet_data: dict):
    expected_value, win_probability = calculate_win_probability(bet_data)
    return {"expectedValue": expected_value, "winProbability": win_probability}
