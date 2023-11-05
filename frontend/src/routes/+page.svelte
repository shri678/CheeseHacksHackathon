<script>
    import Roster from '$lib/components/Roster.svelte'
    import Bet from '$lib/components/Bet.svelte'
    import BetInfo from '$lib/components/BetInfo.svelte'
    import {selectedPlayer} from '$lib/stores/SelectedPlayer.js'

    const teams = {
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
    const teamNames = Object.values(teams);
    let selectedTeam1 = teams[0];
    let selectedTeam2 = teams[1];
    let opposingPlayer;
    let betData = {
        expectedValue: 0,
        winProbability: 0,
    }

    async function handleBet({type, overUnder, value}) {
        const data = {
            type,
            overUnder,
            value,
            selectedPlayer: $selectedPlayer,
            opposingPlayer: $selectedPlayer,
        }
        await fetch("http://localhost:8000/bets", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then((res) => res.json())
        .then((json) => {
            console.log(json);
            betData = json;
        })
        .catch((err) => console.log(err));
    }
</script>

<main class="flex justify-between h-screen items-center bg-slate-700">
    <div class="flex-1 p-4 h-full">
        <select bind:value={selectedTeam1} class="w-full bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 px-4 py-2 text-center">
        {#each teamNames as team}
            <option value={team}>{team}</option>
        {/each}
        </select>
        <Roster teamName={selectedTeam1}/>
    </div>
    <div class="flex-1 flex flex-col justify-center items-center gap-5 h-full">
        <img src="images/logo.jpeg" alt="logo" class="w-36 h-36 rounded-full"/> 
        <div class="bg-white p-4 h-1/3 w-full rounded-lg">
        <Bet handleBet={handleBet}/>
        </div>
        <div class="bg-white p-4 h-1/3 w-full rounded-lg">
        <BetInfo betData={betData}/>
        </div>
    </div>
    <div class="flex-1 p-4 h-full">
        <select bind:value={selectedTeam2} class="w-full bg-blue-500 text-white font-semibold rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 px-4 py-2 text-center">
        {#each teamNames as team}
            <option value={team}>{team}</option>
        {/each}
        </select>
        <Roster teamName={selectedTeam2}/>
    </div>
</main>
