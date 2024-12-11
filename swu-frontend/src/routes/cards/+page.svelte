<script>
    import {CardStore} from '../../card-store'
    import {onMount} from 'svelte'

    onMount(async function () {
        if(!$CardStore.length) {
        const endpoint = 'http://localhost:8000/api/cards/'
        const response = await fetch(endpoint)
        const data = await response.json()
        CardStore.set(data)
        }
    })
</script>

<div>
    <h2 class="my-4">Card List</h2>
    
    <div class="my-4 row">
        {#each $CardStore as card}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="card w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="{card.frontimage}" 
                    alt="Card">
                <div class="card-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="card-title">{ card.name }</h5>
                        <p class="card-subtitle">{ card.subtitle }</p>
                    </div>
                    <div>
                        <a href="/cards/{card.id}" class="btn btn-primary">View</a>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>