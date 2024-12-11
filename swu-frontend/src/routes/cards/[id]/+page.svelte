<script>
    import { CardStore } from '../../../card-store.js';
    import { onMount } from 'svelte'

    export let data;

    let card;
    onMount(async function() {
        if($CardStore.length) {
            card = $CardStore.find(card => card.id == data.id)
        }
        else {
            let endpoint = `http://localhost:8000/api/cards/${data.id}`
            let response = await fetch(endpoint)
            if(response.status == 200) {
                card = await response.json()
            }
            else {
                card = null
            }
        }
    })
</script>

<div class="row nt-4">
    {#if card }
    <h2 class="mb-4">{ card.name }</h2>
    <div class="col-8 col-md-4">
        <img src="{card.frontimage}" alt="Film" class="w-100"/>
    </div>
    <div class="col-4 col-md-4">
        <p>{ card.fronttext }</p>
    </div>
    {:else }
        <p> No Card was found with ID {data.id}</p>
    {/if}
</div>