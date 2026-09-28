# Databricks notebook source
# DBTITLE 1,3. Limpeza e Preparação dos Dados
# MAGIC %md
# MAGIC # 3. Limpeza e Preparação dos Dados
# MAGIC
# MAGIC Nesta etapa, avaliamos a qualidade dos dados e realizamos os tratamentos necessários para utilizá-los nas etapas seguintes do projeto.
# MAGIC
# MAGIC As principais atividades desta seção são:
# MAGIC
# MAGIC - **Identificar** problemas de qualidade nos dados;
# MAGIC - **Tratar** valores ausentes;
# MAGIC - **Tratar** inconsistências e valores inválidos;
# MAGIC - **Verificar e tratar** duplicidades;
# MAGIC - **Adequar** os tipos e formatos das variáveis;
# MAGIC - **Justificar** as principais decisões tomadas.
# MAGIC
# MAGIC Os dados utilizados são sintéticos e foram criados exclusivamente para fins educacionais, representando propostas de crédito da financeira fictícia **CredAIR**.

# COMMAND ----------

# DBTITLE 1,Carregamento do dataset
import pandas as pd
import numpy as np

# Carregamento do dataset
df = pd.read_csv('/Workspace/Users/cafreitas@gmail.com/Repos/FT-IA---Analise-Credito/dataset.csv')

print(f"Dimensões originais: {df.shape}")
df.head(10)

# COMMAND ----------

# DBTITLE 1,Identificação de Problemas de Qualidade
# MAGIC %md
# MAGIC ## 3.1 Identificação de Problemas de Qualidade
# MAGIC
# MAGIC Antes de qualquer tratamento, é fundamental diagnosticar os problemas presentes nos dados. A análise exploratória anterior já sinalizou alguns problemas; aqui faremos a verificação sistemática.
# MAGIC
# MAGIC ### Problemas identificados na análise exploratória
# MAGIC
# MAGIC 1. **Valores ausentes**: verificar se há registros faltantes em qualquer coluna;
# MAGIC 2. **Duplicatas**: verificar se existem linhas idênticas (a análise anterior encontrou 19 duplicatas);
# MAGIC 3. **Inconsistência em `estado`**: a variável apresenta 85 valores únicos quando deveria ter no máximo 27, devido a espaços em branco irregulares (ex.: ` DF `, `  CE `, ` PA `);
# MAGIC 4. **Idades inválidas**: existem 15 registros com idade superior a 100 anos, chegando a um máximo de 750 anos;
# MAGIC 5. **Possível inconsistência em `tempo_emprego_anos`**: valor máximo de 74 anos, que pode estar associado aos registros de idade inválida;
# MAGIC 6. **Tipos de variáveis**: verificar se as colunas categóricas e numéricas estão com os tipos adequados.

# COMMAND ----------

# DBTITLE 1,Verificação sistemática de problemas
# --- 1. Valores ausentes ---
print("=== VALORES AUSENTES ===")
print(df.isnull().sum())
print(f"\nTotal de valores ausentes: {df.isnull().sum().sum()}")

# --- 2. Duplicatas ---
print(f"\n=== DUPLICATAS ===")
print(f"Linhas duplicadas: {df.duplicated().sum()}")

# --- 3. Inconsistência em 'estado' ---
print(f"\n=== VALORES ÚNICOS EM 'estado' ===")
print(f"Total de valores únicos: {df['estado'].nunique()}")
print(f"Valores únicos: {df['estado'].unique().tolist()}")

# --- 4. Idades inválidas ---
print(f"\n=== IDADES INVÁLIDAS ===")
print(f"Idade mínima: {df['idade'].min()}")
print(f"Idade máxima: {df['idade'].max()}")
print(f"Registros com idade > 100: {(df['idade'] > 100).sum()}")
print(f"Registros com idade > 120: {(df['idade'] > 120).sum()}")
print("\nDistribuição de idades > 100:")
print(df.loc[df['idade'] > 100, 'idade'].value_counts().sort_index())

# --- 5. Tempo de emprego ---
print(f"\n=== TEMPO_EMPREGO_ANOS ===")
print(f"Mínimo: {df['tempo_emprego_anos'].min()}")
print(f"Máximo: {df['tempo_emprego_anos'].max()}")
print(f"Registros com tempo > 50: {(df['tempo_emprego_anos'] > 50).sum()}")

# Verificar se os outliers de tempo_emprego estão associados a idades inválidas
print("\nRegistros com tempo_emprego > 50:")
print(df.loc[df['tempo_emprego_anos'] > 50, ['idade', 'tempo_emprego_anos']])

# --- 6. Tipos das variáveis ---
print(f"\n=== TIPOS DAS VARIÁVEIS ===")
print(df.dtypes)

# --- 7. Valores únicos das variáveis categóricas ---
print(f"\n=== VALORES ÚNICOS - ESCOLARIDADE ===")
print(df['escolaridade'].unique().tolist())
print(f"\n=== VALORES ÚNICOS - FINALIDADE ===")
print(df['finalidade'].unique().tolist())

# --- 8. Variável resposta ---
print(f"\n=== DISTRIBUIÇÃO DA VARIÁVEL RESPOSTA ===")
print(df['inadimplente'].value_counts())
print(df['inadimplente'].value_counts(normalize=True).round(4) * 100)

# COMMAND ----------

# DBTITLE 1,Tratamento de Duplicatas
# MAGIC %md
# MAGIC ## 3.2 Tratamento de Duplicatas
# MAGIC
# MAGIC Foram identificadas **19 linhas duplicadas** no dataset. Duplicatas podem enviesar o modelo, pois o mesmo registro aparece mais de uma vez, dando peso desproporcional a certas observações durante o treinamento.
# MAGIC
# MAGIC **Decisão:** Remover as linhas duplicadas, mantendo apenas a primeira ocorrência de cada registro.

# COMMAND ----------

# DBTITLE 1,Remoção de duplicatas
# Remoção de duplicatas, mantendo a primeira ocorrência
n_antes = df.shape[0]
df = df.drop_duplicates(keep='first').reset_index(drop=True)
n_depois = df.shape[0]

print(f"Registros antes: {n_antes}")
print(f"Registros depois: {n_depois}")
print(f"Duplicatas removidas: {n_antes - n_depois}")

# COMMAND ----------

# DBTITLE 1,Tratamento da Variável estado
# MAGIC %md
# MAGIC ## 3.3 Tratamento da Variável `estado`
# MAGIC
# MAGIC A variável `estado` apresenta **85 valores únicos** quando deveria ter no máximo 27 (unidades federativas do Brasil). O problema é causado por **espaços em branco** adicionados irregularmente aos valores (ex.: ` DF `, `  CE `, ` PA `), criando variações do mesmo estado como categorias distintas.
# MAGIC
# MAGIC **Decisão:** Aplicar `strip()` para remover espaços em branco no início e no fim de cada valor, normalizando a variável para as 27 unidades federativas esperadas.

# COMMAND ----------

# DBTITLE 1,Normalização da variável estado
# Remoção de espaços em branco no início e fim dos valores de 'estado'
print(f"Valores únicos antes: {df['estado'].nunique()}")

df['estado'] = df['estado'].str.strip()

print(f"Valores únicos depois: {df['estado'].nunique()}")
print(f"Estados: {sorted(df['estado'].unique().tolist())}")

# COMMAND ----------

# DBTITLE 1,Tratamento de Idades Inválidas
# MAGIC %md
# MAGIC ## 3.4 Tratamento de Idades Inválidas
# MAGIC
# MAGIC A variável `idade` contém **15 registros com valores acima de 100 anos**, incluindo um valor extremo de **750 anos**. Esses valores são claramente inválidos e provavelmente resultam de erros de digitação ou falhas na geração dos dados sintéticos.
# MAGIC
# MAGIC **Decisão:** Remover os registros com idade superior a 100 anos. Optamos pela remoção em vez de imputação porque:
# MAGIC
# MAGIC 1. O número de registros afetados é pequeno (15 em ~4.981), representando menos de 0,3% do dataset;
# MAGIC 2. Não temos contexto suficiente para inferir a idade correta desses registros;
# MAGIC 3. Imputar um valor arbitrário poderia introduzir ruído desnecessário nos dados.

# COMMAND ----------

# DBTITLE 1,Remoção de idades inválidas
# Remoção de registros com idade superior a 100 anos
n_antes = df.shape[0]
df = df[df['idade'] <= 100].reset_index(drop=True)
n_depois = df.shape[0]

print(f"Registros antes: {n_antes}")
print(f"Registros depois: {n_depois}")
print(f"Registros removidos: {n_antes - n_depois}")
print(f"\nNova idade máxima: {df['idade'].max()}")
print(f"Nova idade mínima: {df['idade'].min()}")

# COMMAND ----------

# DBTITLE 1,Tratamento de tempo_emprego_anos
# MAGIC %md
# MAGIC ## 3.5 Tratamento de `tempo_emprego_anos`
# MAGIC
# MAGIC Após remover os registros com idades inválidas, verificamos se o problema de `tempo_emprego_anos` com valor máximo de 74 anos persiste. É razoável que uma pessoa com 100 anos tenha até ~80 anos de emprego, mas valores muito altos são suspeitos.
# MAGIC
# MAGIC **Decisão:** Aplicar um limite superior razoável de 60 anos para `tempo_emprego_anos`. Valores acima desse limite serão ajustados (capped) para 60, já que representam casos extremamente improváveis mas não impossíveis, e a remoção poderia descartar informações válidas em outras colunas.

# COMMAND ----------

# DBTITLE 1,Tratamento de tempo_emprego_anos
# Verificação dos valores atuais de tempo_emprego_anos
print(f"Máximo atual: {df['tempo_emprego_anos'].max()}")
print(f"Registros com tempo > 60: {(df['tempo_emprego_anos'] > 60).sum()}")
print("\nRegistros com tempo_emprego_anos > 60:")
print(df.loc[df['tempo_emprego_anos'] > 60, ['idade', 'tempo_emprego_anos']])

# Aplicação do limite superior (cap) de 60 anos
n_capped = (df['tempo_emprego_anos'] > 60).sum()
df['tempo_emprego_anos'] = df['tempo_emprego_anos'].clip(upper=60)

print(f"\nRegistros ajustados (capped em 60): {n_capped}")
print(f"Novo máximo: {df['tempo_emprego_anos'].max()}")

# COMMAND ----------

# DBTITLE 1,Adequação dos Tipos de Variáveis
# MAGIC %md
# MAGIC ## 3.6 Adequação dos Tipos e Formatos das Variáveis
# MAGIC
# MAGIC Após os tratamentos, é importante garantir que as variáveis estejam com os tipos adequados para a modelagem:
# MAGIC
# MAGIC - **Variáveis categóricas** (`estado`, `escolaridade`, `finalidade`): converter para o tipo `category` do pandas, que é mais eficiente em memória e facilita o uso em pipelines de machine learning;
# MAGIC - **Variável resposta** (`inadimplente`): manter como inteiro (0/1), mas converter para `category` para sinalizar que é uma variável categórica;
# MAGIC - **Variáveis numéricas** (`idade`, `renda_mensal`, `tempo_emprego_anos`, `score_credito`, `valor_solicitado`, `prazo_meses`, `dividas_ativas`): já estão com tipos numéricos adequados, sem necessidade de conversão.

# COMMAND ----------

# DBTITLE 1,Conversão de tipos
# Conversão de variáveis categóricas para o tipo 'category'
colunas_categoricas = ['estado', 'escolaridade', 'finalidade']
for col in colunas_categoricas:
    df[col] = df[col].astype('category')

# Conversão da variável resposta para 'category' (categórica binária)
df['inadimplente'] = df['inadimplente'].astype('category')

print("Tipos das variáveis após conversão:")
print(df.dtypes)

# COMMAND ----------

# DBTITLE 1,Verificação Final e Salvamento
# MAGIC %md
# MAGIC ## 3.7 Verificação Final e Salvamento
# MAGIC
# MAGIC Após todos os tratamentos, realizamos uma verificação final para confirmar que:
# MAGIC
# MAGIC - Não há mais valores ausentes;
# MAGIC - Não há duplicatas;
# MAGIC - As dimensões do dataset são coerentes;
# MAGIC - Os tipos das variáveis estão corretos;
# MAGIC - As variáveis categóricas têm os valores esperados.
# MAGIC
# MAGIC O dataset limpo será salvo como um novo arquivo CSV para uso nas etapas subsequentes (engenharia de atributos, preparação para modelagem e modelagem).

# COMMAND ----------

# DBTITLE 1,Verificação final e salvamento do dataset limpo
# --- Verificação final ---
print("=" * 60)
print("VERIFICAÇÃO FINAL DO DATASET LIMPO")
print("=" * 60)

print(f"\n1. DIMENSÕES: {df.shape[0]} linhas x {df.shape[1]} colunas")

print(f"\n2. VALORES AUSENTES: {df.isnull().sum().sum()} valores ausentes")

print(f"\n3. DUPLICATAS: {df.duplicated().sum()} linhas duplicadas")

print(f"\n4. TIPOS DAS VARIÁVEIS:")
print(df.dtypes)

print(f"\n5. VARIÁVEIS CATEGÓRICAS:")
for col in ['estado', 'escolaridade', 'finalidade']:
    print(f"  {col}: {df[col].nunique()} valores únicos -> {sorted(df[col].unique().tolist())}")

print(f"\n6. ESTATÍSTICAS NUMÉRICAS:")
print(df.describe().round(2))

print(f"\n7. DISTRIBUIÇÃO DA VARIÁVEL RESPOSTA:")
print(df['inadimplente'].value_counts())
print((df['inadimplente'].value_counts(normalize=True) * 100).round(2))

# --- Salvamento ---
df.to_csv('/Workspace/Users/cafreitas@gmail.com/Repos/FT-IA---Analise-Credito/dataset_limpo.csv', index=False)
print(f"\n✅ Dataset limpo salvo em: dataset_limpo.csv")
print(f"   Registros originais: 5000 -> Registros finais: {df.shape[0]}")

# COMMAND ----------

# DBTITLE 1,Resumo das Decisões
# MAGIC %md
# MAGIC ## 3.8 Resumo das Decisões Tomadas
# MAGIC
# MAGIC | Problema | Decisão | Justificativa |
# MAGIC | --- | --- | --- |
# MAGIC | Valores ausentes | Nenhuma ação necessária | O dataset não possui valores ausentes |
# MAGIC | Duplicatas (19 registros) | Remoção, mantendo a primeira ocorrência | Evitar viés por registros duplicados no treinamento |
# MAGIC | `estado` com 85 valores únicos | `strip()` para remover espaços em branco | Normalizar para as 27 unidades federativas esperadas |
# MAGIC | Idades > 100 anos (15 registros) | Remoção dos registros | Valores claramente inválidos; baixo impacto (< 0,3% do dataset); imputação introduziria ruído |
# MAGIC | `tempo_emprego_anos` > 60 | Cap em 60 anos | Valores extremamente improváveis mas não impossíveis; preservação das demais informações do registro |
# MAGIC | Tipos das variáveis | Categóricas -> `category` | Eficiência de memória e compatibilidade com pipelines de ML |
# MAGIC
# MAGIC ### Impacto no dataset
# MAGIC
# MAGIC - **Registros originais:** 5.000
# MAGIC - **Registros após limpeza:** ~4.966 (19 duplicatas + ~15 idades inválidas removidas)
# MAGIC - **Perda de dados:** < 1% do total, preservando a representatividade do dataset