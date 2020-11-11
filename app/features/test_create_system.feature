Feature: criar requisicao e enviar os dados do sistema ao microsservico winery atraves do BFF 
  Como Sistema, quero registrar um sistema na aplicacao atraves,
  e armazenar no meu servico.

  Context: O administrador criar os sistemas na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os sistemas na aplicacao
        Given a pagina de criar novo sistema
        When ele regista novo conteudo do sistema da solicitacao
        Then o bff requisita o microsservico para criar informacao do sistema