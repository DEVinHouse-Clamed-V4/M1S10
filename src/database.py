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
        print("Erro: Falha ao conectar com o banco de dados!\n")

def cadastrar_aluno(nome: str, email: str, senha: str, telefone: str):

    '''
        Cadastra um novo aluno no banco de dados.

        Parâmetros:
            - nome: str
            - email: str
            - senha: str
            - telefone: str
    '''
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('INSERT INTO tbl_aluno(nome, email, senha, telefone) VALUES (%s, %s, %s, %s)',
                            (nome, email, senha, telefone))
            except Exception as e:
                print('Error: Falha ao cadastrar aluno! ', e)

