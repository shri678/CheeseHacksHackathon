<script>
    import Roster from '$lib/components/Roster.svelte'
    import Bet from '$lib/components/Bet.svelte'
</script>

<main class="flex justify-between h-screen items-center">
    <div class="flex-1 border p-4 h-full">
        <Roster/>
    </div>
    <div class="flex-1 border p-4 h-1/3">
        <Bet/>
    </div>
    <div class="flex-1 border p-4 h-full">
        <Roster/>
    </div>
</main>
