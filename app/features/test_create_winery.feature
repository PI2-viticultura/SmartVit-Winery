Feature: criar requisicao e enviar ao microsservico winery atraves do BFF 
  Como Sistema, quero registrar uma vinicola na aplicacao atraves,
  e armazenar no meu servico.

  Context: O administrador criar as vinicolas na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra as vinicolas na aplicacao
        Given a pagina de criar nova vinicola
        When ele regista novo conteudo da solicitacao
        | name                 | address              | contract_id              |
        | Vinicola dos Alveres | Fazendas do Sul - RS | 5f87a04fff9628aaeeea43a9 |
        Then o bff requisita o microsservico para criar informacao
        | name                 | address              | contract_id              |
        | Vinicola dos Alveres | Fazendas do Sul - RS | 5f87a04fff9628aaeeea43a9 |