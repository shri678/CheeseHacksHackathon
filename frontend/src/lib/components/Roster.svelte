<script>
    import { flip } from "svelte/animate";
    import {selectedPlayer} from '$lib/stores/SelectedPlayer.js';

    const team = [{name: "Stephen Curry", id: 201939}, {name: "Klay Thompson", id: 202691}, {name: "Draymond Green", id: 203110}, {name: "Andrew Wiggins", id: 203952}, {name: "James Wiseman", id: 1630164}];
    let positions = [
        {name: "Point Guard", players: [team[0]]},
        {name: "Shooting Guard", players: [team[1]]},
        {name: "Small Forward", players: [team[2]]},
        {name: "Power Forward", players: [team[3]]},
        {name: "Center", players: [team[4]]},
    ]
    let hoveredPosition;

    function dragStart(event, positionIndex, playerIndex) {
        const data = {positionIndex, playerIndex};
        event.dataTransfer.setData("text/plain", JSON.stringify(data));
    }

    function drop(event, positionIndex) {
        event.preventDefault();
        const json = event.dataTransfer.getData("text/plain");
        const data = JSON.parse(json);

        //Remove item from its container
        const [player] = positions[data.positionIndex].players.splice(data.playerIndex, 1);
        //Add item to new container
        positions[positionIndex].players.push(player);
        positions = positions;
        hoveredPosition = null;
    }

</script>

<div class="flex flex-col items-center justify-around h-100 gap-4 p-8">
    {#each positions as position, positionIndex (position)}
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div class="w-40 h-40 bg-slate-200 border border-solid border-slate-300 "
        on:dragenter={() => hoveredPosition = position.name} on:dragleave={() => hoveredPosition = null} on:drop={e => drop(e, positionIndex)} animate:flip on:dragover={e => e.preventDefault()}
        class:border-teal-300={hoveredPosition === position.name}>
            {#if positions[positionIndex].players.length === 0}
                <p class="text-center text-slate-500 font-semibold text-lg">{position.name}</p>
            {/if}
            {#each position.players as player, playerIndex (player)}
                <!-- svelte-ignore a11y-no-static-element-interactions -->
                <div class="max-w-xs shadow-lg w-full h-full rounded inline-block border-solid border-teal-200 border-4 bg-slate-200"
                on:dragstart={e => dragStart(e, positionIndex, playerIndex)} animate:flip draggable="true" on:dblclick={() => selectedPlayer.set(player.name)}
                class:border-red-500={$selectedPlayer === player.name}>
                    <h1 class="font-bold text-lg h-1/4 text-center">{player.name.split(" ")[1]}</h1>
                    <img class="w-full h-3/4" src={`https://cdn.nba.com/headshots/nba/latest/260x190/${player.id}.png`} alt="player headshot"/>
                </div>
            {/each}
        </div>
    {/each}
</div>