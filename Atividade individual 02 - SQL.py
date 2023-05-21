import psycopg2

# Classe para a conexão com o banco de dados
class Conexao:

    def __init__(self, dbname, host, port, user, password) -> None:
        self._dbname = dbname
        self._host = host
        self._port = port
        self._user = user
        self._password = password
    
    def consultarBanco(self, sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)
        cursor = conn.cursor()
        cursor.execute(sql)
        resultado = cursor.fetchall()
        cursor.close()
        conn.close()
        return resultado
    
    def manipularBanco(self,sql):
        conn = psycopg2.connect(dbname = self._dbname, host = self._host, port = self._port, user = self._user, password = self._password)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        conn.close()

con = Conexao(dbname = "Escola" ,host = "localhost", port = "5432", user = "postgres", password = "postgres" )

#   Código SQL referente a criação das seguintes tabelas
# — Alunos: NroMatricula, nome, cpf, endereço, telefone, anoNascimento
# — Disciplina: CodDisciplina, nome, codigo do curso a qual ela pertence
# — Matricula: NroMatricula, CodDisciplina, Semestre, Ano, Nota, NroFaltas 

def criartabela_alunos(conexao):
    sql = conexao.manipularBanco ('''
    create table "Alunos"(
    "NroMatricula" int GENERATED ALWAYS AS IDENTITY,
    "nome" varchar(255) not null,
    "cpf" char(11) not null unique,
    "endereço" varchar(255),
    "telefone" varchar(11),
    "anoNascimento" varchar(10),
    primary key ("NroMatricula")
    )
    ''')
    return sql

def criartabela_disciplina(conexao):
    sql = conexao.manipularBanco ('''
    create table "Disciplina"(
    "CodDisciplina" int GENERATED ALWAYS AS IDENTITY,
    "nome" varchar(255) not null,
    "codigo_curso" int not null,
    primary key ("CodDisciplina"))
    ''')
    return sql


def criartabela_matricula(conexao):
    sql = conexao.manipularBanco (''' 
    create table "Matricula"(
    "id" int GENERATED ALWAYS AS IDENTITY,
    "NroMatricula" int not null,
    "CodDisciplina" int not null,
    "Semestre" int not null,
    "Ano" int not null,
    "Nota" int not null,
    "NroFaltas" int not null,
    primary key("id"),

    CONSTRAINT fk_aluno
      FOREIGN KEY ("NroMatricula")
      REFERENCES "Alunos"("NroMatricula"),

    CONSTRAINT fk_disciplina
      FOREIGN KEY ("CodDisciplina")
      REFERENCES "Disciplina"("CodDisciplina")
    )
    ''')
    return sql


def criar_tabelas():
    criartabela_alunos(con)
    criartabela_disciplina(con)
    criartabela_matricula(con)

