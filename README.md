# SkyNet

SkyNet é um aplicativo que permite a leitura de arquivos HTML provenientes de navegadores, com links de favoritos salvos por um usuário, para acompanhar sua navegação e obter dados.

## Estrutura do Projeto

O projeto é dividido em duas partes principais: **backend** e **frontend**.

### Backend

O backend é construído utilizando FastAPI e possui a seguinte estrutura:

- **app**: Contém a lógica da aplicação.
  - **main.py**: Ponto de entrada da aplicação FastAPI.
  - **core**: Configurações e segurança da aplicação.
    - **config.py**: Configurações da aplicação.
    - **security.py**: Lida com autenticação e autorização.
  - **api**: Define as rotas da API.
    - **v1**: Versão 1 da API.
      - **deps.py**: Dependências injetáveis nas rotas.
      - **routers**: Contém as rotas da API.
        - **favorites.py**: Rotas relacionadas aos favoritos.
      - **schemas**: Modelos Pydantic para validação de dados.
        - **favorite.py**: Esquemas de dados para favoritos.
  - **models**: Define os modelos de dados.
    - **favorite.py**: Modelo de dados para favoritos.
  - **services**: Lógica de negócios.
    - **favorite_service.py**: Manipulação de dados e interações com o repositório.
  - **repositories**: Acesso a dados.
    - **favorite_repo.py**: Operações de banco de dados para favoritos.
  - **db**: Configuração do banco de dados.
    - **session.py**: Gerencia a conexão do banco de dados.
    - **base.py**: Define a base para os modelos do banco de dados.

- **tests**: Contém os testes da aplicação.
  - **unit**: Testes unitários.
    - **test_favorite_service.py**: Testes para os serviços de favoritos.
  - **integration**: Testes de integração.
    - **test_api_favorites.py**: Testes para as rotas da API de favoritos.
  - **conftest.py**: Configuração de fixtures para os testes.

- **pyproject.toml**: Configuração do projeto Python.
- **requirements.txt**: Lista de dependências do projeto.
- **alembic.ini**: Configuração para migrações de banco de dados.
- **README.md**: Documentação do backend.

### Frontend

O frontend é construído utilizando React e possui a seguinte estrutura:

- **src**: Contém o código-fonte da aplicação.
  - **index.tsx**: Ponto de entrada da aplicação React.
  - **app**: Estrutura da aplicação.
    - **components**: Componentes React.
      - **FavoriteList.tsx**: Componente que exibe a lista de favoritos.
    - **pages**: Páginas da aplicação.
      - **Dashboard.tsx**: Página principal do aplicativo.
    - **services**: Interação com a API do backend.
      - **api.ts**: Funções para interagir com a API.
  - **tests**: Testes para o aplicativo frontend.
    - **App.test.tsx**: Testes para o aplicativo.

- **public**: Contém arquivos públicos.
  - **index.html**: HTML principal que carrega a aplicação React.

- **package.json**: Configuração do npm para o frontend.
- **tsconfig.json**: Configuração do TypeScript para o frontend.
- **jest.config.js**: Configuração do Jest para testes no frontend.
- **cypress**: Testes de ponta a ponta.
  - **integration**: Testes de integração com Cypress.
    - **e2e_spec.ts**: Testes de ponta a ponta.

- **README.md**: Documentação do frontend.

### Outros Arquivos

- **.github/workflows/ci.yml**: Fluxo de trabalho de integração contínua.
- **docker-compose.yml**: Configuração dos serviços do Docker.
- **Makefile**: Comandos para facilitar a execução de tarefas.
- **.gitignore**: Arquivos e pastas a serem ignorados pelo Git.
- **README.md**: Documentação geral do projeto.