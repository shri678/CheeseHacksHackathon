<script>
    export let betData;
</script>

<div class="flex flex-col items-center justify-between h-full">
    <h1 class="font-semibold text-xl">Expected Value: </h1>
    <h1 class="text-3xl font-semibold text-center">{betData.expectedValue}</h1>
    <h1 class="font-semibold text-xl">Win Probability: </h1>
    <h1 class="text-3xl font-semibold text-center">{betData.winProbability}</h1>
</div>