<script>
    export let teamNames;
    $: resultPromise = teamNames.length === 2 && getResult(teamNames);
    let result;
    async function getResult(teams) {
        await fetch("http://localhost:8000/results", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                team1: teams[0],
                team2: teams[1],
            }),
        })
        .then((res) => res.json())
        .then((json) => {
            console.log(json);
            result = json;
        })
    }
</script>

<h1 class="text-2xl font-bold text-center">Expected Results</h1>
<h2 class="text-2xl font-semibold text-center p-16">{result || "Loading..."}</h2>
