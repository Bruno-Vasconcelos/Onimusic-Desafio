# Onimusic desafio para estagio


## Sobre o projeto

 #### Criação de um sistema CRUD de aplicação web para a empresa ficticia MusicOni
 Nessa aplicação é possivel adicionar artistas, e em seguida asicionar musicas, dessesdeterminados artistas, a musica conta com infomações sobre o titulo, duração contabilizada em segundos, se ela foi publicada no Spoity, ou no Youtube e  o Artista que a produziu se ele já estiver no banco de dados, quanto ao artista, só pode ser adicionado pela interface do Admin e conta com as informações de nome e data que se juntou a empresa.

### Tecnologias ultilizadas 

- Python
- Django
- sqlite
- html

### Preparação e Instalação

- No terminal inicie um ambiente virtual atravez do comando ```virtualenv venv``` seguido de ```source venv/bin/activate```.
- Instale o Django atravez do "comando pip install django".
- Para criar o banco de dados insira o comando ```python manage.py makemigrations``` e depois ```python manage.py migrate```.
- Para ter acesso ao Admin é preciso criar um superusuario com o comando ```python manage.py createsuperuser```.
- Inicie o servidor com o comando ```python manage.py runserver``` e pegue o link do localhost.

### Execução
- primeiro acessando o endereço + /admin, temos acesso a criação de artistas atravez so superusuario.

 ![alt text](/onimusicdesafio/musiconi/images/admin_artist.png)
 
 - Esta é a tela inicial acessando apenas o ip fornecido pelo comando.

 ![alt text](/onimusicdesafio/musiconi/images/home_screen.png)
 
  - clicando em "Add New Song" temos acesso ao formulario para adicionar novas musicas.

 ![alt text](/onimusicdesafio/musiconi/images/create_form.png)
 
  - clicando em "Update" temos acesso a um formulario preenchido com a musica escolhida

 ![alt text](/onimusicdesafio/musiconi/images/update_form.png)
 
  - clicando em "Delete" temos acesso a uma pagina para ter certeza se a ação vai ser tomada

 ![alt text](/onimusicdesafio/musiconi/images/delete_screen.png)





