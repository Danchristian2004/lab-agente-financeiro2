import streamlit as st
import pandas as pd

# Simulação de carregamento de dados
def load_data():
    perfil = {"nome": "João Silva", "perfil": "Moderado", "reserva_atual": 10000}
    produtos = [
        {"nome": "Tesouro Selic", "indicado": "Reserva de Emergência"},
        {"nome": "CDB Liquidez Diária", "indicado": "Segurança e Rendimento"}
    ]
    return perfil, produtos

st.title("🏦 B-Fin: Seu Assistente Bradesco")

perfil, produtos = load_data()

st.sidebar.markdown(f"### Olá, {perfil['nome']}!")
st.sidebar.write(f"Perfil: **{perfil['perfil']}**")

prompt = st.chat_input("Como posso ajudar suas finanças hoje?")

if prompt:
    with st.chat_message("assistant"):
        if "investir" in prompt.lower():
            st.write(f"Vi que você tem R$ 10.000 na reserva. Para chegar nos R$ 15.000, recomendo o {produtos[1]['nome']}.")
        else:
            st.write("Estou analisando seu histórico para te dar a melhor direção.")