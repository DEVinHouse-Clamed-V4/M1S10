import pandas as pd
from src.database import connect_db


def extrair_alunos_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtypes= {
        'id_aluno': int,
        'nome': str,
        'email': str,
        'senha': str,
        'telefone': str
    })

    return df

def extrair_alunos_sql() -> pd.Dataframe: 
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        sql = 'SELECT * FROM tbl_alunos;'
        df = pd.read_sql(sql, conn)
        return df