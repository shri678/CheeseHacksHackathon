<script>
    export let betData;
</script>

<div class="flex flex-row items-center justify-around h-full">
    <div>
        <h1 class="font-semibold text-xl">Expected Value: </h1>
        <h1 class="text-3xl font-semibold text-center">{betData.expectedValue}</h1>
    </div>
    <div>
        <h1 class="font-semibold text-xl">Payoff Probability: </h1>
        <h1 class="text-3xl font-semibold text-center">{betData.winProbability * 100 + "%"}</h1>
    </div>
</div>