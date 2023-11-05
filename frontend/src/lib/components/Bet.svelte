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

<div class="flex flex-col items-center justify-between h-full">
    <h1 class="font-semibold text-xl">Select An Outcome</h1>
    <div class="flex items-center">
    <select bind:value={selectedOption} class="appearance-none w-full bg-white border border-gray-300 text-gray-700 py-3 px-4 pr-8 rounded-lg leading-tight focus:outline-none focus:bg-white focus:border-gray-500 focus:ring focus:ring-opacity-50">
        {#each options as option}
            <option value={option}>{option}</option>
        {/each}
    </select>
    <select bind:value={selectedOverUnder} class="appearance-none w-full bg-white border border-gray-300 text-gray-700 py-3 px-4 pr-8 rounded-lg leading-tight focus:outline-none focus:bg-white focus:border-gray-500 focus:ring focus:ring-opacity-50">
        {#each overUnder as option}
            <option value={option}>{option}</option>
        {/each}
    </select>
    <input type="number" bind:value={inputValue} on:input={cleanInput} class="w-full px-4 py-2 rounded-lg border border-gray-300 shadow-sm focus:ring focus:ring-opacity-50 focus:ring-blue-500 focus:border-blue-500 focus:outline-none"/>
    </div>
    <button on:click={handleSubmit} class="rounded-md bg-emerald-200 w-3/4 h-1/6">Submit</button>
</div>