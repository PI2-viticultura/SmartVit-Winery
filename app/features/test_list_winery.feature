Feature: aptar requisicao feita no frontend e enviar ao microsservico winery atraves do BFF 
  Como Sistema, quero pegar os dados informados no frontend pelo administrador,
  e visualiza-los no meu servico.

  Context: O administrador ver as vinicolas cadastradas 
    Dado que os dados que foram resgistrados utilizem o servico atraves do BFF

    Scenario: Administrador visualiza as vinicolas cadastradas na aplicacao
        Given a pagina de gerenciar vinicolas
        When ele visualizar as vinicolas desejadas
        Then o bff requisita o microsservico desejado