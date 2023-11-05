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
    return 

#Returns the estimated win probability for a given bet
@app.post("/bets/")
async def calculate_bet(bet_data: dict):
    return calculate_win_probability(bet_data)