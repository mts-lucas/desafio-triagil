# Desafio Triagil
Repositório dedicado ao desafio técnico para admissão como estagiario backend na empresa Triagil


<h2>Executando o projeto sem docker</h2>

<p>Para rodar o projeto, siga as etapas abaixo:</p>

<ol>

<li>Crie um ambiente virtual para isolar as dependências do projeto:</li>
    <pre>python -m venv venv</pre>

<li>Ative o ambiente virtual:</li>
<ul>
    <li>No Windows:</li>
    <pre>venv\Scripts\activate</pre>
    <li>No Linux/MacOS:</li>
    <pre>source venv/bin/activate</pre>
</ul>

<li>Instale as dependências do projeto:</li>
<pre>pip install -r requirements.txt</pre>

<li>Gere sua SECRET_KEY a partir do seguinte comando no terminal:</li>
<pre>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
</pre>

<li>Crie um arquivo .env na raiz do diretório do projeto, copie o conteudo de .env.example e adicione sua SECRET_KEY:</li>
<pre>SECRET_KEY='your-secret-key-here'</pre>

<li>Faça as migrações do banco de dados:</li>
<pre>python manage.py migrate</pre>


<li>Inicie o servidor de desenvolvimento:</li>
<pre>python manage.py runserver</pre>

<li>Abra o navegador e acesse o endereço http://localhost:8000 para acessar a aplicação.</li>
</ol>


<h2>Diagrama de entidade relacionamento</h2>

```mermaid

    erDiagram
        POKEMON {

            int id PK
            int dex_id UK
            string(32) name
            int weight
            int height
        }

        TEAM {

            int id PK
            string(32) owner

        }
        TEAM_POKEMONS {
            int pokemonID PK, FK
            int TeamID PK, FK
        }

        POKEMON ||--o{ TEAM_POKEMONS : esta_em
        TEAM ||--o{ TEAM_POKEMONS : tem

```

<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.</p>
