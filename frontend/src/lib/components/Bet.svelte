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

<div class="">
    <h1>Select a Bet</h1>
    <select bind:value={selectedOption}>
        {#each options as option}
            <option value={option}>{option}</option>
        {/each}
    </select>
    <select bind:value={selectedOverUnder}>
        {#each overUnder as option}
            <option value={option}>{option}</option>
        {/each}
    </select>
    <input type="number" bind:value={inputValue} on:input={cleanInput} />
    <button on:click={handleSubmit}>Submit</button>
</div>