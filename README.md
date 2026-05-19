# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%"></a>
</p>

<br>

## Nome do grupo

Equipe 7

## 👨‍🎓 Integrantes

* <a href="#">Luiz Henrique Martins Dias</a>
* <a href="#">Ricardo Colpani Sprocati de Oliveira</a>
* <a href="#">Walter Corradini Ferreira</a>
* <a href="#">Fahd Ozelame Al Khaldi</a>
* <a href="#">André Rohregger Machado</a>

## 👩‍🏫 Professores

### Tutor(a)

* <a href="#">Nicolly Candida Rodrigues de Souza</a>

### Coordenador(a)

* <a href="#">Andre Godoi Chiovato</a>

---

# 🌱 FarmTech Solutions – Fase 3

## 📌 Visão Geral do Projeto

O projeto FarmTech Solutions – Fase 3 tem como objetivo trabalhar com dados agrícolas no contexto do agronegócio, utilizando banco de dados, visualização de dados e técnicas de Machine Learning.

A proposta foi dividida em três partes principais:

- Entrega obrigatória: Banco de Dados Oracle;
- Programa Ir Além: Dashboard em Python;
- Programa Ir Além: Machine Learning no Agronegócio.

A entrega principal envolve a importação e consulta de dados agrícolas em um banco Oracle. As etapas complementares mostram outras formas de utilizar esses dados, seja por meio de uma dashboard interativa ou por modelos preditivos capazes de recomendar culturas agrícolas.

---

# 🗄️ Entrega Obrigatória – Banco de Dados Oracle

## 📌 Visão Geral

Nesta etapa, os dados agrícolas foram importados para um banco de dados Oracle utilizando o Oracle SQL Developer.

O objetivo foi armazenar os dados em uma tabela relacional e realizar consultas SQL para verificar, explorar e analisar as informações carregadas no banco.

Essa parte representa a base principal do projeto, pois permite organizar os dados de forma estruturada e acessá-los posteriormente por meio de consultas.

## 🎯 Objetivos da Entrega Obrigatória

A entrega obrigatória teve como principais objetivos:

- Criar uma conexão com o banco Oracle;
- Importar os dados agrícolas para uma tabela;
- Executar consultas SQL para visualizar os dados;
- Registrar prints das etapas realizadas;
- Documentar o processo no repositório GitHub;
- Mostrar o funcionamento em vídeo demonstrativo.

## 🧪 Consultas SQL

Após a importação dos dados, foram executadas consultas SQL para verificar se os registros foram carregados corretamente.

Exemplos de consultas utilizadas:

```sql
SELECT * FROM NOME_DA_TABELA;
```

```sql
SELECT COUNT(*) FROM NOME_DA_TABELA;
```

```sql
SELECT * FROM NOME_DA_TABELA WHERE ROWNUM <= 10;
```

As consultas permitem visualizar os dados armazenados, contar registros e verificar informações específicas da tabela.

## 📸 Prints do Banco
<p align="center">
  <img src="document/prints_oracle/Captura%20de%20tela%202026-05-18%20182549.jpg" alt="print oracle" >
</p>
<p align="center">
  <img src="document/prints_oracle/Captura%20de%20tela%202026-05-18%20162928.jpg" alt="print oracle" >
</p>
<p align="center">
  <img src="document/prints_oracle/Captura%20de%20tela%202026-05-18%20182706.jpg" alt="print oracle" >
</p>
---

# 📊 Programa Ir Além – Dashboard em Python

## 📌 Visão Geral

Esta etapa do projeto tem como objetivo desenvolver uma dashboard interativa em Python para visualização e análise dos dados agrícolas armazenados no banco Oracle.

A aplicação foi desenvolvida utilizando:

- Streamlit;
- oracledb;
- Pandas;
- Matplotlib.

A dashboard consome diretamente os dados armazenados no banco Oracle utilizado na Fase 3.

## 🎯 Objetivos da Dashboard

A aplicação permite:

- Visualizar níveis de Nitrogênio, Fósforo e Potássio;
- Monitorar Umidade, Temperatura e Chuva;
- Analisar o pH do solo;
- Filtrar dados por tipo de cultura;
- Gerar sugestão automática de irrigação baseada em clima.

## 🗂 Estrutura do Projeto da Dashboard

```text
dashboard/
│
├── app.py
├── db.py
└── requirements.txt
```

## 🛠 Preparação do Ambiente Local

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv
```

### 2️⃣ Ativar o ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependências

```bash
pip install streamlit oracledb pandas matplotlib
```

### 4️⃣ Gerar arquivo de dependências

```bash
pip freeze > requirements.txt
```

### 5️⃣ Executar a dashboard

```bash
streamlit run app.py
```

---

# 🤖 Programa Ir Além – Machine Learning no Agronegócio

## 📌 Visão Geral

Além da dashboard, também foi desenvolvida uma etapa complementar de análise de dados e Machine Learning aplicada ao agronegócio.

Essa parte do projeto foi construída em um Jupyter Notebook, utilizando uma base de dados agrícola com informações de solo, clima e culturas recomendadas.

O objetivo foi analisar os dados, identificar padrões entre as variáveis e testar modelos capazes de prever a cultura agrícola mais adequada com base nas condições de solo e clima.

A base utilizada contém variáveis como:

- Nitrogênio;
- Fósforo;
- Potássio;
- Temperatura;
- Umidade;
- pH;
- Chuva;
- Cultura recomendada.

## 🎯 Objetivos do Notebook

O notebook tem como principais objetivos:

- Realizar uma análise exploratória dos dados;
- Criar gráficos para entender melhor o comportamento das variáveis;
- Comparar o perfil médio de solo e clima para três culturas;
- Desenvolver modelos preditivos com diferentes algoritmos;
- Avaliar e comparar o desempenho dos modelos;
- Demonstrar uma aplicação prática de Machine Learning no contexto do agronegócio.

## 📁 Base de Dados Utilizada

A base utilizada no notebook foi o arquivo:

```text
Atividade_Cap10_produtos_agricolas.csv
```

Ela contém informações relacionadas a nutrientes do solo, clima e cultura agrícola recomendada.

As principais colunas da base são:

| Coluna | Descrição |
|---|---|
| `N` | Quantidade de nitrogênio no solo |
| `P` | Quantidade de fósforo no solo |
| `K` | Quantidade de potássio no solo |
| `temperature` | Temperatura |
| `humidity` | Umidade |
| `ph` | Nível de acidez ou alcalinidade do solo |
| `rainfall` | Índice de chuva |
| `label` | Cultura agrícola recomendada |

A coluna `label` foi utilizada como variável alvo dos modelos de Machine Learning.

## 📊 Análise Exploratória

Na primeira etapa do notebook, foi feita uma análise inicial da base de dados para verificar:

- Quantidade de linhas e colunas;
- Tipos de dados;
- Existência de valores nulos;
- Distribuição das culturas;
- Estatísticas gerais das variáveis numéricas.

Também foram criados gráficos para auxiliar na interpretação dos dados, como:

- Distribuição das culturas na base;
- Matriz de correlação entre variáveis numéricas;
- Temperatura por cultura;
- Umidade por cultura;
- Chuva por cultura;
- pH por cultura.

Essa etapa ajudou a entender melhor o comportamento dos dados antes da criação dos modelos preditivos.

## 🌾 Perfil Ideal de Solo e Clima

Para comparar melhor as características das culturas, foram escolhidas três culturas da base:

- `rice`;
- `maize`;
- `coffee`.

Para cada uma delas, foi calculada a média das variáveis de solo e clima.

A comparação mostrou que cada cultura possui características diferentes. A cultura `rice`, por exemplo, apresentou maior relação com umidade e chuva. A cultura `coffee` apresentou maior média de nitrogênio entre as três analisadas, enquanto `maize` apresentou valores mais moderados em relação às variáveis climáticas.

Essa análise reforça que as culturas agrícolas possuem necessidades diferentes e que os dados podem ajudar na recomendação da cultura mais adequada.

## 🧠 Modelos de Machine Learning

Foram desenvolvidos cinco modelos preditivos com algoritmos distintos:

- Regressão Logística;
- Árvore de Decisão;
- Random Forest;
- KNN;
- SVM.

Os modelos foram treinados com o objetivo de prever a cultura agrícola recomendada a partir das variáveis de solo e clima.

## 📈 Avaliação dos Modelos

Os modelos foram avaliados utilizando métricas de classificação, como:

- Acurácia;
- Precision;
- Recall;
- F1-score;
- Matriz de confusão.

Após o treinamento, os resultados foram comparados para identificar qual algoritmo apresentou melhor desempenho na previsão das culturas.

O modelo com melhor desempenho foi:

```text
Random Forest
```

Com acurácia de:

```text
0.9955
```

## 🗂 Estrutura da Etapa de Machine Learning
```text
machine_learning/
│
├── machine-learning.ipynb
└── Atividade_Cap10_produtos_agricolas.csv
```

## 🛠 Bibliotecas Utilizadas

Para o desenvolvimento do notebook, foram utilizadas as seguintes bibliotecas:

- Pandas;
- NumPy;
- Matplotlib;
- Seaborn;
- Scikit-learn.

## ▶️ Como Executar o Notebook

### 1️⃣ Instalar as dependências

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

### 2️⃣ Abrir o Jupyter Notebook

```bash
jupyter notebook
```

### 3️⃣ Executar o arquivo

Abra o arquivo:

```text
machine-learning.ipynb
```

Execute as células em ordem, desde a importação das bibliotecas até a avaliação dos modelos.

---

# 📹 Vídeo Geral do Projeto

O vídeo abaixo apresenta as três etapas do projeto: Banco de Dados Oracle, Dashboard em Python e Machine Learning.

```text

```

---

# ✅ Conclusão Geral

O projeto FarmTech Solutions – Fase 3 trabalhou com dados agrícolas em diferentes etapas.

Na entrega principal, os dados foram importados e consultados em um banco de dados Oracle. Em seguida, a dashboard em Python permitiu visualizar os dados de forma mais prática e interativa.

Por fim, a etapa de Machine Learning mostrou como os dados agrícolas podem ser utilizados para análise e previsão, permitindo recomendar culturas com base em características de solo e clima.

Dessa forma, o projeto conecta banco de dados, visualização de dados e inteligência artificial em uma solução aplicada ao agronegócio.

---

# 📁 Estrutura Geral do Repositório

```text
Sistema-FarmTech-fase3/
│
├── assets/
│   └── logo-fiap.png
│
├── dashboard/
│   ├── app.py
│   ├── db.py
│   └── requirements.txt
│
│
├── machine_learning/
│   ├── machine-learning.ipynb
│   └── Atividade_Cap10_produtos_agricolas.csv
│
├── document/
│   └── prints_oracle/
│
└── README.md
```

---
