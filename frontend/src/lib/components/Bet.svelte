<script>
    export let handleBet;
    const options = ["Points", "Steals", "Rebounds"];
    const overUnder = ["Over", "Under"];
    let selectedOption = options[0];
    let selectedOverUnder = overUnder[0];
    let inputValue = '0';

    function cleanInput(event) {
        const { value } = event.target;
        const cleanValue = value.replace(/[^0-9]/g, '');
        inputValue = cleanValue;
    }

    function handleSubmit() {
        const bet = {
            type: selectedOption,
            overUnder: selectedOverUnder,
            value: inputValue
        };
        handleBet(bet);
    }
</script>

<div class="flex flex-col items-center justify-around h-full">
    <h1 class="font-semibold text-2xl">Select An Outcome</h1>
    <div class="flex items-center">
    <select bind:value={selectedOption} class="appearance-none w-full bg-white text-gray-700 py-3 px-4 pr-8 focus:outline-none focus:bg-white focus:border-gray-500 focus:ring focus:ring-opacity-50">
        {#each options as option}
            <option value={option}>{option}</option>
        {/each}
    </select>
    <select bind:value={selectedOverUnder} class="appearance-none w-full bg-white text-gray-700 py-3 px-4 pr-8 focus:outline-none focus:bg-white focus:border-gray-500 focus:ring focus:ring-opacity-50">
        {#each overUnder as option}
            <option value={option}>{option}</option>
        {/each}
    </select>
    <input type="number" bind:value={inputValue} on:input={cleanInput} class="text-black w-full px-4 py-3 pr-8 shadow-sm focus:ring focus:ring-opacity-50 focus:ring-blue-500 focus:border-blue-500 focus:outline-none"/>
    </div>
    <button on:click={handleSubmit} class="w-1/2 bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:ring focus:ring-opacity-50 focus:ring-blue-500">Bet</button>
</div>