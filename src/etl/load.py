import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from src.database import cadastrar_aluno 

import pandas as pd

def carregar_alunos_db(df: pd.DataFrame):

    for _, row in df.iterrows():
        cadastrar_aluno(row['nome'], row['email'], row['senha'], row['telefone'])

