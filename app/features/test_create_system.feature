Feature: criar requisicao e enviar os dados do sistema ao microsservico winery atraves do BFF 
  Como Sistema, quero registrar um sistema na aplicacao atraves,
  e armazenar no meu servico.

  Context: O administrador criar os sistemas na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os sistemas na aplicacao
        Given a pagina de criar novo sistema
        When ele regista novo conteudo do sistema da solicitacao
        | latitude | longitude | status     | winery_id                |
        | 1454.55  | 154895.12 | Desativado | 5fa0c880d578d4bc349dc376 |
        Then confirma se a listagem do cadastro do sistema foi pega
        | latitude | longitude | status     | winery_id                |
        | 1454.55  | 154895.12 | Desativado | 5fa0c880d578d4bc349dc376 |