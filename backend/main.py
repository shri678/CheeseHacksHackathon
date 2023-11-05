from fastapi import FastAPI
app = FastAPI()

@app.get("/teams/{team_name}")
async def get_team(team_name):
    return {"team_name": team_name}

@app.get("/bets/")
async def calculate_bet(bet_data):
    return 