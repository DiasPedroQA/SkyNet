# Frontend Documentation for SkyNet

Este diretório contém a aplicação frontend do projeto SkyNet, que é construída utilizando React e TypeScript. Abaixo estão as informações sobre a estrutura do projeto e como configurar e executar a aplicação.

## Estrutura do Projeto

```
frontend
├── src
│   ├── index.tsx                # Ponto de entrada da aplicação React
│   ├── app
│   │   ├── components            # Componentes reutilizáveis da aplicação
│   │   │   └── FavoriteList.tsx  # Componente que exibe a lista de favoritos
│   │   ├── pages                 # Páginas da aplicação
│   │   │   └── Dashboard.tsx     # Página principal do aplicativo
│   │   └── services              # Serviços para interagir com a API
│   │       └── api.ts            # Funções para chamadas à API do backend
│   └── tests                     # Testes da aplicação
│       └── App.test.tsx         # Testes para o aplicativo frontend
├── public
│   └── index.html                # HTML principal que carrega a aplicação React
├── package.json                  # Configuração do npm, incluindo dependências e scripts
├── tsconfig.json                 # Configuração do TypeScript
├── jest.config.js                # Configuração do Jest para testes
├── cypress
│   └── integration
│       └── e2e_spec.ts           # Testes de ponta a ponta utilizando Cypress
└── README.md                     # Documentação do frontend
```

## Configuração do Ambiente

1. **Instalação de Dependências**: Navegue até o diretório `frontend` e execute o seguinte comando para instalar as dependências:

   ```
   npm install
   ```

2. **Executar a Aplicação**: Após a instalação das dependências, você pode iniciar a aplicação com o comando:

   ```
   npm start
   ```

   A aplicação estará disponível em `http://localhost:3000`.

## Testes

Para executar os testes, utilize o comando:

```
npm test
```

Isso executará os testes unitários e de integração definidos na pasta `tests`.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, crie um fork do repositório, faça suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.