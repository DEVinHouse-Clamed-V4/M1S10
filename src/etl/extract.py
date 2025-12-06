import pandas as pd
import numpy as np
from src.database import connect_db


def extrair_alunos_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype = {
        'id_aluno': object,
        'nome': str,
        'email': str,
        'senha': str,
        'telefone': str
    })

    return df

def extrair_alunos_sql() -> pd.Dataframe: 
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        sql = 'SELECT * FROM tbl_aluno;'
        df = pd.read_sql(sql, conn)
        return df