Feature: criar requisicao e enviar os dados do sensor ao microsservico winery atraves do BFF 
  Como sistema, quero registrar um sensor na aplicacao atraves,
  e armazenar no meu servico.

  Context: O administrador criar os sensores na aplicacao
    Dado que os dados sejam resgistrados e utilizem o servico atraves do BFF

    Scenario: Administrador cadastra os sensores na aplicacao
        Given a pagina de criar novo sensor
        When ele regista novo conteudo do sensor da solicitacao
        Then o bff requisita o microsservico para criar informacao do sensor