<h1>Projeto de estudo com Django</h1>
<hr>
<p>
  O projeto consiste basicamente em uma rede social básica, onde o usuario pode se logar com username e senha, e criar posts de texto que serão visíveis para todos os outros usuarios.
  <br>
  <br>
  <b>Funcionalidades:</b>
  <br>
  <br>
  Usuario/Conta
  <ul>
    <li>Criar conta/usuario</li>
    <li>Editar conta/usuario</li>
    <li>Apagar conta/usuario</li>
    <li>Visualizar perfil/conta/usuario</li>
  </ul>
  <br>
  Post
  <ul>
    <li>Criar Post</li>
    <li>Ver todos os post</li>
    <li>Ver post especifico</li>
  </ul>
  <br>
  Login
  <ul>
    <li>Realizar login</li>
    <li>Realizar logout</li>
  </ul>
  <p>
    Todas as rotas sao protegidas por um token de autenticacao.
    Esse token é gerado durante o login do usuario, que junto com a rota de criação de usuarios, é "aberta" para qualquer um acessar.
  </p>
</p>
<hr>
<p>Na parte do backend (api) o sistema foi desenvolvido utilizando django, tecnologia que usa a linguagem python para que possam ser desenvolvidos apis restful</p>
<p>Na parte do frontend o sistema foi desenvolvido com a tecnologia svelte, framework que utiliza javascript</p>
