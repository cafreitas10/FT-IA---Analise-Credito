# 2. Análise Exploratória

## 2.1 Visão Geral dos Dados

O dataset possui **5.000 registros** e **11 colunas** (10 variáveis preditoras + 1 variável resposta). Não há valores ausentes em nenhuma coluna.

### Tipos das variáveis

| Coluna | Tipo | Categoria |
| --- | --- | --- |
| `idade` | int64 | Numérica |
| `estado` | object | Categórica |
| `escolaridade` | object | Categórica |
| `renda_mensal` | float64 | Numérica |
| `tempo_emprego_anos` | int64 | Numérica |
| `score_credito` | int64 | Numérica |
| `valor_solicitado` | float64 | Numérica |
| `prazo_meses` | int64 | Numérica |
| `finalidade` | object | Categórica |
| `dividas_ativas` | int64 | Numérica |
| `inadimplente` | int64 | Variável resposta |

### Estatísticas descritivas (variáveis numéricas)

| Variável | Mínimo | Média | Mediana | Máximo | Desvio Padrão |
| --- | --- | --- | --- | --- | --- |
| `idade` | 18 | 47,77 | 46 | 750 | 31,65 |
| `renda_mensal` | 100,00 | 5.228,63 | 4.146,30 | 44.814,19 | 3.968,48 |
| `tempo_emprego_anos` | 1 | — | — | 74 | — |
| `score_credito` | 335 | — | — | 850 | — |
| `valor_solicitado` | 1.721,48 | — | — | 50.000,00 | — |
| `prazo_meses` | 6 | — | — | 60 | — |
| `dividas_ativas` | 0 | 1,90 | 1 | 7 | 1,86 |

### Variáveis categóricas

| Variável | Valores únicos | Valores |
| --- | --- | --- |
| `escolaridade` | 4 | Ensino Fundamental, Ensino Médio, Ensino Superior, Pós-graduação |
| `finalidade` | 6 | Viagem, Outros, Reforma, Educação, Saúde, Veículo |
| `estado` | 85* | DF, SP, RJ, MG, ... (*ver seção 2.5 — problema de qualidade) |

## 2.2 Distribuição da Variável Resposta

A variável `inadimplente` apresenta a seguinte distribuição:

| Valor | Quantidade | Proporção |
| --- | --- | --- |
| 0 (adimplente) | 3.280 | 65,6% |
| 1 (inadimplente) | 1.720 | 34,4% |

Há um **desbalanceamento moderado**: a classe positiva (inadimplente) representa cerca de 34% dos registros, enquanto a classe negativa representa 66%. Esse desbalanceamento não é extremo, mas deve ser considerado na modelagem — métricas como acurácia podem ser enganosas, e técnicas como ajuste de limiar, ponderação de classes ou amostragem podem ser necessárias.

## 2.3 Relação entre Variáveis Numéricas e Inadimplência

### Correlações com a variável resposta

| Variável | Correlação com `inadimplente` | Interpretação |
| --- | --- | --- |
| `score_credito` | -0,3018 | **Mais forte** — quanto menor o score, maior a inadimplência |
| `renda_mensal` | -0,1887 | Maior renda → menor inadimplência |
| `dividas_ativas` | +0,1717 | Mais dívidas ativas → maior inadimplência |
| `valor_solicitado` | +0,1437 | Maior valor solicitado → maior inadimplência |
| `prazo_meses` | -0,1006 | Prazos maiores → ligeira redução na inadimplência |
| `tempo_emprego_anos` | -0,0837 | Mais tempo no emprego → menor inadimplência |
| `idade` | -0,0215 | Correlação muito fraca, praticamente nula |

### Análise de `dividas_ativas`

A variável `dividas_ativas` apresenta uma relação clara e monotônica com a inadimplência:

| Dívidas Ativas | Nº de Propostas | Taxa de Inadimplência |
| --- | --- | --- |
| 0 | 1.554 | 27,4% |
| 1 | 965 | 26,8% |
| 2 | 848 | 36,3% |
| 3 | 631 | 38,7% |
| 4 | 420 | 46,2% |
| 5 | 322 | 45,7% |
| 6 | 162 | 51,2% |
| 7 | 98 | 60,2% |

Observa-se que a taxa de inadimplência **dobra** quando o solicitante passa de 0-1 dívidas (~27%) para 6-7 dívidas (~51-60%). Propostas com 2 ou mais dívidas ativas apresentam risco significativamente elevado.

## 2.4 Relação entre Variáveis Categóricas e Inadimplência

### Por `escolaridade`

| Escolaridade | Nº de Propostas | Taxa de Inadimplência |
| --- | --- | --- |
| Ensino Fundamental | 411 | 32,4% |
| Ensino Médio | 2.061 | 36,0% |
| Ensino Superior | 1.938 | 33,4% |
| Pós-graduação | 590 | 33,7% |

A escolaridade apresenta **baixa variabilidade** na taxa de inadimplência (32% a 36%), sugerindo um poder preditivo limitado.

### Por `finalidade`

| Finalidade | Nº de Propostas | Taxa de Inadimplência |
| --- | --- | --- |
| Viagem | 494 | 32,4% |
| Educação | 709 | 33,3% |
| Outros | 941 | 33,7% |
| Veículo | 1.128 | 34,5% |
| Reforma | 1.117 | 34,9% |
| Saúde | 611 | 37,3% |

A finalidade também apresenta pouca variação (32% a 37%). Propostas para **Saúde** apresentam a maior taxa de inadimplência (37,3%), enquanto **Viagem** apresenta a menor (32,4%).

### Por `estado`

A variável `estado` apresenta **85 valores únicos** — muito acima dos 27 estados brasileiros esperados. Isso indica um **problema de qualidade** decorrente de espaços em branco inconsistentes (ex.: ` DF `, `  CE `, ` PA `). Antes de qualquer análise por estado, é necessário realizar a limpeza (strip de espaços). Após o tratamento, a análise por estado poderá ser refeita.

## 2.5 Problemas de Qualidade Identificados

Durante a análise exploratória, foram identificados os seguintes problemas de qualidade nos dados:

### 2.5.1 Idades inválidas

A variável `idade` possui **15 registros com valores acima de 100 anos**, chegando a um máximo de **750 anos**. Esses valores são claramente inválidos e precisam ser tratados na etapa de limpeza.

### 2.5.2 Inconsistência na variável `estado`

A variável `estado` apresenta **85 valores únicos** quando deveria ter no máximo 27 (unidades federativas do Brasil). O problema é causado por **espaços em branco** adicionados aos valores (ex.: ` DF `, `  CE `, ` PA `), gerando variações do mesmo estado como categorias distintas.

### 2.5.3 Duplicatas

Foram encontradas **19 linhas duplicadas** no dataset, que devem ser removidas para evitar viés na modelagem.

### 2.5.4 Possíveis outliers em `tempo_emprego_anos`

O valor máximo é **74 anos** de tempo de emprego. Embora não seja impossível, é altamente improvável e merece investigação, especialmente considerando que existem registros com idades avançadas (potencialmente ligados aos outliers de idade).

## 2.6 Padrões e Comportamentos Relevantes

1. **Score de crédito é o maior preditor**: apresenta a correlação mais forte com a inadimplência (-0,30), indicando que solicitantes com menor score têm maior propensão à inadimplência.

2. **Dívidas ativas têm impacto direto e cumulativo**: a taxa de inadimplência aumenta de forma aproximadamente monotônica com o número de dívidas ativas, passando de ~27% (0-1 dívidas) para ~60% (7 dívidas).

3. **Renda mensal como fator de proteção**: maior renda está associada a menor inadimplência (correlação de -0,19).

4. **Valor solicitado eleva o risco**: propostas com valores maiores tendem a ter maior inadimplência (correlação de +0,14).

5. **Variáveis categóricas têm baixo poder discriminativo**: `escolaridade` e `finalidade` apresentam pouca variação na taxa de inadimplência entre categorias, sugerindo contribuição marginal limitada para o modelo.

6. **Idade tem relação quase nula**: a correlação com inadimplência é praticamente zero (-0,02), indicando que a idade por si só não é um bom preditor.

7. **Desbalanceamento moderado da variável resposta**: 34% de inadimplentes vs. 66% de adimplentes — deve ser considerado na escolha de métricas e técnicas de modelagem.

8. **Problemas de qualidade exigem tratamento antes da modelagem**: idades inválidas, inconsistências em `estado` e duplicatas devem ser resolvidas na etapa de limpeza.