import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../../')))

from extract import *
from transform import *
from load import *

def pipeline_alunos():
    #1. Extract
    df_alunos = extrair_alunos_csv('../../data/raw/alunos.csv')
    print('Alunos coletados com sucesso!')

    #2. Transform
    df_alunos_clean = limpar_alunos_csv(df_alunos)
    print('Transformação concluída com sucesso!')

    #3. Load
    carregar_alunos_db(df_alunos_clean)
    print('Carga concluída com sucesso!')

if __name__ == "__main__":
    pipeline_alunos()