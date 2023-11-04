<!-- Scripts para reatividade e hooks de inicializacao -->
<script>
    // svelte animations
    import { fade } from 'svelte/transition';
    import {onMount} from 'svelte';
    import axios from 'axios'


    let username = ''
    let password = ''
    async function fazerLogin(){
        await axios.post("http://127.0.0.1:8000/login/",{
            "username": username,
            "senha": password
        }).then((res) => console.log(res.data))
    }    

</script>

<!-- Corpo em html -->
<div class="flex flex-row py-12 px-24 items-center justify-center h-screen">
    <div class="flex flex-row w-full h-full justify-center 
            items-center gap-3 rounded-lg shadow-lg bg-purple-300">
        <div class="flex flex-col gap-4 p-2 w-full">
                <h2 class="text-center uppercase text-xl">
                    Entre agora
                </h2>
            <input class='input-text rounded-sm' type="text" bind:value={username} />
            <input class='input-text rounded-sm' type="password" bind:value={password} />
            <button class='btn tracking-wide uppercase rounded-sm bg-purple-900 text-white' on:click={fazerLogin}>Login</button>
            <div class="flex flex-row gap-2">
                <a href="/registrar" class="text-sm">criar conta</a>
                <a href="/home" class="text-sm">github</a>
            </div>
        </div>
        <div class="bg-gradient-to-b from-purple-600 to-purple-900 rounded-lg w-full h-full"></div>
    </div>
</div>

<!-- Estilos customzados da pagina -->
<style>
    .input-text{
        height: 2rem;
    }
    .btn{
        height: 3rem;
        transition: all .2 ease;
    }
</style>