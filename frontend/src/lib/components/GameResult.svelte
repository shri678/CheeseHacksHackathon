<script>
    export let teams;
    $: resultPromise = teams && getResult(teams);
    let result;
    async function getResult(teams) {
        await fetch("http://localhost:8000/results", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(teams),
        })
        .then((res) => res.json())
        .then((json) => {
            console.log(json);
            result = json;
        })
    }
</script>

<h1 class="text-2xl font-bold text-center">Expected Results</h1>
<h2 class="text-xl font-semibold text-center p-16">{result || "Loading..."}</h2>
