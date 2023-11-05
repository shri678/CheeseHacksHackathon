from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from algorithm import calculate_win_probability, get_outcome
from nba_directory import get_players_data
from nba_directory import return_data_team

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

class Game(BaseModel):
    team1: str
    team2: str

# Returns the player names and ids for a given team
@app.get("/teams/{team_name}")
async def get_team(team_name: str):
    return return_data_team(team_name)

@app.post("/results/")
async def get_results(game: Game):
    return get_outcome(game.team1, game.team2)

#Returns the estimated win probability for a given bet
@app.post("/bets/")
async def calculate_bet(bet_data: dict):
    expected_value, win_probability = calculate_win_probability(bet_data)
    return {"expectedValue": expected_value, "winProbability": win_probability}
