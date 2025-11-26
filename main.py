import psycopg2 as pg

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

#cadastrar_aluno('Davi Saldanha', 'davi@email.com', 'davi01', '8590001245')

dataset = buscar_alunos_por_turno('Tarde')

for i in dataset:
    print(i)




