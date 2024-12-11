<script>
    import {SetStore} from '../../set-store'
    import {onMount} from 'svelte'

    onMount(async function () {
        if(!$SetStore.length) {
        const endpoint = 'http://localhost:8000/api/sets/'
        const response = await fetch(endpoint)
        const data = await response.json()
        SetStore.set(data)
        }
    })
</script>


<div>
    <h2 class="my-4">Set List</h2>
    
    <div class="my-4 row">
        {#each $SetStore as set}
        <div class="col-12 col-sm-6 col-md-4">
            
            <div class="set w-100 h-100">
                <img class="card-img-top" style="height: 300px; object-fit: cover" 
                    src="" 
                    alt="Set">
                <div class="set-body d-flex flex-column justify-content-between gap-4">
					<div>
                        <h5 class="set-title">{ set.name }</h5>
                    </div>
                    <div>
                        <a href="/{set.setcode}" class="btn btn-primary">View</a>
					</div>
                </div>
              </div>

        </div>
        {/each}
    </div>
    
</div>