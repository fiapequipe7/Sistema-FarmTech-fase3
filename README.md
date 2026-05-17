# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## Nome do grupo

Equipe 7

## 👨‍🎓 Integrantes:

* <a href="#">Luiz Henrique Martins Dias</a>
* <a href="#">Ricardo Colpani Sprocati de OLiveira</a>
* <a href="#">Walter Corradini Ferreira</a>
* <a href="#">Fahd Ozelame Al Khaldi</a>
* <a href="#">Eric Roberto Miglioli</a>

## 👩‍🏫 Professores:

### Tutor(a)

* <a href="#">Nicolly Candida Rodrigues de Souza</a>

### Coordenador(a)

* <a href="#">Andre Godoi Chiovato</a>

---


# 🌱 FarmTech Solutions – Fase 3  

# Entrega obratória ...


## 📊 Programa Ir Além – Dashboard em Python

---

## 📌 Visão Geral

Esta etapa do projeto tem como objetivo desenvolver uma **dashboard interativa em Python** para visualização e análise dos dados agrícolas armazenados no banco Oracle.

A aplicação foi desenvolvida utilizando:

- Streamlit  
- oracledb (driver Oracle para Python)  
- Pandas  
- Matplotlib  

A dashboard consome diretamente os dados armazenados no banco Oracle utilizado na Fase 3.

---

## 🎯 Objetivos da Dashboard

A aplicação permite:

- Visualizar níveis de **Nitrogênio, Fósforo e Potássio**
- Monitorar **Umidade, Temperatura e Chuva**
- Analisar o **pH do solo**
- Filtrar dados por tipo de cultura
- Gerar **sugestão automática de irrigação baseada em clima**

---

## 🗂 Estrutura do Projeto


fase3_dashboard/
│
├── app.py
├── db.py
├── requirements.txt
└── README.md


---

## 🛠 Preparação do Ambiente Local

### 1️⃣ Criar ambiente virtual

```bash
python -m venv venv

Ativar:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
2️⃣ Instalar dependências
pip install streamlit oracledb pandas matplotlib

Gerar arquivo de dependências:

pip freeze > requirements.txt

## 📹 Vídeo Demonstrativo

Link do vídeo no YouTube: