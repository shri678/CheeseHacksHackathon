<script>
    import Roster from '$lib/components/Roster.svelte'
    import Bet from '$lib/components/Bet.svelte'

    const teams = ["Warriors", "Nuggets", "Heat"];
    let selectedTeam1 = teams[0];
    let selectedTeam2 = teams[1];

    let selectedPlayer;
    const testPlayers1 = [{name: "Stephen Curry", id: 201939}, {name: "Klay Thompson", id: 202691}, {name: "Draymond Green", id: 203110}, {name: "Andrew Wiggins", id: 203952}, {name: "James Wiseman", id: 1630164}];
    const testPlayers2 = [{name: "Nikola Jokic", id: 203999}, {name: "Jamal Murray", id: 1627750}, {name: "Michael Porter Jr.", id: 1629008}, {name: "Will Barton", id: 203115}, {name: "Paul Millsap", id: 200794}];

    function handleBet({type, overUnder, value}) {
        console.log(type, overUnder, value);
    }
</script>

<main class="flex justify-between h-screen items-center">
    <div class="flex-1 border p-4 h-full">
        <select bind:value={selectedTeam1} class="w-full bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 px-4 py-2">
        {#each teams as team}
            <option value={team}>{team}</option>
        {/each}
        </select>
        <Roster team={testPlayers1}/>
    </div>
    <div class="flex-1 border p-4 h-1/3">
        <Bet handleBet/>
    </div>
    <div class="flex-1 border p-4 h-full">
        <select bind:value={selectedTeam2} class="w-full bg-blue-500 text-white font-semibold rounded-lg hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 px-4 py-2">
        {#each teams as team}
            <option value={team}>{team}</option>
        {/each}
        </select>
        <Roster team={testPlayers2}/>
    </div>
</main>
