from .database import connect_db
import matplotlib.pyplot as plt

def ranking_alunos_por_curso():
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            sql = '''
WITH medias AS ( 
		SELECT h.fk_aluno,
		       ROUND(AVG(h.media),2) AS media
	      FROM tbl_historico h
		 group by h.fk_aluno
),

relacionamentos AS ( 
		SELECT c.nome AS curso,
		       a.nome AS aluno,
			   m.media,
			   ROW_NUMBER() OVER (PARTITION BY c.nome ORDER BY m.media DESC) AS posicao_curso
		  FROM tbl_aluno a
		  JOIN medias m ON m.fk_aluno = a.id_aluno
		  JOIN tbl_historico h ON h.fk_aluno = a.id_aluno
		  JOIN tbl_turma t ON t.id_turma = h.fk_turma
		  JOIN tbl_curso c ON c.id_curso = t.fk_curso
)

	SELECT * 
	  FROM relacionamentos
	 ORDER BY curso, posicao_curso;
'''
            try:
                cur.execute(sql)
                return cur.fetchall()
            except:
                print('Erro: Falha ao retornar ranking de alunos por turma!\n')

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

def alunos_por_turno():
    with connect_db('lab365', 'postgres', 'postgres', 5433, 'localhost') as conn:
        with conn.cursor() as cur:
            try:
                cur.execute('''
                    SELECT t.turno, COUNT(at.fk_aluno) AS total_alunos
                    FROM tbl_turma t 
                    JOIN tbl_aluno_has_turma at ON t.id_turma = at.fk_turma
                    GROUP BY t.turno;
                ''')
                data = cur.fetchall()
                return data
            except Exception as e:
                print(f"Erro: {e}")
