<!-- Scripts para reatividade e hooks de inicializacao -->
<script>

    import ValidationInput from '../lib/helpers/validationInput.js'
    import AlertShow from '../lib/helpers/alertShowers.js'
    import ConnRequest from '../lib/helpers/connectionFactory.js' 

    // dados de login
    var loginData = {
        username: '',
        senha: ''
    }

    // funcao que executa o login
    async function fazerLogin(){

        if(!ValidationInput.notEmpty(loginData.username) || !ValidationInput.notEmpty(loginData.senha)){

            return AlertShow.errorAlert("Campos não podem estar vazios")
        }

        let dataResponse = await ConnRequest.postRequest("http://127.0.0.1:8000/login/", loginData)

        if(dataResponse.status){

            return AlertShow.successAlert().then(()=>{
                window.location.href='/home'
            })
        }
        return AlertShow.errorAlert()
    }

</script>

<!-- Corpo em html -->
<div class="flex flex-row py-12 px-24 items-center justify-center h-screen 
        bg-gradient-to-b from-purple-100 via-indigo-200 to-violet-200"
        on:keydown={(event)=> {
            if(event.key == 'Enter') fazerLogin()
        }} role='presentation'>

    <div class="flex flex-row w-full h-full justify-center 
            items-center gap-3 rounded-l-lg shadow-lg bg-slate-100 ">

        <div class="flex flex-col gap-4 p-2 w-full">
            <h2 class="title text-center uppercase text-xl">
                Acesse agora
            </h2>

            <input placeholder="username" class='input-text rounded-md' type="text" bind:value={loginData.username} />
            <input placeholder="senha" class='input-text rounded-md' type="password" bind:value={loginData.senha} />

            <button class='btn tracking-wide uppercase rounded-md text-white' 
                on:click={fazerLogin} >
                Entrar
            </button>

            <div class="flex flex-col items-center gap-2">
                <a href="/cadastrar" class="text-sm font-medium underline">criar conta</a>
            </div>
        </div>

        <div class="img-bg flex flex-col justify-center items-center rounded-r-lg w-full h-full">
            <img class="" src="./oceano.png" alt='img' width="456" height="456"/>
        </div>
    </div>
</div>

<!-- Estilos customzados da pagina -->
<style>
    .img-bg{
        background-color: #514BBF;
    }
    .title::after{
        content: '';
        height: 1px;
        width: 30%;
        margin: auto;
        margin-top: 0.5rem;
        display: block;
        background-color: #1E293B;
    }
    .input-text{
        padding: 1rem;
        height: 3rem;
        border: 1px solid #1E293B;
    }
    .btn{
        background-color: #514BBF;
        height: 3rem;
        transition: all .2 ease;
    }
    .btn:hover{
        transition: all .4s ease;
        background-color: #645cff;
    }
</style>