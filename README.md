# Desafio 1 - Análise de Crédito

## 🏦 Contexto

Você faz parte de uma equipe de dados da **CredAIR**, uma financeira fictícia que oferece empréstimos pessoais.

A empresa possui um histórico de propostas de crédito analisadas ao longo do tempo. Para cada proposta, estão disponíveis informações sobre o solicitante, suas características financeiras e as condições do empréstimo. Após o acompanhamento das propostas, a empresa também passou a ter informações sobre quais casos resultaram ou não em inadimplência.

A equipe de crédito deseja utilizar esse histórico para compreender melhor o comportamento da carteira e investigar se as informações disponíveis podem ser utilizadas para **identificar propostas com maior risco de inadimplência**.

Seu papel neste desafio é atuar como **cientista de dados**. A partir dos dados fornecidos, você deverá investigar o problema, preparar os dados, desenvolver um modelo e avaliar os resultados obtidos.

> **Importante:** os dados utilizados neste exercício são sintéticos e foram criados exclusivamente para fins educacionais. O cenário é fictício e inspirado em situações comuns de análise de crédito.

## 📊 Dados disponíveis

O arquivo `credito.csv` contém registros de propostas de empréstimo analisadas pela CredAIR.

Cada linha representa uma **proposta de crédito** e reúne informações sobre o perfil do solicitante, sua situação financeira e as características do empréstimo.

| Coluna               | Descrição                                                               |
| -------------------- | ----------------------------------------------------------------------- |
| `idade`              | Idade do solicitante no momento da proposta                             |
| `estado`             | Estado de residência do solicitante                                     |
| `escolaridade`       | Nível de escolaridade declarado pelo solicitante                        |
| `renda_mensal`       | Renda mensal declarada pelo solicitante, em reais                       |
| `tempo_emprego_anos` | Tempo, em anos, no emprego atual                                        |
| `score_credito`      | Pontuação utilizada para representar o perfil de crédito do solicitante |
| `valor_solicitado`   | Valor solicitado no empréstimo, em reais                                |
| `prazo_meses`        | Prazo solicitado para pagamento do empréstimo, em meses                 |
| `finalidade`         | Principal finalidade informada para o empréstimo                        |
| `dividas_ativas`     | Quantidade de dívidas atualmente em aberto                              |
| `inadimplente`       | Indica se a proposta resultou em inadimplência                          |

Os dados representam os **registros recebidos pela equipe de dados** e devem ser analisados antes de qualquer decisão sobre sua utilização na modelagem.

## 🎯 Desafio

A equipe da CredAIR precisa utilizar o histórico de propostas para compreender melhor os fatores relacionados à inadimplência e investigar se é possível utilizar as informações disponíveis para apoiar a identificação de propostas de maior risco.

A partir dos dados fornecidos, desenvolva uma análise que percorra as principais etapas de um projeto de Ciência de Dados e Machine Learning.

Não existe uma única forma correta de realizar todas as etapas. Suas escolhas devem ser justificadas de acordo com o problema e com as características dos dados.

### 1. Entendimento do problema

Analise o contexto apresentado e as variáveis disponíveis.

Você deverá:

* identificar a **variável resposta** do problema;
* explicar o que essa variável representa;
* caracterizar o problema de Machine Learning;
* justificar por que o problema pode ser tratado como um problema de **classificação**.

### 2. Análise exploratória

Investigue os dados antes de realizar a modelagem.

Sua análise deverá:

* apresentar as principais características dos dados;
* analisar a distribuição da variável resposta;
* investigar relações entre as variáveis e a inadimplência;
* destacar padrões ou comportamentos relevantes encontrados durante a análise.

Utilize tabelas, estatísticas e visualizações quando forem relevantes para sustentar suas conclusões.

### 3. Limpeza e preparação dos dados

Avalie a qualidade dos dados e realize os tratamentos necessários para utilizá-los nas etapas seguintes.

Você deverá:

* identificar problemas de qualidade nos dados;
* tratar valores ausentes;
* tratar inconsistências e valores inválidos;
* verificar e tratar duplicidades, quando necessário;
* adequar os tipos e formatos das variáveis;
* justificar as principais decisões tomadas.

### 4. Engenharia de atributos

Avalie se as variáveis disponíveis representam adequadamente o problema.

Você deverá:

* criar pelo menos **uma variável derivada** a partir das informações disponíveis;
* explicar como ela foi construída;
* explicar o que ela representa;
* justificar sua possível relação com a inadimplência;
* avaliar se ela será utilizada no modelo.

### 5. Preparação para modelagem

Prepare os dados para a construção do modelo.

Você deverá:

* definir as variáveis utilizadas na modelagem;
* realizar as transformações necessárias;
* preparar as variáveis categóricas, quando aplicável;
* separar os dados em treinamento e teste;
* realizar outras etapas de preparação necessárias para o modelo escolhido.

Explique as principais decisões tomadas durante essa etapa.

### 6. Modelagem

Desenvolva um modelo de **Regressão Logística** utilizando os dados preparados nas etapas anteriores.

Apresente:

* as variáveis utilizadas no modelo;
* o processo utilizado para treinamento;
* os resultados obtidos pelo modelo.

### 7. Avaliação e interpretação

Avalie o desempenho do modelo utilizando dados que não participaram do treinamento.

Você deverá:

* utilizar métricas adequadas para avaliar o modelo;
* comparar o desempenho obtido com uma referência simples;
* interpretar os resultados;
* analisar quais variáveis apresentam maior relação com o resultado previsto;
* discutir o que os resultados representam para o problema da CredAIR.

### 8. Conclusão

Finalize a análise apresentando as principais conclusões obtidas durante o desenvolvimento.

Sua conclusão deverá abordar:

* os principais padrões encontrados nos dados;
* os principais fatores relacionados à inadimplência;
* os resultados obtidos pelo modelo;
* as limitações da análise;
* possíveis cuidados para utilização desse tipo de modelo em uma situação real.

## 🎤 Apresentação

Além do notebook, você deverá apresentar o desenvolvimento do desafio.

A apresentação será realizada **via Microsoft Teams, em uma reunião individual com um dos monitores da trilha**.

O objetivo é apresentar a história da análise, desde o entendimento do problema até os resultados obtidos.

A apresentação deverá abordar:

* o problema e o objetivo da análise;
* as principais características dos dados;
* os principais problemas encontrados durante a preparação;
* as descobertas mais relevantes da análise exploratória;
* as principais decisões tomadas durante o desenvolvimento;
* o modelo desenvolvido;
* os resultados obtidos;
* as principais conclusões e limitações.

A apresentação deve demonstrar que você compreendeu as decisões tomadas durante o desenvolvimento, e não apenas apresentar os resultados finais.

## 📦 Entregáveis

### Notebook

Um notebook organizado e executável contendo todo o desenvolvimento da análise.

O notebook deverá:

* estar dividido em seções;
* apresentar código e resultados de forma organizada;
* conter explicações das principais decisões;
* permitir acompanhar o desenvolvimento desde os dados brutos até o modelo final;
* estar disponível em um **repositório pessoal no GitHub**.

O **link para o repositório do GitHub deverá ser disponibilizado junto à entrega**.

Antes da entrega, execute o notebook do início ao fim para garantir que todas as células sejam executadas corretamente.

### Apresentação

Uma apresentação contendo o desenvolvimento e os principais resultados do desafio.

A apresentação deverá ser realizada **via Microsoft Teams, em uma reunião individual com um dos monitores da trilha**, em data e horário definidos pela organização.

## 💻 Prática de Git e GitHub

A prática de **Git e GitHub faz parte deste desafio**.

Crie um repositório pessoal no GitHub para desenvolver e organizar sua solução.

Organize o desenvolvimento em commits que representem etapas relevantes do trabalho. Utilize **Conventional Commits** para descrever as alterações.

Por exemplo:

```text
feat: inicia analise dos dados
feat: realiza limpeza dos dados
feat: adiciona analise exploratoria
feat: cria atributos para o modelo
feat: desenvolve modelo
feat: adiciona avaliacao do modelo
docs: adiciona apresentacao
```

Você também pode criar commits para correções, ajustes na análise ou outras evoluções relevantes.

A organização do repositório e o histórico de commits fazem parte da prática proposta neste desafio.
