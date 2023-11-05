<script>
    export let player;
    export let onClose;
</script>

<style>
    .popout {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        z-index: 100;
    }
    .popout-arrow {
        content: "";
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translateX(-50%);
        width: 0;
        height: 0;
        border-left: 20px solid transparent;
        border-right: 20px solid transparent;
        border-top: 20px solid white;
    }
    .close-button {
        cursor: pointer;
        position: absolute;
        top: 10px;
        right: 10px;
    }
</style>

<div class="popout">
    <div class="popout-arrow"></div>
    <span class="close-button" on:click={onClose}>X</span>
    <p>Points: {player.stats.points}</p> 
    <p>Steals: {player.stats.steals}</p>
    <p>Rebounds: {player.stats.rebounds}</p>
    <!-- Add more stats here -->
</div>
