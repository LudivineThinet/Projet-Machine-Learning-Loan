import streamlit as st
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

st.set_page_config(page_title="CrediTrust", page_icon="🏦")

st.title("CrediTrust Finance - Dashboard de scoring de crédit")

st.markdown("""
### Contexte

Ce projet a été réalisé pour **CrediTrust Finance**, accompagné par **NexaData Consulting**,
dans le cadre d'un brief Machine Learning.

L'objectif : s'appuyer sur l'historique des décisions de prêt déjà prises pour aider à évaluer
le risque associé à une nouvelle demande, avec une attention particulière portée à la réduction
des faux négatifs (accorder un prêt à quelqu'un qui aurait dû être refusé).

### Navigation

Utilise le menu à gauche :
- **Analyse** : vue d'ensemble du portefeuille de prêts, facteurs de risque.
- **Simulateur** : teste une demande de prêt en direct avec le modèle entraîné.
""")