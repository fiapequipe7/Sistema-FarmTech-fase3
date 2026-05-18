import streamlit as st
from db import get_data

st.set_page_config(layout="wide")
st.title("🌱 FarmTech Solutions – Dashboard Agrícola")

df = get_data()

# ======================
# FILTRO POR CULTURA
# ======================

culturas = df["CROP_TYPE"].unique()
cultura_selecionada = st.selectbox("Selecione a Cultura:", culturas)

df_filtrado = df[df["CROP_TYPE"] == cultura_selecionada]

# ======================
# MÉTRICAS
# ======================

col1, col2, col3, col4 = st.columns(4)

col1.metric("Umidade Média", round(df_filtrado["HUMIDITY"].mean(), 2))
col2.metric("Temperatura  Média", round(df_filtrado["TEMPERATURE"].mean(), 2))
col3.metric("Fósforo Médio", round(df_filtrado["PHOSPHOROUS"].mean(), 2))
col4.metric("Potássio Médio", round(df_filtrado["POTASSIUM"].mean(), 2))

# ======================
# GRÁFICOS
# ======================

st.subheader("Níveis de Nutrientes (N, P, K)")
st.line_chart(df_filtrado[["NITROGEN", "PHOSPHOROUS", "POTASSIUM"]])

st.subheader("Umidade e Chuva")
st.line_chart(df_filtrado[["HUMIDITY", "MOISTURE"]])

st.subheader("Temperatura")
st.line_chart(df_filtrado["TEMPERATURE"])

# ======================
# SUGESTÃO DE IRRIGAÇÃO
# ======================

st.subheader("Sugestão de Irrigação")

media_umidade = df_filtrado["HUMIDITY"].mean()
media_chuva = df_filtrado["MOISTURE"].mean()
media_temperatura = df_filtrado["TEMPERATURE"].mean()

if media_umidade < 60 and media_chuva < 25 and media_temperatura > 25:
    st.warning("Recomenda-se irrigar a cultura, pois os níveis de umidade e chuva estão baixos e a temperatura está alta.")
else:
    st.success("As condições atuais parecem adequadas, não é necessário irrigar no momento.")