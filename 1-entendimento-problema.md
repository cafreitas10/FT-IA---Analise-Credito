# 1. Entendimento do Problema

## 1.1 Contexto

A **CredAIR** é uma financeira fictícia que oferece empréstimos pessoais. A empresa possui um histórico de propostas de crédito analisadas ao longo do tempo, contendo informações sobre o solicitante, suas características financeiras e as condições do empréstimo. Após o acompanhamento dessas propostas, a empresa passou a ter informações sobre quais casos resultaram ou não em inadimplência.

A equipe de crédito deseja utilizar esse histórico para compreender melhor o comportamento da carteira e investigar se as informações disponíveis podem ser utilizadas para **identificar propostas com maior risco de inadimplência**.

## 1.2 Variável Resposta

A variável resposta do problema é **`inadimplente`**.

Essa variável é do tipo binária e indica se uma proposta de crédito resultou em inadimplência:

| Valor | Significado |
| --- | --- |
| `0` | A proposta **não** resultou em inadimplência (cliente pagou o empréstimo conforme acordado) |
| `1` | A proposta **resultou** em inadimplência (cliente não cumpriu as obrigações de pagamento) |

A variável resposta foi obtida a partir do acompanhamento posterior das propostas, ou seja, representa o **desfecho observado** de cada solicitação de crédito.

## 1.3 Caracterização do Problema de Machine Learning

Este é um problema de **aprendizado supervisionado**, pois:

- Os dados de treinamento contêm **exemplos rotulados** — cada proposta possui um valor conhecido para a variável `inadimplente` (0 ou 1);
- O objetivo é **aprender um mapeamento** entre as características da proposta (variáveis preditoras) e o desfecho (variável resposta);
- O modelo treinado será utilizado para **prever** a probabilidade de inadimplência de novas propostas.

## 1.4 Justificativa: Problema de Classificação

O problema pode ser tratado como **classificação binária** pelos seguintes motivos:

1. **A variável resposta é categórica e discreta**: assume apenas dois valores possíveis (0 ou 1), representando duas classes mutuamente exclusivas — adimplente e inadimplente.

2. **O objetivo é atribuir um rótulo**: dado um conjunto de características de uma nova proposta, deseja-se classificá-la em uma das duas categorias: *propensa à inadimplência* ou *não propensa à inadimplência*.

3. **Não se trata de prever um valor contínuo**: o desfecho não é uma quantidade numérica a ser estimada (como um valor de perda), mas sim uma **categoria** a ser atribuída. Isso distingue o problema de regressão, onde a variável resposta seria contínua.

4. **Aplicação prática direta**: a classificação permite que a CredAIR utilize a saída do modelo como apoio à decisão de aprovação ou recusa de novas propostas, bem como para definir condições diferenciadas (taxas, limites) conforme o risco estimado.

## 1.5 Variáveis Preditoras Disponíveis

As variáveis disponíveis para prever a inadimplência são:

| Coluna | Tipo | Descrição |
| --- | --- | --- |
| `idade` | Numérica | Idade do solicitante no momento da proposta |
| `estado` | Categórica | Estado de residência do solicitante |
| `escolaridade` | Categórica | Nível de escolaridade declarado |
| `renda_mensal` | Numérica | Renda mensal declarada, em reais |
| `tempo_emprego_anos` | Numérica | Tempo no emprego atual, em anos |
| `score_credito` | Numérica | Pontuação de crédito do solicitante |
| `valor_solicitado` | Numérica | Valor solicitado no empréstimo, em reais |
| `prazo_meses` | Numérica | Prazo de pagamento solicitado, em meses |
| `finalidade` | Categórica | Finalidade informada para o empréstimo |
| `dividas_ativas` | Numérica | Quantidade de dívidas em aberto |

Essas variáveis serão investigadas na etapa de análise exploratória para entender suas relações com a variável resposta e seu potencial preditivo.