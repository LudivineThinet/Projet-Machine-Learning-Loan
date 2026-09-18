import streamlit as st

st.set_page_config(page_title="CrediTrust - Scoring de crédit", layout="wide")

st.title("CrediTrust Finance - Dashboard de scoring de crédit")

st.markdown("""
Ce dashboard permet d'explorer les données de demandes de prêt et de tester
l'éligibilité d'un client via un modèle de Machine Learning entraîné sur
l'historique des décisions passées.

Utilise le menu à gauche pour naviguer :
- **Analyse** : vue d'ensemble du portefeuille, facteurs de risque, performance du modèle.
- **Simulateur** : teste une demande de prêt en direct.
""")