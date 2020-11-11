Feature: aptar requisicao feita no frontend e enviar informacoes do sensor ao microsservico winery atraves do BFF 
  Como Sistema, quero pegar os dados informados no frontend pelo administrador,
  e visualiza-los no meu servico.

  Context: O administrador ver os sistemas cadastrados 
    Dado que os dados que foram resgistrados utilizem o servico atraves do BFF

    Scenario: Administrador visualiza os sistemas cadastradas na aplicacao
        Given a pagina de gerenciar sistemas
        When ele visualizar os sistemas desejados
        Then o bff requisita o microsservico do sistema