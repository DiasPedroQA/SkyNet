# SkyNet Backend

Este é o backend do projeto SkyNet, uma aplicação FastAPI que permite a leitura de arquivos HTML e o gerenciamento de links de favoritos.

## Estrutura do Projeto

A estrutura do backend é organizada da seguinte forma:

```
backend/
├── app/
│   ├── main.py                # Ponto de entrada da aplicação FastAPI
│   ├── core/
│   │   ├── config.py          # Configurações da aplicação
│   │   └── security.py        # Lógica de segurança (autenticação e autorização)
│   ├── api/
│   │   └── v1/
│   │       ├── __init__.py    # Inicialização do pacote da API v1
│   │       ├── deps.py        # Dependências injetáveis nas rotas
│   │       ├── routers/
│   │       │   └── favorites.py # Rotas relacionadas aos favoritos
│   │       └── schemas/
│   │           └── favorite.py # Esquemas de dados para validação
│   ├── models/
│   │   └── favorite.py        # Modelo de dados para favoritos
│   ├── services/
│   │   └── favorite_service.py # Lógica de negócios para favoritos
│   ├── repositories/
│   │   └── favorite_repo.py   # Acesso a dados para favoritos
│   └── db/
│       ├── session.py         # Configuração da sessão do banco de dados
│       └── base.py            # Base para os modelos do banco de dados
├── tests/
│   ├── unit/
│   │   └── test_favorite_service.py # Testes unitários para serviços de favoritos
│   ├── integration/
│   │   └── test_api_favorites.py   # Testes de integração para a API de favoritos
│   └── conftest.py             # Configuração de fixtures para testes
├── pyproject.toml              # Configuração do projeto Python
├── requirements.txt            # Dependências do projeto
├── alembic.ini                 # Configuração para migrações de banco de dados
└── README.md                   # Documentação do backend
```

## Como Executar

1. **Instalação das Dependências**: Utilize o arquivo `requirements.txt` para instalar as dependências necessárias.
   
   ```
   pip install -r requirements.txt
   ```

2. **Executar a Aplicação**: Utilize o comando abaixo para iniciar a aplicação FastAPI.

   ```
   uvicorn app.main:app --reload
   ```

3. **Testes**: Para executar os testes, utilize o comando:

   ```
   pytest
   ```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e correções. Para isso, crie uma nova branch e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.