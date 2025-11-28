import psycopg2 as pg
import pandas as pd

#Conexão com banco de dados
def connect_db(dbname, user, password, port, host):
    try:
        return pg.connect(
            dbname=dbname,
            user=user,
            password=password,
            port=port,
            host=host
        )
    except:
        print("Erro: Falha ao conectar com o banco de dados!")

def cadastrar_aluno(nome: str, email: str, senha: str, telefone: str):
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('INSERT INTO tbl_aluno(nome, email, senha, telefone) VALUES (%s, %s, %s, %s)',
                            (nome, email, senha, telefone))
            except:
                print('Error: Falha ao cadastrar aluno!')

def listar_alunos_por_turma(turma_id: int):
        with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
            with conn.cursor() as cur:
                try: 
                    cur.execute("""
                        SELECT a.nome
                        FROM tbl_aluno a
                        JOIN tbl_aluno_has_turma at ON a.id_aluno = at.fk_aluno
                        WHERE at.fk_turma = %s;
                    """, (turma_id,))
                    return cur.fetchall()
                except:
                    print("Erro: Falha ao listar os aluno por turma!")

def buscar_alunos_por_turno(turno: str):
    '''
        Retorna os alunos por turno.

        Parâmetros:
            - turno: str 
    '''
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    SELECT a.nome, t.nome
                    FROM tbl_aluno a
                    JOIN tbl_aluno_has_turma at ON a.id_aluno = at.fk_aluno
                    JOIN tbl_turma t ON t.id_turma = at.fk_turma
                    WHERE t.turno = %s;
                """, (turno,))
                return cur.fetchall()
            except:
                print("Erro: Falha ao buscar alunos por turno!")

def quantidade_alunos_por_turma():
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    SELECT t.nome, COUNT(at.fk_aluno) AS total_alunos
                    FROM tbl_turma t
                    LEFT JOIN tbl_aluno_has_turma at ON at.fk_turma = t.id_turma
                    GROUP BY t.nome
                ''')
            except:
                print(f'Erro: Falha ao retornar quantidade de alunos por turma!')

            return cur.fetchall()

#Retornar os e-mails dos alunos por uma determinada turma
def emails_alunos_por_turma(turma_id: int):
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    SELECT a.email 
                    FROM tbl_aluno a
                    JOIN tbl_aluno_has_turma at ON a.id_aluno = at.fk_aluno
                    WHERE at.fk_turma = %s;
                ''', (turma_id,))
                return cur.fetchall()
            except:
                print('Erro: Falha ao listar os e-mails!')

#cadastrar_aluno('Davi Saldanha', 'davi@email.com', 'davi01', '8590001245')
'''
dataset = emails_alunos_por_turma(2)

for i in dataset:
    print(i[0])
'''
sql = 'SELECT * FROM tbl_aluno;'
con = connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost')

df = pd.read_sql(sql, con)

con.close()

print(df.info())

'''
    DESAFIO: Gerar uma plotagem que apresente a distribuição de alunos por turno
'''
import matplotlib.pyplot as plt
def plot_alunos_por_turno():
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    SELECT t.turno, COUNT(at.fk_aluno) AS total_alunos
                    FROM tbl_turma t
                    LEFT JOIN tbl_aluno_has_turma at ON at.fk_turma = t.id_turma
                    GROUP BY t.turno;
                ''')
                data = cur.fetchall()
                
                turnos = [row[0] for row in data]
                total_alunos = [row[1] for row in data]

                plt.bar(turnos, total_alunos, color=['blue', 'orange', 'green'])
                plt.xlabel('Turno')
                plt.ylabel('Número de Alunos')
                plt.title('Distribuição de Alunos por Turno')
                plt.show()
            except:
                print('Erro: Falha ao gerar plotagem!')

plot_alunos_por_turno()




