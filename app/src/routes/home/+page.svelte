<script>
    import { fade } from 'svelte/transition';
    import {onMount} from 'svelte';

    let cond = false

    onMount(()=>{
        cond = true
    })
</script>

{ #if cond}
    <h1 transition:fade>Skrr</h1>
{/if}