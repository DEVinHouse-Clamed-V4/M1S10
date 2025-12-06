import pandas as pd
import numpy as np
import re

def limpar_alunos_csv(df: pd.DataFrame):
    df_clean = df.copy()

    # --------------------
    # Tratamento id_aluno
    # --------------------
    df_clean['id_aluno'] = pd.to_numeric(df_clean['id_aluno'], errors='coerce')
    df_clean['id_aluno'] = df_clean['id_aluno'].dropna().astype(int)

    # --------------------
    # Tratamento nome
    # --------------------
    def limpar_nome(nome):
        if pd.isna(nome) or nome.strip() == "":
            return np.nan
        
        nome = nome.strip()
        nome = re.sub(r'\s+', ' ', nome)
        nome = nome.title()
        return nome

    df_clean['nome'] = df_clean['nome'].apply(limpar_nome)
    df_clean.fillna({'nome': 'Não Informado'}, inplace=True)

    # --------------------
    # Tratamento email
    # --------------------
    def limpar_email(email):
        if pd.isna(email) or email.strip() == "":
            return np.nan
        email = email.strip().lower()
        email = email.replace('..', '.').replace('@@', '@')

        if '@' not in email or '.' not in email.split('@')[-1]:
            return np.nan
        
        return email
    
    df_clean['email'] = df_clean['email'].apply(limpar_email)
    df_clean.fillna({'email': 'Não Informado'}, inplace=True)

    # --------------------
    # Tratamento senha
    # --------------------
    def limpar_senha(senha):
        if pd.isna(senha) or senha.strip() == "":
            return np.nan
        return senha.strip()

    df_clean['senha'] = df_clean['senha'].apply(limpar_senha)
    df_clean.fillna({'senha': 'senha123'}, inplace=True)

    # --------------------
    # Tratamento telefone
    # --------------------
    def limpar_telefone(telefone):
        if pd.isna(telefone) or telefone.strip() == "":
            return np.nan
        telefone = re.sub(r'\D', '', telefone)

        if len(telefone) != 11:
            return np.nan

        return telefone

    df_clean['telefone'] = df_clean['telefone'].apply(limpar_telefone)
    df_clean.fillna({'telefone': 'N/A'}, inplace=True)

    # --------------------
    # Remoção Duplicatas
    # --------------------
    
    df_clean.drop_duplicates(subset=['id_aluno'], inplace=True)
    df_clean = df_clean.drop_duplicates(subset=['nome', 'email', 'telefone', 'senha'])


    df_clean = df_clean.reset_index(drop=True)

    return df_clean
